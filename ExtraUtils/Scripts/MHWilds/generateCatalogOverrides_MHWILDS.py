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


def getIDDict(idDir):
	fullIDDict = dict()
	for entry in os.scandir(idDir):
		if entry.is_file() and entry.name.startswith("it") and entry.name.endswith(".csv"):
			fullIDDict[entry.name.split("_")[0]] = buildWeaponIDDictFromCSV(os.path.join(idDir,entry.name))
	return fullIDDict

fullIDDict = getIDDict("IDs\\")
wpLevelStrings = tuple([" I"," II"," III"," IV"," V"," VI"," VII"])
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

weaponTypeStrings = tuple(fullIDDict.keys())
CATALOG_PATH = r"J:\REAssetLibrary\MHWILDS\REAssetCatalog_MHWILDS.tsv"
CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\MHWILDS\REAssetCatalog_MHWILDS_NEWTU1_AKUMA.tsv"
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
	("Armors/Male",r"Art/Model/Character/ch02"),
	("Armors/Female",r"Art/Model/Character/ch03"),
	
	("Weapons/Great Sword",r"Art/Model/Item/it00"),
	("Weapons/Sword and Shield",r"Art/Model/Item/it01"),
	("Weapons/Dual Blades",r"Art/Model/Item/it02"),
	("Weapons/Long Sword",r"Art/Model/Item/it03"),
	("Weapons/Hammer",r"Art/Model/Item/it04"),
	("Weapons/Hunting Horn",r"Art/Model/Item/it05"),
	("Weapons/Lance",r"Art/Model/Item/it06"),
	("Weapons/Gun Lance",r"Art/Model/Item/it07"),
	("Weapons/Switch Axe",r"Art/Model/Item/it08"),
	("Weapons/Charge Blade",r"Art/Model/Item/it09"),
	("Weapons/Insect Glaive",r"Art/Model/Item/it10"),
	("Weapons/Bow",r"Art/Model/Item/it11"),
	("Weapons/Heavy Bowgun",r"Art/Model/Item/it12"),
	("Weapons/Light Bowgun",r"Art/Model/Item/it13"),
	("Items/Misc",r"Art/Model/Item"),
	
	("Player/Hair/Male",r"Art/Model/Character/ch01/000/0"),
	("Player/Hair/Female",r"Art/Model/Character/ch01/001/0"),
	("Player/Eyebrows/Male",r"Art/Model/Character/ch01/000/1"),
	("Player/Eyebrows/Female",r"Art/Model/Character/ch01/001/1"),
	("Player/Beards/Male",r"Art/Model/Character/ch01/000/2"),
	("Player/Beards/Female",r"Art/Model/Character/ch01/001/2"),
	("Player/Head/Male",r"Art/Model/Character/ch00/000"),
	("Player/Head/Female",r"Art/Model/Character/ch00/001"),
	
	("NPC/Body",r"Art/Model/Character/ch04"),
	("NPC/Hair",r"Art/Model/Character/ch01/5"),
	("NPC/Hair",r"Art/Model/Character/ch01/9"),
	("NPC/Head",r"Art/Model/Character/ch00/5"),
	("NPC/Head",r"Art/Model/Character/ch00/8"),
	("NPC/Head",r"Art/Model/Character/ch00/9"),
	
	("Palico",r"Art/Model/Character/ch05"),
	("Seikret",r"Art/Model/Character/ch07"),
	
	("Monsters/Endemic Life",r"Art/Model/Character/ch80"),
	("Monsters/Large",r"Art/Model/Character/ch90"),
	("Monsters/Small",r"Art/Model/Character/ch91"),
	
	("Stage/Set Models",r"Art/Model/StageModel/sm"),
	("Stage/Base",r"GameDesign/Stage"),
	("Stage/Parts",r"Art/Stage"),
	
	("UI/Minimap",r"GUI/ui_mesh/ui060000/st"),
	("UI",r"GUI/ui_mesh"),
	#("Gimmicks",r"Art/VFX/Mesh/Props"),
	("VFX/Ammo",r"Art/VFX/Mesh/Common/Shell"),
	("VFX",r"Art/VFX"),
	
	
	
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
			
			if fileExtension not in excludeExtensionSet and fileName.startswith("ch"):
				if filePath.startswith("Art/Model/Character/ch02") or filePath.startswith("Art/Model/Character/ch03"):
					if fileName.count("_") == 2:
						genderStr,armorID,partIDStr = fileName.split("_")
						gender = genderDict.get(genderStr,"UNK")
						#print(filePath)
						armorSection = armorSectionDict.get(partIDStr[3],"Unknown Part")
						variantGender = genderVariantDict.get(partIDStr[2],"UNK")
						#seriesID = partIDStr[1],"UNK"
						typeVariant = partIDStr[0]#Alpha, beta, gamma armor? Used on innerwear
						name = f"{armorInfo.get(armorID,os.path.split(filePath)[1])} {armorSection} ({gender}-{variantGender})"
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
						category += f"/{armorSection}"
				
				#Large monster overrides
				elif filePath.startswith("Art/Model/Character/ch90") and fileName.startswith("ch"):
					if fileName.count("_") == 2:
						root,emID,partIDStr = fileName.split("_")
						partName = monsterSectionDict.get(partIDStr[3],"")
						#seriesID = partIDStr[1],"UNK"
						typeVariant = partIDStr[0]
						subspecies = partIDStr[1]
						name = f"{largeMonsterInfo.get(emID,os.path.split(filePath)[1])}"
						if typeVariant == "5" and "Guardian" not in name:
							name = "Guardian " + name
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
							
				#Small monster overrides
				elif filePath.startswith("Art/Model/Character/ch91") and fileName.startswith("ch"):
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
					elif filePath.startswith("Art/Model/Character/ch80") and fileName.startswith("ch"):
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
				
			elif filePath.startswith("Art/Model/Item/it") and fileName.startswith(weaponTypeStrings):
				
				if fileName.count("_") == 2:
					wpTypeStr,wpIDStr,partStr = fileName.split("_")
					idPart1 = wpTypeStr[4::]
					wpType = wpTypeStr[:4]
					#print(wpType)
					
					#print(idPart1)
					#print(wpIDStr)
					if idPart1[0] == "1":
						modelID = idPart1+wpIDStr
					
					elif idPart1 == "01":#Base Iron/Bone Weapon?
						modelID = "1"+wpIDStr
					else:
						modelID = str(int(wpIDStr))
					#print(fileName)
					#print(modelID)
					if fullIDDict[wpType].get(modelID):
						#print(fullIDDict[wpType][modelID])
						pass
					else:
						pass
						#print("not found")
					
					
					modelName = fullIDDict[wpType].get(modelID,None)
					partName = wpPartsDict[wpType].get(partStr,None)
					
					
					if modelName != None:
						#Remove weapon level from name
						name = modelName["name"]
						#print(tags)
						tags = os.path.split(filePath)[1] + ","
						for altName in modelName["altNames"]:
							tags += (altName.replace("\'","")+",")
						if name.endswith(wpLevelStrings):
							name = name.rsplit(" ",1)[0]
					else:
						name = os.path.split(filePath)[1]
					#name = f"{fullIDDict[wpType].get(modelID,os.path.split(filePath)[1])}"
					if partName != None:
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
					
			#
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