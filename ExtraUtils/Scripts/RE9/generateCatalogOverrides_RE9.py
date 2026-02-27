
import os
import json
import csv

CATALOG_PATH = r"J:\REAssetLibrary\RE9\REAssetCatalog_RE9.tsv"

CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\RE9\REAssetCatalog_RE9.tsv"

AUTOMATIC_CATEGORY_LIST = [

	
	#(r"CATEGORY_NAME",r"directoryPath"),
	("Weapons",r"character/wp"),
	("Characters/Other",r"character/ch/"),
	("Characters/Leon",r"character/ch/ch01"),
	("Characters/Grace",r"character/ch/ch02"),
	
	
	("Props",r"environment/sm"),
	#("Props/Gimmicks",r"escape/setmodel/sm4x_gimmick"),
	#("Items",r"escape/setmodel/sm7x_item"),
	
	("Stage Models",r"environment/optimization"),
	("VFX",r"vfx/"),
	
	]


#-------------

AUTOMATIC_CATEGORY_LIST.sort(key = lambda item: len(item[1]))
AUTOMATIC_CATEGORY_LIST.reverse()

OVERRIDE_DIR = "Overrides"


overrideDict = dict()
if os.path.isdir(OVERRIDE_DIR):
	for entry in os.scandir(OVERRIDE_DIR):
		if entry.is_file() and entry.name.endswith(".tsv"):
			tsvPath = os.path.join(OVERRIDE_DIR,entry.name)
			with open(tsvPath,"r") as file:
				rd = csv.reader(file, delimiter="\t", quotechar='"')
				next(rd)#Skip header
				for row in rd:
					overrideDict[row[0]] = list(row)
				print(f"Loaded override file: {tsvPath}")
						

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
			
			
			
			#Name Overrides
			if filePath in overrideDict:
				override = overrideDict[filePath]
				name = override[1]
				category = override[2]
				tags = override[3]
			outputFile.write(f"{filePath}\t{name}\t{category}\t{tags}\t{platformExtension}\t{langExtension}")
print(f"Generated new catalog: {CATALOG_PATH_OUTPUT}")