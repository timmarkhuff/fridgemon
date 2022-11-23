from tkinter import PhotoImage
from datetime import date, timedelta
import random
from time import sleep
from threading import Thread

FOOD_LABELS = ['Steak', 'Cake', 'Salmon', 'Xiao Long Bao', 'Spaghetti',
            'Linguine', 'Bulgogi', 'Stew', 'Halibut', 'Burger', 'Gumbo',
            'Chow Mein', 'Pork Chop', 'Soup', 'Sushi', 'Chicken Parm',
            'Lasagna', 'Fajita', 'Tacos', 'Carne Asada', 'Fried Rice',
            'Pancakes', 'Rice Cakes']

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
                    today = date.today()
                    rand_time_delta = timedelta(days = random.randint(0,5))
                    start_date = today - rand_time_delta

                    tag.add_to_fridge(start_date, label)

    def scan_contents_simulated(self) -> tuple:
        removed = []
        added = []
        for tag in self.tags.values():
            if random.randint(0,1):
                if tag.is_in_fridge:
                    tag.remove_from_fridge()
                    removed.append(tag)
                else:
                    tag.add_to_fridge(date.today())
                    added.append(tag)
        return removed, added

class Tag:
    def __init__(self, fm, id: int, name: str, color: str, icon_path: str):
        self.fm: FridgeMon = fm
        self.id: int = id
        self.name: str = name
        self.color: str = color
        self.icon_path: str = icon_path
        self.icon: PhotoImage = None
        self.label: str = ''    
        self.is_in_fridge: bool = False

    def add_to_fridge(self, start_date: date, label: str = None) -> None:
        self.is_in_fridge = True
        self.label = label
        self.start_date = start_date

    def remove_from_fridge(self) -> None:
        self.is_in_fridge = False

    def label_contents(self, label:str) -> None:
        self.label: str = label

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
        today = date.today()
        return (today - self.start_date).days


class DoorButton:
    def __init__(self, status_label, cbk_funcs):
        self.status_label = status_label
        self.cbk_funcs = cbk_funcs
        self.run = True
        self.position = 0
        self.positions = [0,0]

    def start(self):
        def thread():
            x = 0
            while self.run:
                sleep(.1)
                if x == 0:
                    self.position = 0
                elif x % 50 == 0 or x % 60 == 0:
                    self.position = not self.position
                self.positions.append(self.position)
                self.positions = self.positions[1:]

                if self.positions[0] == 0 and self.positions[1] == 1:
                    print('-----------Door opened!-----------')
                    text = "Door Open"
                    fg = "#FF0000"
                    self.status_label.config(text=text, fg=fg)
                if self.positions[0] == 1 and self.positions[1] == 0:
                    text = "Door Closed"
                    fg = "#84BD93"
                    self.status_label.config(text=text, fg=fg)
                    print('-----------Door closed!-----------')
                    previous_output = None
                    for i in self.cbk_funcs:
                        func = i[0]
                        args = i[1]
                        if previous_output:
                            previous_output = func(*previous_output)
                        elif args:
                            previous_output = func(*args)
                        else:
                            previous_output = func()
                x += 1
        Thread(target=thread).start()

    def stop(self):
        self.run = False

