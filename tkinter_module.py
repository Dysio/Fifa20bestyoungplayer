import tkinter as tk
import sqlite3

main_window = tk.Tk()
main_window.title('Fifa 20 Best Young Players')
main_window.geometry("800x800")

def print_results(result):
    for index, element in enumerate(result):
        col = 0
        for item in element:
            row_result = tk.Label(main_window, text=item)
            row_result.grid(row=index+1, column=col)
            col += 1

def search_position():
    myLabel = tk.Label(main_window, text=clicked.get())
    myLabel.grid(row=1,column=0)
    # sql = "SELECT * FROM young_players_fifa20 WHERE POSITION LIKE %s"
    if clicked.get() == positions_options[0]:
        pos = "'GK'"
    elif clicked.get() == positions_options[1]:
        pos = "'%B%'"
    elif clicked.get() == positions_options[2]:
        pos = "'%M%'"
    else:
        pos = "'%F%'"

    position = (pos,)
    sql = f"SELECT * FROM young_players_fifa20 WHERE POSITION LIKE {pos}"
    result = cursor.execute(sql)
    result = cursor.fetchall()

    return print_results(result)


db = sqlite3.connect('fifa20youngplayers.db')
cursor = db.cursor()

positions_options = (
    "GK",
    "Defender",
    "Midfielder",
    "Forward"
)

clicked = tk.StringVar()
clicked.set(positions_options[0])
position_choose_drop = tk.OptionMenu(main_window, clicked, *positions_options)
position_choose_drop.grid(row=0, column=0, padx= 10, pady=10)

check_buttons = {
    "GK":{"box":"gk_check_box","var":"gk_check_var"},
    "DEF":{"box":"defender_check_box","var":"defender_check_var"},
    "MID":{"box":"midfielder_check_box","var":"midfielder_check_var"},
    "F":{"box":"forward_check_box","var":"forward_check_var"}
}

col = 2
for key, item in check_buttons.items():
    print(f"{item['box']} -- {item['var']}")
    item["var"] = tk.IntVar()
    item["box"] = tk.Checkbutton(main_window, text=key, variable=item["var"])
    item["box"].grid(row=0, column=col)
    col += 1

# gk_check_var = tk.IntVar()
# gk_check_box = tk.Checkbutton(main_window, text="GK", variable=gk_check_var)
# gk_check_box.grid(row=0, column=2)
# test_label = tk.Label(main_window, text=check_buttons["GK"]["var"].get())
# test_label.grid(row=1, column=3)

def position_check():
    positions_label = tk.Label(main_window)
    positions_label.destroy()
    pos_text = ""
    for key, item in check_buttons.items():
        if item["var"].get() != 0:
            pos_text += key + "+"
    positions_label = tk.Label(main_window, text = pos_text)
    positions_label.grid(row=2, column=1)

position_check_button = tk.Button(main_window, text="Show choosen Positions", command=position_check)
position_check_button.grid(row=1, column=1)

search_button = tk.Button(main_window, text="Search...", command=search_position)
search_button.grid(row=0, column=1)


# for index, element in enumerate(result):
#     col = 0
#     for item in element:
#         row_result = tk.Label(main_window, text=item)
#         row_result.grid(row=index+1, column=col)
#         col += 1

main_window.mainloop()