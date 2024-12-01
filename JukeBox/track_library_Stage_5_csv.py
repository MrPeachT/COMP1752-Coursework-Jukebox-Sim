from library_item_Stage_5_csv import LibraryItem
import csv
import os

library = {}
library["01"] = LibraryItem("Another Brick in the Wall", "Pink Floyd", 4)
library["02"] = LibraryItem("Stayin' Alive", "Bee Gees", 5)
library["03"] = LibraryItem("Highway to Hell ", "AC/DC", 2)
library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 1)
library["05"] = LibraryItem("Someone Like You", "Adele", 3)

def save_to_csv(file_path="library.csv"):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Artist", "Rating", "Play Count"])
        for key, item in library.items():
            writer.writerow([key, item.name, item.artist, item.rating, item.play_count])

def load_from_csv(file_path="library.csv"):
    if os.path.exists(file_path):
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = row["ID"]
                library[key] = LibraryItem(
                    name=row["Name"],
                    artist=row["Artist"],
                    rating=int(row["Rating"]),
                    play_count=int(row["Play Count"])
                )

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None

def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
        save_to_csv()
    except KeyError:
        return

def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
        save_to_csv()
    except KeyError:
        return
