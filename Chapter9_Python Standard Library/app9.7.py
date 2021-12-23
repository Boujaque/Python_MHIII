# 7 - Working with JSON Files
import json
from pathlib import Path
movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarden Cop", "year": 1993},
    {"id": 3, "title": "Trainspoting", "year": 1990}
]

data = json.dumps(movies)
print("original data: ", data)

# write to a Json file
# Path("movies.json").write_text(data)

# read from a Json file
data_read = Path("movies.json").read_text()
movies_read = json.loads(data_read)
print("data read:", movies_read)
# get an item from array
print(movies[0])
print(movies[0]["title"])
