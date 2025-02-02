#Author: NSA Cloud
#Script to modify catalog file to set categories and names automatically

#This is game specific so changes will need to be made for other games
import os
import json
CATALOG_PATH = r"J:\REAssetLibrary\MHWILDS\REAssetCatalog_MHWILDS.tsv"
CATALOG_PATH_OUTPUT = r"J:\REAssetLibrary\MHWILDS\REAssetCatalog_MHWILDS_new.tsv"

ARMOR_DUMP = os.path.join(os.path.dirname(__file__),"armorSeries.json")
MONSTER_DUMP = os.path.join(os.path.dirname(__file__),"monsterSeries.json")

with open(ARMOR_DUMP,"r", encoding ="utf-8") as file:
	armorInfo = json.load(file)
	
with open(MONSTER_DUMP,"r", encoding ="utf-8") as file:
	monsterInfo = json.load(file)
AUTOMATIC_CATEGORY_LIST = [
	("Armors/Male",r"Art\Model\Character\ch02"),
	("Armors/Female",r"Art\Model\Character\ch03"),
	
	("Weapons/Great Sword",r"Art\Model\Item\it00"),
	("Weapons/Great Sword",r"Art\Model\Item\it02"),
	("Weapons/Sword and Shield",r"Art\Model\Item\it01"),
	("Weapons/Long Sword",r"Art\Model\Item\it03"),
	("Weapons/Hammer",r"Art\Model\Item\it04"),
	("Weapons/Hunting Horn",r"Art\Model\Item\it05"),
	("Weapons/Lance",r"Art\Model\Item\it06"),
	("Weapons/Gun Lance",r"Art\Model\Item\it07"),
	("Weapons/Switch Axe",r"Art\Model\Item\it08"),
	("Weapons/Charge Blade",r"Art\Model\Item\it09"),
	("Weapons/Insect Glaive",r"Art\Model\Item\it10"),
	("Weapons/Bow",r"Art\Model\Item\it11"),
	("Weapons/Heavy Bowgun",r"Art\Model\Item\it12"),
	("Weapons/Light Bowgun",r"Art\Model\Item\it13"),
	("Items/Misc",r"Art\Model\Item"),
	
	("Player/Hair/Male",r"Art\Model\Character\ch01\000\0"),
	("Player/Hair/Female",r"Art\Model\Character\ch01\001\0"),
	("Player/Eyebrows/Male",r"Art\Model\Character\ch01\000\1"),
	("Player/Eyebrows/Female",r"Art\Model\Character\ch01\001\1"),
	("Player/Beards/Male",r"Art\Model\Character\ch01\000\2"),
	("Player/Beards/Female",r"Art\Model\Character\ch01\001\2"),
	("Player/Head/Male",r"Art\Model\Character\ch00\000"),
	("Player/Head/Female",r"Art\Model\Character\ch00\001"),
	
	("NPC/Body",r"Art\Model\Character\ch04"),
	("NPC/Hair",r"Art\Model\Character\ch01\5"),
	("NPC/Hair",r"Art\Model\Character\ch01\9"),
	("NPC/Head",r"Art\Model\Character\ch00\5"),
	("NPC/Head",r"Art\Model\Character\ch00\8"),
	("NPC/Head",r"Art\Model\Character\ch00\9"),
	
	("Palico",r"Art\Model\Character\ch05"),
	("Seikret",r"Art\Model\Character\ch07"),
	
	("Monsters/Endemic Life",r"Art\Model\Character\ch80"),
	("Monsters/Large",r"Art\Model\Character\ch90"),
	("Monsters/Small",r"Art\Model\Character\ch91"),
	
	("Stage/Set Models",r"Art\Model\StageModel\sm"),
	("Stage/Base",r"GameDesign\Stage"),
	("Stage/Parts",r"Art\Stage"),
	
	("UI/Minimap",r"GUI\ui_mesh\ui060000\st"),
	("UI",r"GUI\ui_mesh"),
	#("Gimmicks",r"Art\VFX\Mesh\Props"),
	("VFX/Ammo",r"Art\VFX\Mesh\Common\Shell"),
	("VFX",r"Art\VFX"),
	
	
	
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
				if filePath.startswith("Art\Model\Character\ch02") or filePath.startswith("Art\Model\Character\ch03"):
					if fileName.count("_") == 2:
						genderStr,armorID,partIDStr = fileName.split("_")
						gender = genderDict.get(genderStr,"UNK")
						#print(filePath)
						armorSection = armorSectionDict.get(partIDStr[3],"Unknown Part")
						variantGender = genderVariantDict.get(partIDStr[2],"UNK")
						#seriesID = partIDStr[1],"UNK"
						typeVariant = partIDStr[0]#Alpha, beta, gamma armor? Used on innerwear
						name = f"{armorInfo.get(armorID,os.path.split(filePath)[1])} {armorSection} ({gender}-{variantGender})"
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
				elif filePath.startswith("Art\Model\Character\ch90") and fileName.startswith("ch"):
					if fileName.count("_") == 2:
						root,emID,partIDStr = fileName.split("_")
						partName = monsterSectionDict.get(partIDStr[3],"")
						#seriesID = partIDStr[1],"UNK"
						typeVariant = partIDStr[0]
						name = f"{monsterInfo.get(emID,os.path.split(filePath)[1])}"
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
			#
			#Name Overrides
			#TODO
			#print(filePath)
			outputFile.write(f"{filePath}\t{name}\t{category}\t{tags}\t{platformExtension}\t{langExtension}")
print("Done")
print("Generated new catalog. Rename after verifying if it is correct.")