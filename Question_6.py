from Tkinter import *
import Tkinter as ttk
from ttk import *


#READS JSON FILE INTO DATA LIST VARIABLE AND RETURNS
def readJson():
    import json
    with open('ca.json') as json_file:
        data = json.load(json_file)
        return data

data = readJson()

#CHANGES GUI TEXT FIELDS TO REPRESENT CITY DATA FROM DATA JSON VARIABLE
def onChoice(index, value, op):
    if latBox.get("1.0", END):
        countyBox.delete("1.0", END)
        latBox.delete("1.0", END)
        longBox.delete("1.0", END)

    city = str(popupMenu.get())

    for entry in data:
        if city in entry["name"] and "County" not in entry["name"]:
            county = entry['county_name']
            countyBox.insert(END, county)
            latitude = entry['primary_latitude']
            latBox.insert(END, latitude)
            longitude = entry['primary_longitude']
            longBox.insert(END, longitude)

#CREATES LIST OF CITIES FROM DATA LIST SORTED BY NAME, FILTERING COUNTIES
cities = []
for entry in data:
    if "County" not in entry["name"]:
        cities.append(entry['name'])

cities = sorted(cities)


#CREATES GUI WINDOW
base = Tk()
base.title("City Information")

tkvar = StringVar(base)
mainWindow = Frame(base)

#CREATES GRID TO PIN GUI WIDGETS TO
mainWindow = Frame(base)
mainWindow.grid(column=0,row=0, sticky=(N,W,E,S))
mainWindow.columnconfigure(0, weight = 1)
mainWindow.rowconfigure(0, weight = 1)
mainWindow.pack(pady = 100, padx = 100)

#CITY SELECTION DROP DOWN WIDGET
Label(mainWindow, text="Choose a city").grid(row = 0, column = 0)
popupMenu = Combobox(mainWindow, textvariable = tkvar, width = 24)
popupMenu['values'] = cities
popupMenu.grid(row = 0, column =1, pady = 10)

C#COUNTY INFORMATION WIDGET
Label(mainWindow, text="County").grid(row = 1, column = 0)
countyBox = Text(mainWindow, height = 1, width = 20)
countyBox.grid(row = 1, column = 1, pady = 10)

#lATITUDE INFORMATION WIDGET
Label(mainWindow, text="Latitude").grid(row = 2, column = 0)
latBox = Text(mainWindow, height = 1, width = 20)
latBox.grid(row = 2, column = 1, pady = 10)

#LONGITUDE INFORMATION WIDGET
Label(mainWindow, text="Longitude").grid(row = 3, column = 0)
longBox = Text(mainWindow, height = 1, width = 20)
longBox.grid(row = 3, column = 1, pady = 10)

#LISTENER FOR EVENT WHERE CITY IS SELECTED
tkvar.trace('w', onChoice)

mainWindow.mainloop()
