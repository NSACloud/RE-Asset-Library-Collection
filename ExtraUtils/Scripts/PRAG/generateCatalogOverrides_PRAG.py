#Author: NSA Cloud
#Script to modify catalog file to set categories and names automatically

#This is game specific so changes will need to be made for other games
import os
import json
CATALOG_PATH = r"J:\REAssetLibrary\PRAG\REAssetCatalog_PRAG.tsv"
CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\PRAG\REAssetCatalog_PRAG_new.tsv"

AUTOMATIC_CATEGORY_LIST = [
	("Items",r"Item/Model"),
	
	
	("Characters/Other",r"Character/ch/"),
	("Characters/Hugh",r"Character/ch/ch00"),
	("Characters/Diana",r"Character/ch/ch01"),
	
	
	("Props",r"Environment/sm"),
	("Stage Models",r"Environment/st"),
	("VFX",r"VFX/"),
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
			"""
			if fileName.lower() in meshItemInfoDict:
				name = meshItemInfoDict[fileName.lower()]
				if fileExtension == ".chain2":
					name += " (Chain Physics)"
				elif fileExtension == ".mdf2":
					name += " (Material Data)"
				elif fileExtension == ".clsp":
					name += " (Collision Shape)"
				elif fileExtension == ".sfur":
					name += " (Shell Fur)"
				elif fileExtension == ".jcns":
					name += " (Joint Constraints)"
				elif fileExtension == ".fbxskel":
					name += " (Base Skeleton)"
			"""
			#
			#Name Overrides
			#TODO
			#print(filePath)
			outputFile.write(f"{filePath}\t{name}\t{category}\t{tags}\t{platformExtension}\t{langExtension}")
print("Done")
print("Generated new catalog. Rename after verifying if it is correct.")