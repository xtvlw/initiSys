from os import system
from json import dumps, loads

# Install modules


def getFromConfig(arg):
    """
    auxiliar function to get information from the config file
    """
    packs = ''
    with open("./config.json", "r") as config:
        config = loads(config.read())
        for pack in (config[arg]):
            packs += f"{pack} "
    return packs


def installNala():
    system("sudo apt install nala -y")


def installPacks():
    """
    Install system packs
    """
    system(f"sudo nala install {getFromConfig('packs')} -y")


def installFlatpak():
    """
    Install flatpak's apss
    """
    system(f"sudo flatpak install {getFromConfig('flatpak')} -y")


# Config Modules

def configFlatpak():
    """
    Configure all the flatpak.
    1. enable the system themes on flatpak apps.
    2. enable flathub repositories
    """
    system("sudo flatpak override --filesystem=/usr/share/themes/")
    system("sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")


def configGnome():
    """
    Config the gnome themes and extentions
    """
    # installing theme
    system("git clone https://github.com/vinceliuice/ChromeOS-theme.git")
    system("./ChromeOS-theme/install.sh")

    # installing icons
    system("git clone https://github.com/yeyushengfan258/Reversal-icon-theme.git")
    system("./Reversal-icon-theme/install.sh -a")

def start():
    """
    Indexer for all the config
    """
    installNala()
    installPacks()
    configFlatpak()
    installFlatpak()


if __name__ == "__main__":
    start()
