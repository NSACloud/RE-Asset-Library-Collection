#Author: NSA Cloud
#Script to modify catalog file to set categories and names automatically

#This is game specific so changes will need to be made for other games
import os
import json
CATALOG_PATH = r"J:\REAssetLibrary\SF6\REAssetCatalog_SF6.tsv"
CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\SF6\REAssetCatalog_SF6_new.tsv"

FIGHTER_DUMP = os.path.join(os.path.dirname(__file__),"fighterSeries.json")

with open(FIGHTER_DUMP,"r", encoding ="utf-8") as file:
	fighterInfo = json.load(file)
	
AUTOMATIC_CATEGORY_LIST = [
	("Characters/Fighters",r"Product/Model/esf"),
	("Characters/NPCs",r"Product/Model/npc"),
	("Characters/Avatar",r"Product/Model/wcs"),
	("Characters/Avatar/Head",r"Product/Model/wpl"),
	("Characters/Animals",r"Product/Model/mob"),
	("VFX",r"Product/VFX"),
	("Objects",r"Product/Model/gnp"),
	("Objects",r"Product/Model/atc"),
	("Objects",r"Product/MiniGame"),
	("Stage/Parts",r"Product/Environment/Stage/Resource/ess"),
	("Stage/Props",r"Product/Environment/Props/Resource"),
	("Stage/World Tour",r"Product/Environment/Stage/Resource/wtc"),
	
	
	
	
	]


#-------------

AUTOMATIC_CATEGORY_LIST.sort(key = lambda item: len(item[1]))#Sort so largest strings are first
AUTOMATIC_CATEGORY_LIST.reverse()

with open(CATALOG_PATH,"r") as file:
    lines = file.readlines()


partIDDict = {
	"00":"Head",
	"10":"Skeleton",
	"01":"Body",
	"02":"Hair",
	"20":"Hands",
	"30":"Accessory A",
	"31":"Accessory B",
	"32":"Accessory C",
	"33":"Accessory D",
	"34":"Accessory E",
	"35":"Accessory F",
	"36":"Accessory G",
	"40":"Accessory H",
	"41":"Accessory I",
	"CMD":"Costume Material Data",
	}


with open(CATALOG_PATH_OUTPUT,"w") as outputFile:
	outputFile.write("File Path\tDisplay Name\tCategory (Forward Slash Separated)\tTags (Comma Separated)\tPlatform Extension\tLanguage Extension\n")#Write header line
	for line in lines[1:]:

		if len(line.strip()) != 0:
			filePath,name,category,tags,platformExtension,langExtension = line.split("\t")
			
			#Category detection
			for categoryTuple in AUTOMATIC_CATEGORY_LIST:
				if categoryTuple[1] in filePath:
					category = categoryTuple[0]
					break
			
			splitext = os.path.splitext(os.path.split(filePath)[1])
			fileName = splitext[0]
			fileExtension = splitext[1]
			#Armor overrides
			excludeExtensionSet = set([
				".tex",
				])
			
			if fileExtension not in excludeExtensionSet:
				if filePath.startswith("Product/Model/esf") and fileName.startswith("esf"):
					if fileName.count("_") >= 2:
						#print(fileName)
						split = fileName.split("_")
						fighterID = split[0]
						costumeNum = split[1]
						partID = split[2]
						#print(filePath)
						partName = partIDDict.get(partID,"Unknown Part")
						if "_cmd_" in fileName.lower() and not "_cmd_dx" in fileName.lower() and not "_cmd_ex" in fileName.lower():
							splitIndex = 3 if fileName.count("_") == 3 else 4
							colorIDString = f"Color {int(split[splitIndex])}"
						else:
							colorIDString = ""
						name = f"{fighterInfo.get(fighterID,os.path.split(filePath)[1])} (C{int(costumeNum)}) {partName} {colorIDString}"
						if fileExtension == ".chain":
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
							
						category += f"/{fighterInfo.get(fighterID,fighterID)}"
				
			#
			#Name Overrides
			#TODO
			#print(filePath)
			outputFile.write(f"{filePath}\t{name}\t{category}\t{tags}\t{platformExtension}\t{langExtension}")
print("Done")
print("Generated new catalog. Rename after verifying if it is correct.")