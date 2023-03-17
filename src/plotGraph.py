import json
from readData import readData
from configAndPlotData import configAndPlotData

# input data
os = "windows"
fullFileName = ".\setup\calibration.json"

# read JSON file
file = open(fullFileName)
setup = json.load(file)
file.close()

# read data to plot
data = readData(setup, os)

# plot graph
configAndPlotData(setup, data, os)