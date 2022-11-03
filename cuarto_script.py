# Prueba simple de una interfaz de consola en Python
import os
import sys
import time
import platform
import subprocess
ans = True

def inicio():
    for i in range(0,5):
        print("Espera.")
        time.sleep(0.2)
        os.system("clear")
        print("Espera..")
        time.sleep(0.2)
        os.system("clear")
        print("Espera...")
        time.sleep(0.2)
        os.system("clear")
           
    for i in range(0,5):
        print("Cargando interfaz.")
        time.sleep(0.2)
        os.system("clear")
        print("Cargando interfaz..")
        time.sleep(0.2)
        os.system("clear")
        print("Cargando interfaz...")
        time.sleep(0.2)
        os.system("clear")
                
if __name__ == "__main__":
    inicio()
    while ans:
        print("\n 1.Opcion 1 \n 2.Opcion 2 \n 3.Opcion 3 \n 4.Exit/Quit")
        ans=input("¿Qué quieres hacer? \n")
        if ans=="1":
            os.system("clear")
            print("\n Opción 1 hecha")
        elif ans=="2":
            os.system("clear")
            print("\n Opción 2 hecha") 
        elif ans=="3":
            os.system("clear")
            print("\n Opción 3 hecha") 
        elif ans=="4":
            os.system("clear")
            print("\n Adiós")
            sys.exit()
        elif ans !="":
            os.system("clear")
            print("\n Esa opción no esa válida")
            

