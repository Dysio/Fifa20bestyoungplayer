import tkinter as tk
import sqlite3


main_window = tk.Tk()
main_window.title('Fifa 20 Best Young Players')
main_window.geometry("800x800")


def print_results(result):
    if result_frame.children:
        dict_help = result_frame.children
        print(result_frame.winfo_children())
        # print(result_frame.children)
        # result_frame.children['zzz'] = 'test'
        # print(dict_help)
        for child in result_frame.winfo_children():
            # result_frame.children[child].destroy()
            child.destroy()

    for index, element in enumerate(result):

        col = 0
        for item in element:
            row_result = tk.Label(result_frame, text=item)
            row_result.grid(row=index + 2, column=col)
            col += 1


def name_search():
    name_to_search = name_box.get()
    if name_to_search != "":
        sql_cmd = f"NAME LIKE '%{name_to_search}%'"
    else:
        sql_cmd = ""

    return sql_cmd


def position_check():
    sql_cmd = ""
    num_of_checks = 0
    for key, item in check_buttons.items():
        if item["var"].get() != 0:
            num_of_checks += 1
            if num_of_checks < 2:
                sql_cmd += f"POSITION LIKE {item['search']}"
            else:
                sql_cmd += f" OR POSITION LIKE {item['search']}"
    return sql_cmd


def order_by():
    order_by = order_clicked.get()
    if order_by == order_options[0]:
        order_by_sql_cmd = ""
    elif order_by == order_options[1]:
        order_by_sql_cmd = "ORDER BY AGE"
    else:
        order_by_sql_cmd = "ORDER BY VALUE"

    return order_by_sql_cmd


def search_func():
    sql_cmd = "SELECT * FROM young_players_fifa20"
    name_sql_cmd = name_search()
    pos_sql_cmd = position_check()
    order_by_sql_cmd = order_by()

    if name_sql_cmd != "":
        sql_cmd += f" WHERE {name_sql_cmd}"
        if pos_sql_cmd != "":
            sql_cmd += f" AND ({pos_sql_cmd})"
    else:
        if pos_sql_cmd != "":
            sql_cmd += f" WHERE ({pos_sql_cmd})"

    if order_by_sql_cmd != "":
        sql_cmd += f" {order_by_sql_cmd} {order_type.get()}"

    print(sql_cmd)

    result = cursor.execute(sql_cmd)
    result = cursor.fetchall()

    return print_results(result)


db = sqlite3.connect('fifa20youngplayers.db')
cursor = db.cursor()

name_label = tk.Label(main_window, text="name:")
name_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
name_box = tk.Entry(main_window, font=("Helvetica", 15))
name_box.grid(row=0, column=1, columnspan=3)

col = 4
position_label = tk.Label(main_window, text="Position: ")
position_label.grid(row=0, column=col)

check_buttons = {
    "GK": {"box": "gk_check_box", "var": "gk_check_var", "search": "'%GK%'"},
    "DEF": {"box": "defender_check_box", "var": "defender_check_var", "search": "'%B%'"},
    "MID": {"box": "midfielder_check_box", "var": "midfielder_check_var", "search": "'%M%' OR POSITION LIKE '%W%'"},
    "F": {"box": "forward_check_box", "var": "forward_check_var", "search": "'%F%' OR POSITION LIKE '%ST%'"}
}

col += 1
for key, item in check_buttons.items():
    print(f"{item['box']} -- {item['var']}")
    item["var"] = tk.IntVar()
    item["box"] = tk.Checkbutton(main_window, text=key, variable=item["var"])
    print(f"item['var']= {item['var']}")
    item["box"].grid(row=0, column=col)
    col += 1

order_by_label = tk.Label(main_window, text="Order By: ")
order_by_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

order_options = ["-", "age", "value"]
order_clicked = tk.StringVar()
order_clicked.set(order_options[0])

order_drop = tk.OptionMenu(main_window, order_clicked, *order_options)
order_drop.grid(row=1, column=1)

order_type = tk.StringVar()
order_type.set("ASC")
order_asc_radio = tk.Radiobutton(main_window, text="ASC", variable=order_type, value="ASC")
order_asc_radio.grid(row=1, column=2)

order_desc_radio = tk.Radiobutton(main_window, text="DESC", variable=order_type, value="DESC")
order_desc_radio.grid(row=1, column=3)

result_frame = tk.Frame(main_window)
result_frame.grid(row=2, column=0, columnspan=8)

# position_check_button = tk.Button(main_window, text="Search", command=position_check)
position_check_button = tk.Button(main_window, text="Search", command=search_func)
position_check_button.grid(row=0, column=col)

main_window.mainloop()
