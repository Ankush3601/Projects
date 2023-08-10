import json
import sqlite3
from pathlib import Path

data = json.loads(Path("movies.json").read_text())
# print(movies)
with sqlite3.connect("dbsqlite3") as conn:
    command = "INSERT INTO data VALUES(?,?,?)"
    for movie in data:
        conn.execute(command, tuple(movie.values()))

    conn.commit()
