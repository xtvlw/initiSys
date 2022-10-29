from os import system
from json import dumps, loads


def installNala():
	system("sudo apt install nala -y")


def installPacks():
	with open("./config.json", "r") as config:
		a = (config.read())
		print(type(a))
		file = loads(config.read())
		for pack in file.packs:
			packs += pack
		print(packs)

def start():
	installPacks()


if __name__ == "__main__":
	start()