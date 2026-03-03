
import os
import json
import csv

CATALOG_PATH = r"J:\REAssetLibrary\RE9\REAssetCatalog_RE9.tsv"

CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\RE9\REAssetCatalog_RE9.tsv"

AUTOMATIC_CATEGORY_LIST = [

	
	#(r"CATEGORY_NAME",r"directoryPath"),
	
	("Characters/Other",r"character/ch/"),
	("Characters/Leon",r"character/ch/ch01"),
	("Characters/Grace",r"character/ch/ch02"),
	("Characters/Sherry",r"character/ch/ch06"),
	("Characters/Emily",r"character/ch/ch13/1300"),
	("Characters/Emily",r"character/ch/ch03/0300"),
	("Characters/Nathan",r"character/ch/ch15/1500"),
	("Characters/Harry",r"character/ch/ch15/1510"),
	("Characters/Alyssa",r"character/ch/ch18"),
	("Characters/Victor",r"character/ch/ch51/5100"),
	("Characters/Police",r"character/ch/ch40/4030"),
	
	("Characters/Civilians/Male/Heads",r"character/ch/ch40/4000/10"),
	("Characters/Civilians/Male/Glasses",r"character/ch/ch40/4000/15"),
	("Characters/Civilians/Male/Hats",r"character/ch/ch40/4000/16"),
	("Characters/Civilians/Male/Hair",r"character/ch/ch40/4000/20"),
	("Characters/Civilians/Male/Clothes",r"character/ch/ch40/4005"),
	
	("Characters/Civilians/Male/Heads",r"character/ch/ch42/4200/10"),
	("Characters/Civilians/Male/Glasses",r"character/ch/ch42/4200/15"),
	("Characters/Civilians/Male/Hats",r"character/ch/ch42/4200/16"),
	("Characters/Civilians/Male/Hair",r"character/ch/ch42/4200/20"),
	("Characters/Civilians/Male/Clothes",r"character/ch/ch42/4210"),
	
	("Characters/Civilians/Female/Heads",r"character/ch/ch41/4100/10"),
	("Characters/Civilians/Female/Glasses",r"character/ch/ch41/4100/15"),
	("Characters/Civilians/Female/Hair",r"character/ch/ch41/4100/20"),
	("Characters/Civilians/Female/Clothes",r"character/ch/ch41/4110"),
	
	("Characters/Zombies (RC)",r"character/ch/ch52"),
	
	("Characters/FBI",r"character/ch/ch40/4010"),
	("Characters/Soldiers",r"character/ch/ch40/4070"),
	("Characters/Soldiers",r"character/ch/ch41/4170"),
	("Characters/Zeno",r"character/ch/ch80/8000"),
	("Characters/Animals",r"character/ch/ch98"),
	
	("Characters/Bosses/Tyrant",r"character/ch/ch86/8610"),
	("Characters/Bosses/Tyrant",r"character/ch/ch86/8620"),
	("Characters/Bosses/Spider",r"character/ch/ch77/7700"),
	("Characters/Bosses/Spider",r"character/ch/ch77/7710"),
	("Characters/Bosses/Chef",r"character/ch/ch43/4310"),
	("Characters/Bosses/Mutated Victor",r"character/ch/ch51/5110"),
	("Characters/Bosses/Mutated Victor",r"character/ch/ch51/5120"),
	("Characters/Bosses/Mutated Emily",r"character/ch/ch43/4395"),
	("Characters/Bosses/Mutated Emily",r"character/ch/ch13/1310"),
	("Characters/Bosses/Chunk",r"character/ch/ch44/4400"),
	("Characters/Bosses/The Girl",r"character/ch/ch12/1210"),
	("Characters/Bosses/Commander",r"character/ch/ch09/0900"),
	
	("Weapons/Other",r"character/wp"),
	("Weapons/Melee/Other",r"character/wp/wp65"),
	("Weapons/Pistols",r"character/wp/wp01"),
	("Weapons/SMGs",r"character/wp/wp02"),
	("Weapons/Shotguns",r"character/wp/wp03"),
	("Weapons/Assualt Rifles",r"character/wp/wp04"),
	("Weapons/Sniper Rifles",r"character/wp/wp05"),
	("Weapons/Special",r"character/wp/wp07"),
	("Weapons/Special",r"character/wp/wp08"),
	("Weapons/Attachments",r"character/wp/wp20"),
	("Weapons/Ammo",r"character/wp/wp30"),
	("Weapons/Magazines",r"character/wp/wp31"),
	("Weapons/Casings",r"character/wp/wp32"),
	("Weapons/Throwables",r"character/wp/wp33"),
	("Weapons/Charms",r"character/wp/wp38"),
	("Weapons/Melee/Knives",r"character/wp/wp40"),
	("Weapons/Melee/Enemy",r"character/wp/wp65"),
	
	("Items/Healing Items",r"character/wp/wp34"),
	("Items/Held Objects",r"character/wp/wp35"),
	("Items/Inspectable Objects",r"environment/sm/sm9x/sm91"),
	("Items/Key Items",r"environment/sm/sm9x/sm90"),
	
	
	("Props",r"environment/sm"),
	
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




allowedExtensions = [".fbxskel",".refskel",".mesh",".chain2"]

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
			
			#Lazy fix
			if category == "FBXSkel Files":
				category = ""
			elif category == "REFSKEL Files":
				category = ""
			elif category == "SKELETON Files":
				category = ""
			
			
			
			splitext = os.path.splitext(os.path.split(filePath)[1])
			fileName = splitext[0]
			fileExtension = splitext[1]
			
			gibsIDSet = set(["50","51","60","61","70","71","80","81"])
			
			outfitIDs = {
				"Leon":{
					"ch0100":"Default",
					"ch0150":"Suit",
					"ch0151":"Apocalypse",
					"ch0152":"RE4",
					"ch0153":"RPD",
					},
				"Grace":{
					"ch0200":"Default",
					"ch0250":"FBI",
					"ch0251":"Film Noir",
					"ch0252":"Apocalypse",
					"ch0253":"Dimitrescu",
					},
				"Alyssa":{
					"ch1800":"Default",
					},
				"Sherry":{
					"ch0600":"Default",
					},
				"Zeno":{
					"ch8000":"Default",
					},
				"Emily":{
					"ch1300":"Default",
					"ch0300":"Alternate",
					},
				"Nathan":{
					"ch1500":"Default",
					},
				"Harry":{
					"ch1510":"Default",
					},
				"Victor":{
					"ch5100":"Default",
					},
				}
			
			
			
			partIDDict = {
				"01":"R Arm",
				"02":"L Arm",
				"08":"Gloves",
				"09":"Watch",
				"10":"Head",
				"14":"Earrings",
				"15":"Headwear",
				"16":"Hat",
				"17":"Headset",
				"20":"Hair",
				"21":"Hair Alt",
				"40":"Torso",
				"41":"Sling",
				"42":"Backpack",
				"43":"Harness",
				"44":"Armor",
				"45":"Jacket",
				"46":"Alt Jacket",
				"48":"Blanket",
				"50":"Legs",
				"55":"Skirt",
				
				}
			
			#Character part sets
			#print(filePath)
			if filePath.startswith("character/ch/ch") and fileExtension in allowedExtensions:
				#print(filePath)
				charName = category.split("/")[-1]
				#print(charName)
				#print(charName)
				if  fileName.count("_") == 2:
					charID,partID,subPartID = fileName.split("_")
				
					if charName in outfitIDs:
						outfitName = outfitIDs[charName].get(charID,f"Unknown Outfit {charID}")
						partName = partIDDict.get(partID,f"Part {partID}")
						if subPartID in gibsIDSet and "Arm" not in partName and "Glove" not in partName:
							newCategory = category +"/Gibs"
						else:
							newCategory = category + f"/{outfitName}"
						
						
						newName = f"{charName} {outfitName} ({partName}) {subPartID}"
						print(newName)
						print(newCategory)
						if fileExtension == ".chain2":
							newName += " (Chain Physics)"
						elif fileExtension == ".mdf2":
							newName += " (Material Data)"
						elif fileExtension == ".clsp":
							newName += " (Collision Shape)"
						elif fileExtension == ".sfur":
							newName += " (Shell Fur)"
						elif fileExtension == ".jcns":
							newName += " (Joint Constraints)"
						elif fileExtension == ".fbxskel":
							newName += " (Base Skeleton)"
						elif fileExtension == ".refskel":
							newName += " (Base Skeleton)"
						elif fileExtension == ".skeleton":
							newName += " (Base Skeleton)"
						name = newName
						category = newCategory
						
			#Name Overrides
			if filePath in overrideDict:
				override = overrideDict[filePath]
				name = override[1]
				category = override[2]
				tags = override[3]
			outputFile.write(f"{filePath}\t{name}\t{category}\t{tags}\t{platformExtension}\t{langExtension}")
print(f"Generated new catalog: {CATALOG_PATH_OUTPUT}")