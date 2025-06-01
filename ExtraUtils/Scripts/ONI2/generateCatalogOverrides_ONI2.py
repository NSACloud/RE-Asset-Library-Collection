#Author: NSA Cloud
#Script to modify catalog file to set categories and names automatically

#This is game specific so changes will need to be made for other games
import os
import json
CATALOG_PATH = r"J:\REAssetLibrary\ONI2\REAssetCatalog_ONI2.tsv"
CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\ONI2\REAssetCatalog_ONI2_new.tsv"



AUTOMATIC_CATEGORY_LIST = [
	("Weapons",r"Character/weapon"),
	("Objects",r"Character/object"),
	("Characters/Player",r"Character/player"),
	("Characters/Enemy",r"Character/enemy"),
	("Characters/Other",r"Character/sub"),
	]


#-------------

AUTOMATIC_CATEGORY_LIST.sort(key = lambda item: len(item[1]))#Sort so largest strings are first
AUTOMATIC_CATEGORY_LIST.reverse()

with open(CATALOG_PATH,"r") as file:
    lines = file.readlines()


with open(CATALOG_PATH_OUTPUT,"w") as outputFile:
	outputFile.write("File Path\tDisplay Name\tCategory (Forward Slash Separated)\tTags (Comma Separated)\tPlatform Extension\tLanguage Extension\n")#Write header line
	for line in lines[1:]:

		if len(line.strip()) != 0:
			filePath,name,category,tags,platformExtension,langExtension = line.split("\t")
			
			#Category detection
			for categoryTuple in AUTOMATIC_CATEGORY_LIST:
				if categoryTuple[1].lower() in filePath.lower():
					category = categoryTuple[0]
					break
			
			splitext = os.path.splitext(os.path.split(filePath)[1])
			fileName = splitext[0]
			fileExtension = splitext[1]
			
			#
			#Name Overrides
			#TODO
			#print(filePath)
			outputFile.write(f"{filePath}\t{name}\t{category}\t{tags}\t{platformExtension}\t{langExtension}")
print("Done")
print("Generated new catalog. Rename after verifying if it is correct.")