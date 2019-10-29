#Program for converting map data from LA-ICPMS csv files provided by GSC into txt maps
#Importable to imageJ or XMapTools
import easygui
import numpy as np

from LaserMaps import LaserMaps

print('Choose the csv file for the laser maps')

#Choose the csv laser file to convert
mapIn = easygui.fileopenbox('Choose the csv file for the laser maps')
#mapIn ="/home/sabastien/Documents/Carleton/Laser Maps/SE17B19 - 18ZE-R-77A/SE17B19 - 18ZE-R-77A.csv"
if mapIn != None:
	mapIn = mapIn.strip()
	mapIn = mapIn.strip('"')
	print("Accessing " + mapIn)
	print("Reading file to memory...")
	myMaps = LaserMaps(mapIn)

	#Block for outputting files
	print("File read to memory, please choose directory to save. Note that it saves each file as a txt that will have the name of that component")
	mapOut = easygui.diropenbox("File read to memory, please choose directory to save. Note that it saves each file as a txt that will have the name of that component")
	
	#mapOut = "/home/sabastien/Documents/Carleton/Laser Maps/SE17B19 - 18ZE-R-77A/txt_files"
	if mapOut != None:

		mapOut = mapOut.strip()
		mapOut = mapOut.strip('"')
		myMaps.saveMaps(mapOut)
		print("Files saved, ending program")
	else:
		print("No directory chosen, quitting")
else:
	print("No file selected, quitting")