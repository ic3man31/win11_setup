import subprocess
import os
import time

# List of Apps
applications = [
    "Google.Chrome",
    "Mozilla.Firefox",
    "Bitwarden",
    "Microsoft.VisualStudioCode",
    "AnyDeskSoftwareGmbH.AnyDesk",
    "7zip.7zip",
    "Notepad++",
    "Obsidian.Obsidian",
    "KeePass.KeePass",
    "Everything",
    "OBSProject.OBSStudio",
    "BraveSoftware.BraveBrowser",
    "Greenshot",
    "Spotify",
    "Git.Git",
    "RevoUninstaller.RevoUninstaller"
]

def display_banner():
    banner = """
\033[34m                  o8o                .o    .o                                     .                                                     
                  `"'              o888  o888                                   .o8                                                     
oooo oooo    ooo oooo  ooo. .oo.    888   888               .oooo.o  .ooooo.  .o888oo oooo  oooo  oo.ooooo.      oo.ooooo.  oooo    ooo 
 `88. `88.  .8'  `888  `888P"Y88b   888   888              d88(  "8 d88' `88b   888   `888  `888   888' `88b      888' `88b  `88.  .8'  
  `88..]88..8'    888   888   888   888   888              `"Y88b.  888ooo888   888    888   888   888   888      888   888   `88..8'   
   `888'`888'     888   888   888   888   888              o.  )88b 888    .o   888 .  888   888   888   888 .o.  888   888    `888'    
    `8'  `8'     o888o o888o o888o o888o o888o ooooooooooo 8""888P' `Y8bod8P'   "888"  `V88V"V8P'  888bod8P' Y8P  888bod8P'     .8'     
                                                                                                   888            888       .o..P'      
                                                                                                  o888o          o888o      `Y8P'     
\033[0m                                                     By: \033[1mgithub.com/ic3man31\033[0m                                                               
"""
    print(banner)

# Clear terminal
def cl():
    os.system('cls' if os.name == 'nt' else 'clear')

# Install, Update, Uninstall
def inst_upd_del(action):
        for app in applications:
            print("[+] {}ing {}...".format(action.title(), app))
            subprocess.run(["winget", action, "-e", "--silent", app], shell=True)
            print("{} {}ed successfully!".format(app, action.title()))

# Main Menù
def main_menu():
    display_banner()
    print()
    print("\033[1;32mInstall\033[0m/\033[1;34mUpdate\033[0m/\033[1;31mUninstall\033[0m the following Apps: ")
    print()
    for p in applications:
        print('> {}'.format(p))
    print()
    valid_opt = [1, 2, 3, 4]
    while True:
        print('\n[1] \033[1;32mInstall\033[0m \n[2] \033[1;34mUpdate\033[0m \n[3] \033[1;31mUninstall\033[0m \n[4] Exit(or Ctrl+C)')
        print()
        try:
            user_input = int(input('Enter an action: '))
            if user_input in valid_opt:
                return user_input
            else:
                print()
                print("\033[1;31m[!] Action NOT Available\033[0m")
                time.sleep(4)
        except ValueError:
            print()
            print('\033[1;31m[!] Invalid input. Please enter an integer.\033[0m')
            time.sleep(4)
         
while True:
    user_inpt = main_menu()
    if user_inpt == int(1):
        print()
        inst_upd_del('install')
        time.sleep(10)
        cl()
    elif user_inpt == int(2):
        print()
        inst_upd_del('update')
        time.sleep(10)
        cl()
    elif user_inpt == int(3):
        print()
        inst_upd_del('uninstall')
        time.sleep(10)
        cl()
    elif user_inpt == int(4):
        print('[-] Thank you. Bye !')
        time.sleep(3)
        exit()