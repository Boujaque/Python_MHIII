# 8 - Working with SQL lite Database
import sqlite3
import json
from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

# if we run will have an error because is messing the Table movies from database
# download the DB Browser for SQLite

# Reading data from Database
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor: # will return a tuple for each row
    #     print(row)
    movies = cursor.fetchall()  # return the table as list of tuples
    print(movies)
