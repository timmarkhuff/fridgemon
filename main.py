from tkinter import Tk, Frame, Label, Button, LEFT, RIGHT, HORIZONTAL
from tkinter.ttk import Progressbar
from logic import FridgeMon, DoorButton, FOOD_LABELS
from threading import Thread
from time import sleep

# colors
RED = '#dc1f1f'
GREEN = '#84BD93'
BG = "#FEF9EF"
TEXT_COLOR = '#73665C'
BUTTON_BACKGROUND = '#F5D3BB'
TEXT_COLOR = '#514e4e'
LIGHT_BROWN = '#73665C'

# screen parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 420
REFRESH_TIME = 30 # seconds
ITEM_BUTTON_WIDTH = 228

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
        self.active_screen = 'items'

        # define some frames and labels
        self.main_frame = Frame(self.master, padx=10, bg=BG)
        self.title_frame = Frame(self.main_frame, padx=10, bg=BG)
        self.title_label = Label(self.title_frame, text='FridgeMon', font=('Inter', 30, 'bold'), bg=BG, fg=TEXT_COLOR)
        self.status_label = Label(self.title_frame, text='Door Closed', fg = "#84BD93", font=('Inter', 20), padx=10, bg=BG)
        text = 'Reduce waste and take control of your fridge!'
        self.tagline_label = Label(self.title_frame, text=text, font=('Inter', 12), bg=BG, fg=TEXT_COLOR)
        self.item_frame = Frame(self.main_frame, padx=10, bg=BG)

        # grid the frames and labels
        self.main_frame.grid(row=0, column=0, sticky='nw')
        self.title_frame.grid(row=0, column=0, sticky='nw')
        self.title_label.grid(row=0, column=0, sticky='nw')
        self.status_label.grid(row=0, column=1, sticky='nw')
        self.tagline_label.grid(row=1, column=0, sticky='nw')
        self.item_frame.grid(row=1, column=0, sticky='nw')

        self.refresh_item_buttons()

    def start_label_screen(self, tag):
        self.active_screen = 'label'
        self.progress_bar = None

        # clear the screen
        for i in self.main_frame.winfo_children():
            i.destroy()

        # create some frames and labels labels
        self.main_frame = Frame(self.master, padx=10, bg=BG)
        self.top_frame = Frame(self.main_frame, padx=10, bg=BG)
        self.bottom_frame = Frame(self.main_frame, bg=BG)
        self.left_bottom_frame = Frame(self.bottom_frame, bg=BG, padx=10, pady=10)
        self.right_bottom_frame = Frame(self.bottom_frame, padx=10, bg=BG)

        text = f'Label {tag.name}'
        font = ('Inter', 20, 'bold')
        self.label_page_heading = Label(self.top_frame, text=text, font=font, bg=BG, fg=TEXT_COLOR)

        self.icon_label = Label(self.left_bottom_frame, 
                                image=tag.get_icon(), 
                                width=ITEM_BUTTON_WIDTH,
                                bg=BG,
                                )

        self.keep_as_last_button = Button(self.left_bottom_frame,
                                    foreground=BG,
                                    activeforeground=BG,
                                    background=GREEN,
                                    activebackground=GREEN,
                                    command=lambda tag=tag: self.click_keep_as_last_button(tag),
                                    font=('Inter', 16),
                                    )     

        self.back_button = Button(self.left_bottom_frame,
                                    foreground=BG,
                                    activeforeground=BG,
                                    background=LIGHT_BROWN,
                                    activebackground=LIGHT_BROWN,
                                    text='Back',
                                    height=3,
                                    font=('Inter', 16),
                                    width=14,
                                    command=lambda self=self: self.return_to_item_screen(),
                                    ) 

        # grid the frames and labels
        self.main_frame.grid(row=0, column=0, sticky='nsew')
        self.top_frame.grid(row=0, column=0, sticky='nsew')
        self.bottom_frame.grid(row=1, column=0, sticky='nsew')
        self.left_bottom_frame.grid(row=0, column=0, sticky='nsew')
        self.right_bottom_frame.grid(row=0, column=1, sticky='nsew')
        self.label_page_heading.grid(row=0, column=0, sticky='nsew')
        self.icon_label.grid(row=0, column=0, sticky='nsew')
        self.back_button.place(x=0,y=264)

        # if the tag has been previously inserted
        if tag.previous_label is not None and tag.label is None:
            days_in_fridge = tag.get_previous_days_in_fridge()
            text = f'Keep as:\n{tag.previous_label}\n({days_in_fridge}'
            if days_in_fridge == 0 or days_in_fridge > 1:
                text += ' days)'
            else:
                text += ' day)'
            self.keep_as_last_button.config(text=text) 
            self.keep_as_last_button.grid(row=2, column=0, sticky='nsew')

        row = 0
        column = 0
        for label in FOOD_LABELS:
            button = Button(self.right_bottom_frame, 
                            text=label,
                            font=('Inter', 14),
                            background=BUTTON_BACKGROUND,
                            activebackground=BUTTON_BACKGROUND,
                            foreground=TEXT_COLOR,
                            activeforeground=TEXT_COLOR,
                            width=19,
                            height=2,
                            command = lambda tag=tag, label=label: self.click_label_button(tag, label)
                            )
            button.grid(row=row, column=column, sticky='nsew')
            if row == 5:
                row = 0
                column += 1
            else:
                row += 1

    def refresh_item_buttons(self):
        # check if the active screen is the items screen
        # if not, there is nothing to refresh, so do nothing
        if self.active_screen != 'items':
            return

        # clear the current contents of the frame
        for button in self.item_frame.winfo_children():
            button.destroy()

        # sort the list of tags
        tags_in_fridge = [tag for tag in self.mon.tags.values() if tag.is_in_fridge]
        tags_in_fridge.sort(key=lambda tag: tag.start_date, reverse=False)
        # show unlabel,recently added items first
        show_first = [tag for tag in tags_in_fridge if tag.get_seconds_in_fridge() <= REFRESH_TIME and not tag.is_labeled()]
        # next, show items that were not recently added to fridge and all labeled items
        show_next = [tag for tag in tags_in_fridge if tag.get_seconds_in_fridge() > REFRESH_TIME or tag.is_labeled()]
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
                foreground = TEXT_COLOR
            else:
                foreground = RED

            # background color of the button
            if tag in show_first:
                color = GREEN
            else:
                color = BUTTON_BACKGROUND

            # create the food item button
            button = Button(self.item_frame, 
                            image=tag.get_icon(), 
                            text=button_text,
                            background=color,
                            activebackground=color,
                            foreground=foreground,
                            activeforeground=foreground,
                            font=('Inter', 15, 'bold'),
                            compound=RIGHT,
                            padx=10,
                            pady=10,
                            width=ITEM_BUTTON_WIDTH,
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
        tag.label_contents(label)
        self.return_to_item_screen()  

    def click_keep_as_last_button(self, tag):
        tag.keep_as_last()
        self.return_to_item_screen() 

    def return_to_item_screen(self):
        self.main_frame.destroy()
        self.start_item_screen()

    def show_open(self):
        text = "Door Open"
        fg = RED
        self.status_label.config(text=text, fg=fg)
        
    def show_closed(self):
        if self.active_screen != 'items':
            return
        text = "Door Closed" 
        fg = GREEN
        self.status_label.config(text=text, fg=fg)

    def start_progress_bar(self):
        text = "Scanning" 
        fg = TEXT_COLOR
        self.status_label.config(text=text, fg=fg)

        self.progress_bar = Progressbar(self.title_frame, orient=HORIZONTAL, length=200, mode='indeterminate')
        self.progress_bar.grid(row=0, column=2, padx=10)
        self.progress_bar.start(2)

    def stop_progress_bar(self):
        if self.active_screen != 'items' or self.progress_bar is None:
            return
        self.progress_bar.grid_forget()

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

door_button.start()
ui.mainloop()

# clean up
ui.stop()
door_button.stop()