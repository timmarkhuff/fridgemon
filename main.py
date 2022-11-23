from tkinter import Tk, Frame, Label, Button, LEFT, RIGHT
from classes import FridgeMon, Tag, DoorButton

BG = "#FEF9EF"
TEXT_COLOR = '#73665C'
master = Tk()
master.configure(bg=BG)
title = 'FridgeMon'
master.title(title)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
master.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

# define some frames and labels
title_frame = Frame(master, padx=10, bg=BG)
title_label = Label(title_frame, text='FridgeMon', font=('Inter', 30, 'bold'), bg=BG, fg=TEXT_COLOR)
status_label = Label(title_frame, text='Door Closed', fg = "#84BD93", font=('Inter', 20), padx=10, bg=BG)
text = 'Reduce waste and take control of your fridge!'
tagline_label = Label(title_frame, text=text, font=('Inter', 12), bg=BG, fg=TEXT_COLOR)
item_frame = Frame(master, padx=10, bg=BG)

# grid the frames and labels
title_frame.grid(row=0, column=0, sticky='w')
title_label.grid(row=0, column=0, sticky='w')
status_label.grid(row=0, column=1, sticky='w')
tagline_label.grid(row=1, column=0, sticky='w')
item_frame.grid(row=1, column=0, sticky='w')

def refresh_item_buttons(item_frame: Frame, mon: FridgeMon):
    # clear the current contents of the frame
    for button in item_frame.winfo_children():
        button.destroy()

    # re-grid the buttons 
    tags_in_fridge = [tag for tag in mon.tags.values() if tag.is_in_fridge]
    if not tags_in_fridge:
        text='No items found in fridge.'
        empty_label = Label(item_frame, text=text, font=('Inter', 15), padx=20, bg=BG, fg=TEXT_COLOR)
        empty_label.grid(row=0, column=0)

    tags_in_fridge.sort(key=lambda tag: tag.start_date, reverse=False)
    row = 0
    column = 0
    for tag in tags_in_fridge:
        days_in_fridge = tag.get_days_in_fridge()

        # string representation of days_in_fridge
        if days_in_fridge == 1:
            days_in_fridge_str = f'1 day'
        else:
            days_in_fridge_str = f'{days_in_fridge} days'

        # color for the text
        if days_in_fridge < 4:
            foreground='#514e4e'
        else:
            foreground='#dc1f1f'

        # the tag label is none, show "???"
        if tag.label is None:
            label = '???'
        else:
            label = tag.label

        button = Button(item_frame, 
                        image=tag.get_icon(), 
                        text=f'{days_in_fridge_str}\n{label}',
                        background=tag.color,
                        foreground=foreground,
                        font=('Inter', 15, 'bold'),
                        compound=RIGHT,
                        padx=10,
                        pady=10,
                        width=232,
                        anchor ='w',
                        justify=LEFT,
                        )
        button.grid(column=column, row=row)
        
        # update column and row count
        if column >= 2:
            column = 0
            row += 1
        else:
            column += 1

def print_removed_items(removed, added):
    for i in removed:
        print(f'{i.label} removed!')
    for i in added:
        print(f'{i.name} added!')

mon = FridgeMon()
cbk_funcs = (
    (mon.scan_contents_simulated, None),
    (print_removed_items, None),
    (refresh_item_buttons, (item_frame, mon)),
)
door_button = DoorButton(status_label, cbk_funcs)
door_button.start()

# initialize the screen
refresh_item_buttons(item_frame, mon)

master.mainloop()

# clean up
door_button.stop()

