from tkinter import PhotoImage
from datetime import datetime, timedelta
import random
from time import sleep
from timeit import default_timer as timer
from threading import Thread
import platform
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# OS-specific imports and initializations
OS = platform.system()
if OS == 'Linux':
    import gpiozero
    rpi_button = gpiozero.Button(4)
else:
    import keyboard

# constants
SECONDS_PER_DAY = 30 # num of actual seconds per simulated day
FOOD_LABELS = sorted(['Steak', 'Cake', 'Salmon', 'Spaghetti',
            'Linguine', 'Bulgogi', 'Stew', 'Halibut', 'Burger', 'Gumbo',
            'Chow Mein', 'Pho']) # sort food labels alphabetically

            #### Extra Labels ####
            #, 'Soup', 'Sushi', 'Chicken Parm',
            # 'Lasagna', 'Fajitas', 'Tacos', 'Carne Asada', 'Fried Rice',
            # 'Pancakes', 'Rice Cakes', 'Burrito', 'Enchiladas', 'Quesadilla',
            # 'Pork Chop', 'Ravioli', 'Dumplings', 'Pot Stickers', 'Pizza',
            # 'Japchae', 'Bibimbap', 'Gyro', 'Biryani', 'Samosa', 'Tikka Masala',
            # 'Naengmyeon', 'Palak Paneer', 'Korma', 'Menudo', 'Udon', 'Tempura',
            # 'Gyudon', 'Sashimi']

def simulate_today():
    """
    Simulates the passage of time at a faster rate
    for simulation purposes
    """
    return datetime.today() + timedelta(days=timer()/SECONDS_PER_DAY)

class FridgeMon:
    """
    Contains the logic and tracks the internal state
    of the FridgeMon system
    """
    def __init__(self):
        # Define the RFID reader, for Raspberry Pi only
        if OS == 'Linux':
            self.rfid_reader = SimpleMFRC522()
        
        # create Tag objects from csv
        self.tags = {}
        with open('tags.csv') as f:
            lines = f.readlines()
            lines = lines[1:] # remove the column header
            for line in lines:
                # skip empty rows
                if line[0] == ',':
                    continue

                # create a Tag object
                line_split = line.split(',')
                id = line_split[0]
                name = line_split[1]
                icon_path = line_split[2]
                tag = Tag(id, name, icon_path)
                self.tags[id] = tag
                
                # randomly label some tags as being in fridge
                if random.randint(0,2):
                    # choose a random food label
                    label = random.choice(FOOD_LABELS)

                    # choose a random start_date
                    today = simulate_today()
                    rand_time_delta = timedelta(days = random.randint(0,5))
                    start_date = today - rand_time_delta

                    tag.stock_fridge(start_date, label)

    def scan_contents_simulated(self):
        """"
        Randomly adds and removes tags from the fridge for demo purposes.
        Eventually, this would be replaced by a function that actually scans for
        RFID tags in the fridge and adds/removes tags accordingly.   
        """
        for tag in self.tags.values():
            if not random.randint(0,2):
                if tag.is_in_fridge:
                    tag.remove_from_fridge()
                else:
                    tag.add_to_fridge(simulate_today())

        # sleep a random amount of time to simulate scanning
        sleep(random.randint(1,2))

    def scan_contents(self, times=50):
        """
        Uses the actual RFID reader to scan for tags
        """
        # scan for tags
        id_list = []
        for i in range(times):
            sleep(0.03)
            try:
                id = self.rfid_reader.read_id_no_block()
                id = str(id)
                if (not id in id_list) and (not id == "None") :
                    id_list.append(id)
                i+=10
            finally:
                a=1
        
        # add and remove tags from fridge accordingly
        for tag in self.tags.values():
            if not tag.id in id_list:
                tag.remove_from_fridge()
            else:
                tag.add_to_fridge(simulate_today())
                

class Tag:
    """
    A class for the RFID tags that are attached to the food containers
    """
    def __init__(self, id: int, name: str, icon_path: str):
        self.id = id
        self.name = name
        self.icon_path = icon_path
        self.icon: PhotoImage = None
        self.label: str = None
        self.previous_label: str = None
        self.start_date = None
        self.previous_start_date = None
        self.is_in_fridge = False

    def stock_fridge(self, start_date: datetime, label:str):
        """
        For demo purposes.
        When the program starts, this method can be used to stock the fridge 
        with items that were already in the fridge. Items will be assigned a label and a 
        start date.
        """
        self.is_in_fridge = True
        self.label = label
        self.previous_label = label
        self.start_date = start_date
        self.previous_start_date = start_date
        self.start_time = timer()

    def add_to_fridge(self, start_date: datetime) -> None:
        """
        When a tag is detected in the fridge, add it.
        """
        self.is_in_fridge = True
        self.start_date = start_date
        self.start_time = timer()
        self.unlabel()

    def remove_from_fridge(self) -> None:
        self.previous_start_date = self.start_date
        self.is_in_fridge = False

    def label_contents(self, label:str) -> None:
        """
        Labels the contents of a tag
        """
        self.label = label

    def keep_as_last(self):
        """
        Keeps the contents of the tag the same as the last time
        the tag as in the fridge. Also preserves the start date
        from the previous fridge visit.
        """
        self.label = self.previous_label
        self.start_date = self.previous_start_date

    def unlabel(self):
        self.previous_label = self.label
        self.label = None

    def is_labeled(self):
        return self.label is not None

    def get_icon(self):
        """
        Returns the icon for the tag
        if the icon hasn't already been read from the filepath,
        then it will be read
        """
        if self.icon is None:
            self.icon = PhotoImage(file=self.icon_path)
        return self.icon

    def get_days_in_fridge(self):
        """
        Simulated days
        """
        today = simulate_today()
        return (today - self.start_date).days

    def get_previous_days_in_fridge(self):
        """
        Simulated days that the previous contents spent in the fridge
        """
        today = simulate_today()
        return (today - self.previous_start_date).days

    def get_seconds_in_fridge(self):
        """
        Actual seconds
        """
        return timer() - self.start_time 

class DoorButton:
    """
    A class for tracking the state of the fridge door (open/closed)
    """
    def __init__(self, ui, mon):
        self.ui = ui
        self.mon = mon
        self.run = True
        self.position = 0
        self.positions = [0,0]

    def start(self):
        """
        Spawn a new thread that keeps track of the position of the door (open/closed).
        Triggers the scanning method when the door closes, updates the UI accordingly. 
        """
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

                door_opened = (self.positions[0] == 1 and self.positions[1] == 0)
                door_closed = (self.positions[0] == 0 and self.positions[1] == 1)

                # Reverse door_opened/door_closed when not on Raspberry Pi
                # This makes for a better demo on PC
                if OS != 'Linux':
                    door_closed, door_opened = door_opened, door_closed

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
        """
        A clean-up function to stop the thread
        """
        self.run = False