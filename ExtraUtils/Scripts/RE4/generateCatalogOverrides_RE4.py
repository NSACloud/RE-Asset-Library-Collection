#Author: NSA Cloud
#Script to modify catalog file to set categories and names automatically

#This is game specific so changes will need to be made for other games
import os
import json
CATALOG_PATH = r"J:\REAssetLibrary\RE4\REAssetCatalog_RE4.tsv"
CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\RE4\REAssetCatalog_RE4_new.tsv"

ITEM_DUMP = os.path.join(os.path.dirname(__file__),"RE4ItemIDDump.json")

with open(ITEM_DUMP,"r", encoding ="utf-8") as file:
	itemInfo = json.load(file)
	
AUTOMATIC_CATEGORY_LIST = [
	("Items/Healing Items",r"Environment\sm\sm7X\sm71"),
	("Items/Ammo",r"Environment\sm\sm7X\sm70"),
	("Items/Crafting Items",r"Environment\sm\sm7X\sm73"),
	("Items/Key Items",r"Environment\sm\sm7X\sm74"),
	("Items/Treasure/Single",r"Environment\sm\sm7X\sm75"),
	("Items/Treasure/Combinable",r"Environment\sm\sm7X\sm76"),
	("Items/Unlocks",r"Environment\sm\sm7X\sm77"),
	
	("Weapons/Other",r"Character\wp"),
	("Weapons/Pistols",r"Character\wp\wp40"),
	("Weapons/DLC",r"Character\wp\wp60"),
	("Weapons/Shotguns",r"Character\wp\wp41"),
	("Weapons/SMGs",r"Character\wp\wp42"),
	("Weapons/Rifles",r"Character\wp\wp44"),
	("Weapons/Magnums",r"Character\wp\wp45"),
	("Weapons/Special",r"Character\wp\wp46"),
	("Weapons/Special",r"Character\wp\wp47"),
	("Weapons/Special",r"Character\wp\wp48"),
	("Weapons/Special",r"Character\wp\wp49"),
	("Weapons/Knives",r"Character\wp\wp50"),
	("Weapons/Throwables",r"Character\wp\wp54"),
	("Weapons/Attachments",r"Environment\sm\sm7X\sm72"),
	("Weapons/SW DLC",r"Character\wp\wp61"),
	("Weapons/Enemy",r"Character\wp\wp08"),
	("Weapons/Enemy",r"Character\wp\wp53"),
	("Weapons/Enemy",r"Character\wp\wp58"),
	("Weapons/Enemy",r"Character\wp\wp64"),
	
	("Characters/Other",r"Character\ch"),
	("Characters/Leon",r"Character\ch\cha0"),
	("Characters/Ashley",r"Character\ch\cha1"),
	("Characters/Ada",r"Character\ch\cha2"),
	("Characters/Luis",r"Character\ch\cha3"),
	("Characters/Wesker",r"Character\ch\cha6"),
	("Characters/Merchant",r"Character\ch\cha7"),
	("Characters/Ada",r"Character\ch\cha8"),
	("Characters/Police",r"Character\ch\chb0"),
	("Characters/Police",r"Character\ch\chb1"),
	("Characters/Hunnigan",r"Character\ch\chb2"),
	("Characters/Verdugo",r"Character\ch\chb3"),
	("Characters/Verdugo",r"Character\ch\chb4"),
	("Characters/Mendez",r"Character\ch\chb5"),
	("Characters/Salazar",r"Character\ch\chb6"),
	("Characters/Krauser",r"Character\ch\chb7"),
	("Characters/Sadler",r"Character\ch\chb8"),
	("Characters/Mike",r"Character\ch\chb9"),
	("Characters/Mike",r"Character\ch\chba"),
	
	#Merc
	
	("Characters/Luis",r"Character\ch\chi1"),
	("Characters/Krauser",r"Character\ch\chi2"),
	("Characters/Hunk",r"Character\ch\chi3"),
	("Characters/Wesker",r"Character\ch\chj0"),
	
	("Accessories",r"Character\ac\ac"),
	
	("Props",r"Environment\sm"),
	("Stage Models",r"Environment\st"),
	]


#-------------

AUTOMATIC_CATEGORY_LIST.sort(key = lambda item: len(item[1]))#Sort so largest strings are first
AUTOMATIC_CATEGORY_LIST.reverse()

with open(CATALOG_PATH,"r") as file:
    lines = file.readlines()


meshItemInfoDict = {os.path.split(itemInfo[x]["Mesh Path"].lower())[1].split(".mesh")[0]:itemInfo[x]["Item Name"] for x in itemInfo}

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
			
			#
			#Name Overrides
			#TODO
			#print(filePath)
			outputFile.write(f"{filePath}\t{name}\t{category}\t{tags}\t{platformExtension}\t{langExtension}")
print("Done")
print("Generated new catalog. Rename after verifying if it is correct.")