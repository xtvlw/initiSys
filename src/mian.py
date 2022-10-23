from os import system
from json import dumps, loads

def install(args):
    system(f"sudo nala {args} -y")



def main():
    with open('../public/config.json', 'r') as config:
        config = loads(config.read())
        system(f"sudo apt install {config.initInstall} -y")
    

if __name__ == "__main__":
    main()