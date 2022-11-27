from tkinter import Tk, Frame, Label, Button, LEFT, RIGHT
from logic import FridgeMon, DoorButton, FOOD_LABELS
from threading import Thread
from time import sleep

BG = "#FEF9EF"
TEXT_COLOR = '#73665C'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
REFRESH_TIME = 60 # seconds

class UI:
    def __init__(self, mon: FridgeMon):
        self.mon = mon
        self.master = Tk()
        title = 'FridgeMon'
        self.master.title(title)
        self.master.configure(bg=BG)
        self.master.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.run = True

        # timer-related attributes
        self.time_since_refresh = 0
        self.start_timer()

        # create the initial display
        self.start_item_screen()

    def start_item_screen(self):
        # define some frames and labels
        self.main_frame = Frame(self.master, padx=10, bg=BG)
        self.title_frame = Frame(self.main_frame, padx=10, bg=BG)
        self.title_label = Label(self.title_frame, text='FridgeMon', font=('Inter', 30, 'bold'), bg=BG, fg=TEXT_COLOR)
        self.status_label = Label(self.title_frame, text='Door Closed', fg = "#84BD93", font=('Inter', 20), padx=10, bg=BG)
        text = 'Reduce waste and take control of your fridge!'
        self.tagline_label = Label(self.title_frame, text=text, font=('Inter', 12), bg=BG, fg=TEXT_COLOR)
        self.item_frame = Frame(self.main_frame, padx=10, bg=BG)

        # grid the frames and labels
        self.main_frame.grid(row=0, column=0, sticky='w')
        self.title_frame.grid(row=0, column=0, sticky='w')
        self.title_label.grid(row=0, column=0, sticky='w')
        self.status_label.grid(row=0, column=1, sticky='w')
        self.tagline_label.grid(row=1, column=0, sticky='w')
        self.item_frame.grid(row=1, column=0, sticky='w')

    def start_label_screen(self, tag):
        # clear the screen
        for i in self.main_frame.winfo_children():
            i.destroy()

        # create some labels
        self.main_frame = Frame(self.master, padx=10, bg=BG)
        text = f'Select a label for {tag.name}'
        self.icon_label = Label(self.main_frame, text=text)

        # grid the labels
        self.main_frame.grid(row=0, column = 0)
        self.icon_label.grid(row=0, column = 0)

        row = 1
        for label in FOOD_LABELS:
            button = Button(self.main_frame, 
                            text=label,
                            font=('Inter', 12),
                            background='#F5D3BB',
                            width=15,
                            command = lambda tag=tag, label=label: self.click_label_button(tag, label)
                            )
            button.grid(row=row, column=0, sticky='nsew')
            row += 1

    def refresh_item_buttons(self):
        # clear the current contents of the frame
        for button in self.item_frame.winfo_children():
            button.destroy()

        # sort the list of tags
        tags_in_fridge = [tag for tag in self.mon.tags.values() if tag.is_in_fridge]
        tags_in_fridge.sort(key=lambda tag: tag.start_date, reverse=False)
        # show unlabel,recently added items first
        show_first = [tag for tag in tags_in_fridge if tag.get_seconds_in_fridge() <= REFRESH_TIME and not tag.is_labeled]
        # next, show items that were not recently added to fridge and all labeled items
        show_next = [tag for tag in tags_in_fridge if tag.get_seconds_in_fridge() > REFRESH_TIME or tag.is_labeled]
        tags_in_fridge = show_first + show_next

        # add some default text if there are no tags
        if not tags_in_fridge:
            text='No items found in fridge.'
            empty_label = Label(self.item_frame, text=text, font=('Inter', 15), padx=20, bg=BG, fg=TEXT_COLOR)
            empty_label.grid(row=0, column=0)

        # re-grid the buttons 
        row = 0
        column = 0
        for tag in tags_in_fridge:
            days_in_fridge = tag.get_days_in_fridge()

            # the tag label is none, show "???"
            if tag.label is None:
                label = '???'
            else:
                label = tag.label

            # text for the button
            if tag in show_first:
                button_text = f'Just added\nLabel it!'
            elif days_in_fridge == 1:
                button_text = f'1 day\n{label}'
            else:
                button_text = f'{days_in_fridge} days\n{label}'

            # color for the text
            if days_in_fridge < 4:
                foreground='#514e4e'
            else:
                foreground='#dc1f1f'

            # background color of the button
            if tag in show_first:
                color = '#84BD93'
            else:
                color = '#F5D3BB'

            # create the food item button
            button = Button(self.item_frame, 
                            image=tag.get_icon(), 
                            text=button_text,
                            background=color,
                            foreground=foreground,
                            font=('Inter', 15, 'bold'),
                            compound=RIGHT,
                            padx=10,
                            pady=10,
                            width=232,
                            anchor ='w',
                            justify = LEFT,
                            command = lambda tag=tag: self.start_label_screen(tag)
                            )
            button.grid(column=column, row=row)

            # update column and row count
            if column >= 2:
                column = 0
                row += 1
            else:
                column += 1

    def click_label_button(self, tag, label:str):
        self.main_frame.destroy()
        tag.label_contents(label)
        self.start_item_screen()
        self.refresh_item_buttons()

    def start_timer(self):
        freq = .1 # seconds
        def thread():
            while self.run:
                sleep(freq)
                self.time_since_refresh += freq
                if self.time_since_refresh > REFRESH_TIME:
                    self.time_since_refresh = 0
                    self.refresh_item_buttons()
        Thread(target=thread).start()

    def mainloop(self):
        self.master.mainloop()

    def stop(self) -> None:
        self.run = False  

mon = FridgeMon()
ui = UI(mon)
door_button = DoorButton(ui, mon)

ui.refresh_item_buttons()
door_button.start()
ui.mainloop()

# clean up
ui.stop()
door_button.stop()

