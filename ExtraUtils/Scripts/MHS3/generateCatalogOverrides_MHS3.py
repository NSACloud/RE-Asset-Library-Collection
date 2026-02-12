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
	with open(csvPath,"r") as file:
		rd = csv.reader(file, delimiter=",", quotechar='"')
		next(rd)#Skip header
		next(rd)#
		
		for row in rd:
			name = row[4]
			modelIDIndex = len(row) - 2
			modelID = row[modelIDIndex]
			if modelID not in idDict:
				idDict[modelID] = {"name":name,"altNames":[]}
			else:
				idDict[modelID]["altNames"].append(name)
	return idDict



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


CATALOG_PATH = r"J:\REAssetLibrary\MHS3\REAssetCatalog_MHS3.tsv"
CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\MHS3\REAssetCatalog_MHS3.tsv"
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
	("Armors/Male",r"art/model/character/ch02"),
	("Armors/Female",r"art/model/character/ch03"),
	
	("Weapons/Great Sword",r"art/model/item/it00"),
	("Weapons/Sword and Shield",r"art/model/item/it01"),
	("Weapons/Dual Blades",r"art/model/item/it02"),
	("Weapons/Long Sword",r"art/model/item/it03"),
	("Weapons/Hammer",r"art/model/item/it04"),
	("Weapons/Hunting Horn",r"art/model/item/it05"),
	("Weapons/Lance",r"art/model/item/it06"),
	("Weapons/Gun Lance",r"art/model/item/it07"),
	("Weapons/Switch Axe",r"art/model/item/it08"),
	("Weapons/Charge Blade",r"art/model/item/it09"),
	("Weapons/Insect Glaive",r"art/model/item/it10"),
	("Weapons/Bow",r"art/model/item/it11"),
	("Weapons/Heavy Bowgun",r"art/model/item/it12"),
	("Weapons/Light Bowgun",r"art/model/item/it13"),
	
	("Items",r"art/model/item"),
	("Items/Pendants",r"art/model/item/it48/"),
	("Items/Talismans",r"art/model/item/it50/15/"),
	
	("Player/Hair",r"art/model/character/ch01/000"),
	("Player/Hair",r"art/model/character/ch01/001/0"),
	("Player/Hair",r"art/model/character/ch01/001/1"),
	("Player/Hair",r"art/model/character/ch01/001/2"),
	("Player/Head/Male",r"art/model/character/ch00/000"),
	("Player/Head/Female",r"art/model/character/ch00/001"),
	
	("NPC/Body",r"art/model/character/ch04"),
	("NPC/Hair",r"art/model/character/ch01/7"),
	("NPC/Hair",r"art/model/character/ch01/8"),
	("NPC/Head",r"art/model/character/ch00/5"),
	("NPC/Head",r"art/model/character/ch00/7"),
	("NPC/Head",r"art/model/character/ch00/8"),
	("NPC/Head",r"art/model/character/ch00/9"),
	
	("Palico",r"art/model/character/ch05"),
	("Seikret",r"art/model/character/ch07"),
	
	("Monsters/Endemic Life",r"art/model/character/ch80"),
	("Monsters/Large",r"art/model/character/ch90"),
	("Monsters/Small",r"art/model/character/ch91"),
	
	("Stage/Set Models",r"art/model/stagemodel/sm"),
	("Stage/Parts",r"art/stage"),

	#("Gimmicks",r"Art/VFX/Mesh/Props"),
	("VFX",r"art/effect"),
	
	
	
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
	"1":"Crystals",
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
			if fileExtension not in excludeExtensionSet and fileName.startswith("ch"):
				if filePath.startswith("art/model/character/ch02") or filePath.startswith("art/model/character/ch03"):
					if fileName.count("_") == 2:
						genderStr,armorID,partIDStr = fileName.split("_")
						gender = genderDict.get(genderStr,"UNK")
						#print(filePath)
						armorSection = armorSectionDict.get(partIDStr[3],"Unknown Part")
						variantGender = genderVariantDict.get(partIDStr[2],"UNK")
						#seriesID = partIDStr[1],"UNK"
						typeVariant = partIDStr[0]#Alpha, beta, gamma armor? Used on innerwear
						name = f"{armorInfo.get(armorID,os.path.split(filePath)[1])} ({gender})"
						#print(partIDStr[0:2])
						if partIDStr [0:2] == "50" or partIDStr [0:2] == "60":
							name = "Guardian " + name
						
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
				
				#Large monster overrides
				elif filePath.startswith("art/model/character/ch90") and fileName.startswith("ch"):
					if fileName.count("_") == 2:
						root,emID,partIDStr = fileName.split("_")
						partName = monsterSectionDict.get(partIDStr[3],"")
						#seriesID = partIDStr[1],"UNK"
						typeVariant = partIDStr[0]
						subspecies = partIDStr[1]
						typeVariant2 = partIDStr[2]
						name = f"{largeMonsterInfo.get(emID,os.path.split(filePath)[1])}"
						if typeVariant == "7":
							partName = "Saddle"
						
						
						if subspecies == "1" and typeVariant == "0":
							name += " (Subspecies)"
						elif subspecies == "2" and typeVariant == "0":
							name += " (Rare)"
						elif subspecies == "4"and typeVariant == "0":
							name += " (Deviant)"
						elif subspecies == "5" and typeVariant == "0":
							name += " (Variant)"
						elif subspecies == "7":
							name += " (Apex)"
						elif subspecies == "8" and typeVariant == "0":
							name += " (Risen)"
							
						if typeVariant2 == "3":
							name =  name + " (Baby)"
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
							category += " (Skeleton)"
							
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
							category += " (Skeleton)"
				
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
			#Weapon IDs
				
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