# FIFA20 best young players 
### Description
This is a small program using webscraping to get informations from website https://www.goal.com/ about young, perspective players in FIFA20. The program get informations from html code of web and put it into table in database. Then you have ability to sort all the players by some options.
Sorting options:
- name - you can type some letters of footballers name. If they appear in passed order in the players name, after clicking search all of those players will be shown.
- position - here you can chceck the positions of players that you look for. Choice can be multiple.
- order by - you can choose by which parameter, age or value, players will be sorted. You also can choose if order will be ascending or descending.

Screen

![WindowView](/static/Window_View_01.png)

#### Technologies used
 - Python
 - sqlite3
 - Tkinter