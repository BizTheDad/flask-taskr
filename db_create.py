import sqlite3
import os
from _config import DATABASE_FOLDER
from _config import DATABASE_PATH

try:
    os.mkdir(DATABASE_FOLDER)
except FileExistsError:
    pass

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute("""
              CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name TEXT NOT NULL,
                                 due_date TEXT NOT NULL,
                                 priority INTEGER NOT NULL,
                                 status INTEGER NOT NULL)
              """)
    c.execute("""
              INSERT INTO tasks(name, due_date, priority, status)
              VALUES('Finish this tutorial', '5/19/18', 10, 1)
              """)
    c.execute("""
              INSERT INTO tasks(name, due_date, priority, status)
              VALUES('Finish Real Python Course 2', '6/1/18', 10, 1)
              """)
