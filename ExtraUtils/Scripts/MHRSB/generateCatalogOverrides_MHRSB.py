#Author: NSA Cloud
#Script to modify catalog file to set categories and names automatically

#This is game specific so changes will need to be made for other games
import os
import json
import csv

def readPathOverrides(overrideDir):
	overrideDict = dict()
	
	for entry in os.scandir(overrideDir):
		if entry.is_file() and entry.name.endswith(".tsv"):
			tsvPath = os.path.join(overrideDir,entry.name)
			with open(tsvPath,"r") as file:
				rd = csv.reader(file, delimiter="\t", quotechar='"')
				next(rd)#Skip header
				
				for row in rd:
					overrideDict[row[0]] = list(row)
					
	print("Overrides:")
	print(overrideDict)
	return overrideDict

def buildWeaponIDDictFromCSV(csvPath):
	idDict = dict()
	with open(csvPath,"r",encoding = "utf-8") as file:
		rd = csv.reader(file, delimiter=",", quotechar='"')
		next(rd)#Skip header
		
		for row in rd:
			name = row[-1]
			modelID = row[3]
			if modelID not in idDict:
				idDict[modelID] = {"name":name,"altNames":[]}
			else:
				idDict[modelID]["altNames"].append(name)
	return idDict

def getIDDict(idDir):
	fullIDDict = dict()
	for entry in os.scandir(idDir):
		if entry.is_file() and entry.name.startswith("IDs_") and entry.name.endswith(".csv"):
			fullIDDict[entry.name.split("_")[1].split(".csv")[0]] = buildWeaponIDDictFromCSV(os.path.join(idDir,entry.name))
	return fullIDDict

fullIDDict = getIDDict("IDs\\")
wpLevelStrings = tuple([" I"," II"," III"," IV"," V"," VI"," VII"])
#print(fullIDDict)
"""
for weapon in fullIDDict.keys():
	print(weapon)
	for key,value in fullIDDict[weapon].items():
		print(f"\t{key}:{value}")
"""
wpPartsDict = {
	"it00":{
	 
	 },
	"it01":{
	 #"0":"Sword",
	 "1":"Shield"
	 },
	"it02":{
	 "0":"L",
	 "1":"R"
	 },
	"it03":{
	 #"0":"Sword",
	 "1":"Sheath"
	 },
	"it03":{
	 #"0":"Sword",
	 "1":"Sheath"
	 },
	"it04":{
	 
	 },
	"it05":{
	 
	 },
	"it06":{
	  #"0":"Lance",
	 "1":"Shield"
	 },
	"it07":{
	  #"0":"Lance",
	 "1":"Shield"
	 },
	"it08":{
	 },
	"it09":{
	 #"0":"Sword",
	 "1":"Shield"
	 },
	"it10":{
	 #"0":"Staff",
	 "1":"Kinsect"
	 },
	"it11":{
	 #"0":"Bow",
	 "1":"Quiver",
	 },
	"it12":{
	 },
	"it13":{
	 },
	}


CATALOG_PATH = r"J:\REAssetLibrary\MHRSB\REAssetCatalog_MHRSB.tsv"
CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\MHRSB\REAssetCatalog_MHRSB_NEW.tsv"
OVERRIDES_DIR = os.path.join(os.getcwd(),"Overrides")
#CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\MHWILDS\REAssetCatalog_MHWILDS.tsv"

overrideDict = readPathOverrides(OVERRIDES_DIR)

ARMOR_DUMP = os.path.join(os.path.dirname(__file__),"armorSeries.json")
MONSTER_DUMP = os.path.join(os.path.dirname(__file__),"monsterSeries.json")

with open(ARMOR_DUMP,"r", encoding ="utf-8") as file:
	armorInfo = json.load(file)
	
with open(MONSTER_DUMP,"r", encoding ="utf-8") as file:
	monsterInfo = json.load(file)
	largeMonsterInfo = monsterInfo["Large"]
	smallMonsterInfo = monsterInfo["Small"]
	endemicMonsterInfo = monsterInfo["Endemic"]

with open(MONSTER_DUMP,"r", encoding ="utf-8") as file:
	monsterInfo = json.load(file)
	largeMonsterInfo = monsterInfo["Large"]
	smallMonsterInfo = monsterInfo["Small"]
	endemicMonsterInfo = monsterInfo["Endemic"]
	
AUTOMATIC_CATEGORY_LIST = [
	("Armors/Male",r"player/mod/m/"),
	("Armors/Female",r"player/mod/f/"),
	
	("Weapons/Great Sword",r"weapon/GreatSword/"),
	("Weapons/Sword and Shield",r"weapon/ShortSword/"),
	("Weapons/Dual Blades",r"weapon/DualBlades/"),
	("Weapons/Long Sword",r"weapon/LongSword/"),
	("Weapons/Hammer",r"weapon/Hammer/"),
	("Weapons/Hunting Horn",r"weapon/Horn/"),
	("Weapons/Lance",r"weapon/Lance/"),
	("Weapons/Gun Lance",r"weapon/GunLance/"),
	("Weapons/Switch Axe",r"weapon/SlashAxe/"),
	("Weapons/Charge Blade",r"weapon/ChargeAxe/"),
	("Weapons/Insect Glaive",r"weapon/InsectGlaive/"),
	("Weapons/Insect Glaive",r"weapon/IG_Insect/"),
	("Weapons/Bow",r"weapon/Bow/"),
	("Weapons/Heavy Bowgun",r"weapon/HeavyBowgun/"),
	("Weapons/Light Bowgun",r"weapon/LightBowgun/"),
	
	("Items",r"item/"),
	("Items/Accessories",r"item/acc/"),
	("Items/Gimmicks",r"item/gm/"),
	("Items/Gimmicks",r"huntingMachine/"),
	("Items/Misc",r"item/item/"),
	
	
	("Player/Hair/Male",r"player/mod/m/hair"),
	("Player/Hair/Female",r"player/mod/f/hair"),
	("Player/Head",r"player/mod/face"),
	
	("NPC/",r"npc/mod/"),
	
	("Palico",r"otomo/OtAirou/mod"),
	("Palamute",r"otomo/OtDog/mod"),
	
	("Monsters",r"enemy/"),
	("Monsters/Endemic Life",r"environmentCreature/"),
	
	("Stage",r"stage/"),

	#("Gimmicks",r"Art/VFX/Mesh/Props"),
	("VFX",r"vfx/"),
	
	
	
	]


#-------------

AUTOMATIC_CATEGORY_LIST.sort(key = lambda item: len(item[1]))#Sort so largest strings are first
AUTOMATIC_CATEGORY_LIST.reverse()

with open(CATALOG_PATH,"r") as file:
    lines = file.readlines()

genderDict = {
	"ch02":"M",
	"ch03":"F",
	}

genderVariantDict = {
	"0":"M",
	"1":"F",
	}
armorSectionDict = {
	"1":"Arms",
	"2":"Body",
	"3":"Helmet",
	"4":"Legs",
	"5":"Waist",
	"6":"Slinger",
	}
monsterSectionDict = {
	"1":"Tail",
	}

with open(CATALOG_PATH_OUTPUT,"w",encoding = "utf-8") as outputFile:
	outputFile.write("File Path\tDisplay Name\tCategory (Forward Slash Separated)\tTags (Comma Separated)\tPlatform Extension\tLanguage Extension\n")#Write header line
	for line in lines[1:]:

		if len(line.strip()) != 0:
			filePath,name,category,tags,platformExtension,langExtension = line.split("\t")
			
			#Category detection
			for categoryTuple in AUTOMATIC_CATEGORY_LIST:
				if categoryTuple[1] in filePath:
					category = categoryTuple[0]
					break
			
			isChain2 = filePath.endswith(".chain2")
			splitext = os.path.splitext(os.path.split(filePath)[1])
			fileName = splitext[0]
			fileExtension = splitext[1]
			#Armor overrides
			excludeExtensionSet = set([
				".tex",
				])
			if category == "FBXSkel Files":
				category = ""
			
			if fileExtension not in excludeExtensionSet:
				if filePath.startswith("player/mod/m") or filePath.startswith("player/mod/f"):
					folderName = os.path.basename(os.path.dirname(filePath))
					if "pl" in folderName:
						partName = "Unknown Part"
						armorSeries = armorInfo.get(folderName.replace("pl",""),"")
						#if armorSeries != "":
							#print(armorSeries)
							#print(fileName)
						gender = fileName[0]
						if fileName.startswith(f"{gender}_arm"):
							partName = "Arms"
						if fileName.startswith(f"{gender}_body"):
							partName = "Body"
						if fileName.startswith(f"{gender}_helm"):
							partName = "Helmet"
						if fileName.startswith(f"{gender}_leg"):
							partName = "Legs"
						if fileName.startswith(f"{gender}_wst"):
							partName = "Waist"
						
						if partName != "Unknown Part":
							category += f"/{partName}"
						#print(filePath)
						if armorSeries != "":
								
							name =  f"{armorSeries} {partName} ({gender.upper()})"
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
						#print(name)
				#Large monster overrides
				elif filePath.startswith("enemy/"):
					variantFolder = os.path.basename(os.path.dirname(os.path.dirname(filePath)))
					monsterIDFolder = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(filePath))))
					if "em" in monsterIDFolder and not "ems" in monsterIDFolder:
						if monsterIDFolder.replace("em","") in monsterInfo["Large"]:
							#print(weaponTypeFolder)
							category += "/Large"
							monsterName = monsterInfo["Large"][monsterIDFolder.replace("em","")]
							
							
							name = monsterName
							variantType = ""
							
							if variantFolder == "01":
								variantType = " (Subspecies)"
							elif variantFolder == "02":
								variantType = " (Rare)"
							elif variantFolder == "05":
								variantType = " (Variant)"
							elif variantFolder == "07":
								variantType = " (Apex)"
							elif variantFolder == "08":
								variantType = " (Risen)"
							
							if variantType != "":
								name += variantType
							
							partName = ""
							
							if fileName.endswith("_tail"):
								partName = "Tail"
							
							if partName != "":
								name += f" ({partName})"
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
							print(name)
					if "ems" in monsterIDFolder:
						category += "/Small"
						
								
				#Small monster overrides
				elif filePath.startswith("art/model/character/ch91") and fileName.startswith("ch"):
					if fileName.count("_") == 2:
						root,emID,partIDStr = fileName.split("_")
						partName = monsterSectionDict.get(partIDStr[3],"")
						#seriesID = partIDStr[1],"UNK"
						typeVariant = partIDStr[0]
						name = f"{smallMonsterInfo.get(emID,os.path.split(filePath)[1])}"
						#Ceratonoth fix
						if "(Male)" in name and partIDStr[2] == "1":
							name = name.replace("(Male)","(Female)")
						if partName != "":
							name += f" ({partName})"
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
				
				#Endemic IDs don't line up with models, need to fix
					"""			
					#Endemic overrides
					elif filePath.startswith("art/model/character/ch80") and fileName.startswith("ch"):
						if fileName.count("_") == 2:
							root,emID,partIDStr = fileName.split("_")
							partName = monsterSectionDict.get(partIDStr[3],"")
							#seriesID = partIDStr[1],"UNK"
							typeVariant = partIDStr[0]
							name = f"{endemicMonsterInfo.get(emID,os.path.split(filePath)[1])}"
							
							if partName != "":
								name += f" ({partName})"
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
			if filePath.startswith("stage/"):
				if "setmodel" in os.path.split(filePath)[0]:
					category += "/Set Models"
				elif "base" in os.path.split(filePath)[0]:
					category += "/Base"
				else:
					category += "/Parts"
			#Weapon IDs
			if filePath.startswith("weapon/"):
				folderName = os.path.basename(os.path.dirname(filePath))
				weaponTypeFolder = os.path.basename(os.path.dirname(os.path.dirname(filePath)))
				#print(weaponTypeFolder)
				if weaponTypeFolder in fullIDDict:
					if folderName in fullIDDict[weaponTypeFolder]:
						partName = None
						if fileName.startswith("B_Ydt"):
							partName  = "Quiver"
						if fileName.startswith("DB_L"):
							partName  = "L"
						if fileName.startswith("DB_R"):
							partName  = "R"
						if fileName.startswith("LS_Saya"):
							partName = "Sheath"
						elif "_Sld" in fileName:
							partName  = "Shield"
						
						#print(fullIDDict[weaponTypeFolder][folderName])
						tags = os.path.split(filePath)[1] + ","
						name = fullIDDict[weaponTypeFolder][folderName]["name"]
						#print(name)
						#print(filePath)
						for altName in fullIDDict[weaponTypeFolder][folderName]["altNames"]:
							tags += (altName.replace("\'","")+",")
						if name.endswith(wpLevelStrings):
							name = name.rsplit(" ",1)[0]
						#name = f"{fullIDDict[wpType].get(modelID,os.path.split(filePath)[1])}"
						if partName != None:
							name += f" ({partName})"
						
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
			#Name Overrides
			if filePath in overrideDict:
				override = overrideDict[filePath]
				name = override[1]
				category = override[2]
				tags = override[3]
			#print(filePath)
			outputFile.write(f"{filePath}\t{name}\t{category}\t{tags}\t{platformExtension}\t{langExtension}")

print("Done")
print("Generated new catalog. Rename after verifying if it is correct.")
#print(weaponTypeStrings)