#Creates list of CompoMaps for as many components measured on a laser map
#Includes method for converting LA-ICPMS csv data into a numeric matrix
import numpy as np
import pandas as pd
import csv
from CompoMap import CompoMap
UNIT_ROW = 4
FIRST_ELEM_COL = 5 
X_HEAD = "x (um)"
Y_HEAD = "y (um)"
class LaserMaps:

	def __init__(self, csvIn):
		#Consturctor that takes csv file and concerts it to a series of CompoMaps

		#First read the csv file to get the units and read the rest as a pandas dataframe
		try:
			csvFile = open(csvIn, 'r')
		except:
			print("File not found")
			exit(0)
		headRead = [row for row in csv.reader(csvFile)]
		csvFile.seek(0)
		headerRow = UNIT_ROW+1
		#print(headRead)
		laserdf = pd.read_csv(csvFile, header = headerRow, index_col = 0)
		
		#headRead = list(headRead)
		csvFile.close()
		units = []

		for i in range(len(headRead[0])):
			if i >= FIRST_ELEM_COL:
				units.append(headRead[UNIT_ROW][i])
		

		#Now it is time to convert the pandas dataframe to a 2D numpy array for each component
		x_col = laserdf[X_HEAD]
		y_col = laserdf[Y_HEAD]
	
		compositions = laserdf.iloc[:,FIRST_ELEM_COL-1:]

		self.spotSize = x_col.iloc[1]-x_col.iloc[0]
		
		self.compoMaps = []
		colCount = 0

		compoCols = list(compositions)#Get the headers

		#iterate through each column to make an array of each component
		for i in range(len(compoCols)):
			
			thisMap = []
			thisRow = []
			currY = y_col.iloc[0]
			#print(currY)
			for j in range(len(y_col)):

				#print(y_col.iloc[j])
				if y_col.iloc[j] != currY: #Check if next pixel row
					#Add this row to map and make a new one
					thisMap.append(thisRow)
					thisRow =[]
					currY = y_col.iloc[j]
				
				thisRow.append(compositions.iloc[j,i])

			mapNp = np.asarray(thisMap)
			
			componentSplit = compoCols[i].strip(')').split('(')#Remove trailing bracket and split at the left bracket, isolate isotope and component
			#This is for reading into XMapTools
			checkOxide = compoCols[i].split('O') #Value to check if the component is an oxide by splitting at 'O'

			if len(checkOxide)>1 or len(componentSplit) <2:#Check if oxide or 'TIC'
				component = componentSplit[0]
			else:
				component = componentSplit[1] + componentSplit[0]



			thisCompoMap = CompoMap(self.spotSize,units[i],mapNp,component)
			self.compoMaps.append(thisCompoMap)

	def saveMaps(self, folderIn):
		#Method for saving all elements in self.compoMaps to a txt file
		for elem in self.compoMaps:
			elem.saveMap(folderIn)
			
