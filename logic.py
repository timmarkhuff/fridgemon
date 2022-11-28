from tkinter import PhotoImage
from datetime import datetime, timedelta
import random
from time import sleep
from timeit import default_timer as timer
from threading import Thread
import platform

# OS-specific imports and initializations
OS = platform.system()
if OS == 'Linux':
    import gpiozero
    rpi_button = gpiozero.Button(4)
else:
    import keyboard

# constants
SECONDS_PER_DAY = 30 # num of actual seconds per simulated day
FOOD_LABELS = ['Steak', 'Cake', 'Salmon', 'Spaghetti',
            'Linguine', 'Bulgogi', 'Stew', 'Halibut', 'Burger', 'Gumbo',
            'Chow Mein', 'Pho'] #, 'Soup', 'Sushi', 'Chicken Parm',
            # 'Lasagna', 'Fajitas', 'Tacos', 'Carne Asada', 'Fried Rice',
            # 'Pancakes', 'Rice Cakes', 'Burrito', 'Enchiladas', 'Quesadilla',
            # 'Pork Chop', 'Ravioli', 'Dumplings', 'Pot Stickers', 'Pizza',
            # 'Japchae', 'Bibimbap', 'Gyro', 'Biryani', 'Samosa', 'Tikka Masala',
            # 'Naengmyeon', 'Palak Paneer', 'Korma', 'Menudo', 'Udon', 'Tempura',
            # 'Gyudon', 'Sashimi']

FOOD_LABELS.sort()

def simulate_today():
    """
    simulates the passage of time at a faster rate
    for simulation purposes
    """
    return datetime.today() + timedelta(days=timer()/SECONDS_PER_DAY)

class FridgeMon:
    def __init__(self):
        # create Tag objects from csv
        self.tags = {}
        with open('tags.csv') as f:
            lines = f.readlines()
            lines = lines[1:] # remove the column header
            for line in lines:
                line_split = line.split(',')
                id = line_split[0]
                name = line_split[1]
                color = line_split[2]
                icon_path = line_split[3]
                tag = Tag(self, id, name, color, icon_path)
                self.tags[id] = tag
                
                # skip empty rows
                if line[0] == ',':
                    continue

                # randomly label some tags as being in fridge
                if random.randint(0,2):
                    # choose a random food label
                    label = random.choice(FOOD_LABELS)

                    # choose a random start_date
                    today = simulate_today()
                    rand_time_delta = timedelta(days = random.randint(0,5))
                    start_date = today - rand_time_delta

                    tag.stock_fridge(start_date, label)

    def scan_contents_simulated(self) -> tuple:
        for tag in self.tags.values():
            if not random.randint(0,2):
                if tag.is_in_fridge:
                    tag.remove_from_fridge()
                else:
                    tag.add_to_fridge(simulate_today())

        # sleep a random amount of time to simulate scanning
        sleep(random.randint(1,2))

class Tag:
    def __init__(self, fm, id: int, name: str, color: str, icon_path: str):
        self.fm: FridgeMon = fm
        self.id: int = id
        self.name: str = name
        self.color: str = color
        self.icon_path: str = icon_path
        self.icon: PhotoImage = None
        self.label: str = None
        self.previous_label: str = None
        self.start_date = None
        self.previous_start_date = None
        self.is_in_fridge = False

    def stock_fridge(self, start_date: datetime, label:str):
        self.is_in_fridge = True
        self.label = label
        self.previous_label = label
        self.start_date = start_date
        self.previous_start_date = start_date
        self.start_time = timer()

    def add_to_fridge(self, start_date: datetime) -> None:
        self.is_in_fridge = True
        self.start_date = start_date
        self.start_time = timer()
        self.unlabel()

    def remove_from_fridge(self) -> None:
        self.previous_start_date = self.start_date
        self.is_in_fridge = False

    def label_contents(self, label:str) -> None:
        self.label = label

    def keep_as_last(self):
        self.label = self.previous_label
        self.start_date = self.previous_start_date

    def unlabel(self):
        self.previous_label = self.label
        self.label = None

    def is_labeled(self):
        return self.label is not None

    def get_icon(self):
        """
        returns the icon for the tag
        if the icon hasn't already been read from the filepath,
        then it will be read
        """
        if self.icon is None:
            self.icon = PhotoImage(file=self.icon_path)
        return self.icon

    def get_days_in_fridge(self):
        """
        simulated days
        """
        today = simulate_today()
        return (today - self.start_date).days

    def get_previous_days_in_fridge(self):
        """
        simulated days that the previous contents spent in the fridge
        """
        today = simulate_today()
        return (today - self.previous_start_date).days

    def get_seconds_in_fridge(self):
        """
        actual seconds
        """
        return timer() - self.start_time 

class DoorButton:
    def __init__(self, ui, mon):
        self.ui = ui
        self.mon = mon
        self.run = True
        self.position = 0
        self.positions = [0,0]

    def start(self):
        def thread():
            x = 0
            while self.run:
                sleep(.05)
                if OS == 'Linux':
                    # for RPI
                    self.position = rpi_button.is_pressed
                else:
                    self.position = keyboard.is_pressed('0')
                    
                # update the list of positions
                self.positions.append(self.position)
                self.positions = self.positions[1:]

                door_opened = (self.positions[0] == 0 and self.positions[1] == 1)
                door_closed = (self.positions[0] == 1 and self.positions[1] == 0)

                if door_opened or door_closed:
                    if self.ui.active_screen == 'label':
                        self.ui.return_to_item_screen()
                    else:
                        self.ui.refresh_item_buttons()
                if door_opened:
                    self.ui.show_open()
                elif door_closed:
                    self.ui.start_progress_bar()
                    self.mon.scan_contents_simulated()
                    self.ui.stop_progress_bar()
                    self.ui.show_closed()
                    self.ui.refresh_item_buttons()
                x += 1
        Thread(target=thread).start()

    def stop(self):
        self.run = False