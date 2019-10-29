#Class for managing numeric matrix of map data from LA-ICPMS or microprobe
#Includes any methods for 
import numpy as np
import os
class CompoMap:

	def __init__(self):
		self.spotSize = 0 #assume spots are squares
		self.unit = Null
		self.component = Null

	def __init__(self,spotIn,unitIn,mapIn,componentIn):
		self.spotSize = spotIn
		self.unit = unitIn
		self.map = mapIn
		self.component = componentIn

	def saveMap(self, folderIn):
		#Method for saving this individual map in a specific folder
		#Will use the self.component as the name of the file
		if os.name == 'nt':#PC
			slash = "\\"
		else:#Mac
			slash= "/"

			
		fileName = folderIn + slash + self.component + ".txt"

		try:
			writeFile = open(fileName, 'w')
		except:
			print('Problem creating new file')
			exit(0)

		#save numpy array as a txt file delimited by spaces
		for row in self.map:
			writeRow = ''
			#Format each row
			for i in range(len(row)):
				writeRow += '%f '%row[i]
			writeRow.strip()
			writeRow += '\n'
			#Add row to file
			writeFile.write(writeRow)