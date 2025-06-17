# Secondary storage process file
# Handles accessing secondary storage to load images or save data
import os, csv

# Load python image
def loadImage(file):
    import pygame
    return pygame.image.load(file)

# Find current path file the program is located in
def findCurrentPath():
    return os.getcwd()

# Finds if a file currently exists
def findFile(name):
    return os.path.isfile(name)

# Returns a list of items containing each line in that file
def readFile():
    dictionary = {}
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dictionary.update({row[0]:row[1]})

    return dictionary

# Writes data using a dictionary to a file called "data.csv"
def writeFile(dictionary):
    with open("data.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        for item in dictionary:
            writer.writerow([item, dictionary.get(item)])

# Creates a csv file called "data.csv"
def createFile():
    with open("data.csv", "w") as csvfile:
        pass

# Create a key in a csv file with a name and its data value
def setVariable(name, data):
    if not findFile("data.csv"):
        createFile()
    
    dictionary = readFile()
    dictionary.update({name: data})
    writeFile(dictionary)
    
# Gets the value of a key
def getVariable(name):
    if not findFile("data.csv"):
        return None
    dictionary = readFile()
    return dictionary.get(name)

# Deletes all keys in the csv file
def deleteAll():
    createFile()

# Deletes a specific key in the csv file
def deleteKey(name):
    if not findFile("data.csv"):
        return None
    dictionary = readFile()
    if dictionary.get(name) == None:
        return None
    
    dictionary.pop(name)
    writeFile(dictionary)

# Returns a boolean if a key exists
def hasKey(name):
    if not findFile("data.csv"):
        return None
    dictionary = readFile()
    if name in dictionary:
        return True
    else:
        return False

# Returns a list of all current keys   
def getKeys():
    if not findFile("data.csv"):
        return None
    dictionary = readFile()
    return list(dictionary.keys())