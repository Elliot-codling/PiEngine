# Secondary storage process file
# Handles accessing secondary storage to load images or save data
import csv, pygame
from ..log.Logger import *
from typing import Union

# Load python image
def loadImage(path: str) -> pygame.Surface | None:
    # Try loading the image using a relative path
    try:
        image = pygame.image.load(f"{directoryPath()}/{path}")
        return image
    except FileNotFoundError:
        pass
    # Else try the absolute path
    try:
        image = pygame.image.load(path)
        return image
    except FileNotFoundError:
        # Else return None if texture could not load
        Logger.warn("storage/SSP", f"Could not load file: {path}. Unable to locate file")
        return None
    

# Find current path file the program is located in
def directoryPath() -> str:
    import os
    return os.getcwd()

# Finds if a file currently exists
def findFile(name: str) -> bool:
    import os
    return os.path.isfile(name)

# Returns a list of items containing each line in that file
def readFile() -> dict:
    dictionary = {}
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dictionary.update({row[0]:row[1]})

    return dictionary

# Writes data using a dictionary to a file called "data.csv"
def writeFile(dictionary: dict) -> None:
    with open("data.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        for item in dictionary:
            writer.writerow([item, dictionary.get(item)])

# Creates a csv file called "data.csv"
def createFile() -> None:
    with open("data.csv", "w") as csvfile:
        pass

# Create a key in a csv file with a name and its data value
def setVariable(name: str, data: str) -> None:
    if not findFile("data.csv"):
        createFile()
    
    dictionary = readFile()
    dictionary.update({name: data})
    writeFile(dictionary)
    
# Gets the value of a key
def getVariable(name: str) -> Union[str, None]:
    if not findFile("data.csv"):
        return None
    dictionary = readFile()
    return dictionary.get(name)

# Deletes all keys in the csv file
def deleteAll() -> None:
    createFile()

# Deletes a specific key in the csv file
def deleteKey(name: str) -> None:
    if not findFile("data.csv"):
        return None
    dictionary = readFile()
    if dictionary.get(name) == None:
        return None
    
    dictionary.pop(name)
    writeFile(dictionary)

# Returns a boolean if a key exists
def hasKey(name: str) -> bool:
    if not findFile("data.csv"):
        return False
    dictionary = readFile()
    if name in dictionary:
        return True
    else:
        return False

# Returns a list of all current keys   
def getKeys() -> Union[None, list]:
    if not findFile("data.csv"):
        return None
    dictionary = readFile()
    return list(dictionary.keys())