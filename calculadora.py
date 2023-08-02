import os

print ("Benvingut hermano :D")
print ("--------------------------Instruccions--------------------------")
print ("Posa un nombre, després un operador i finalment altre nombre")
print("IMPORTANT! A les arrels, el segon nombre puede ser qualsevol")
print("© 2023-2023 Miquel Estruch. All rights reserved")
print ("-----------------------------------------------------------------")

def Calc():
    numerouno = float(input ("Fica un número: "))
    Pregunta = input ("Que vols fer: +\-\*\ /\**\//: ")
    numerodos = float(input ("Fica altre número: "))

    if Pregunta == "+":
        print (numerouno + numerodos)
    elif Pregunta == "//":
        print ( numerouno ** (0.5))
    elif Pregunta == "-":
        print (numerouno - numerodos)
    elif Pregunta == "*":
        print (numerouno * numerodos)
    elif Pregunta == "**":
        print (numerouno ** numerodos)
    elif Pregunta == "/":
        print (numerouno / numerodos)
    else:
        print ("FATAL ERROR! MUST RESTART :(")
        print("")
    def reinicio():
        reiniciar = input("Desitja continuar? [Y/n]: ")
        if reiniciar == "Y":
            print("")
            Calc()
        elif reiniciar == "y":
            print("")
            Calc()
        elif reiniciar == "n":
            print("")
            print("Moltes gràcies per utilitzar aquest programa!")
            print("© 2023-2023 Miquel Estruch. All rights reserved")
            exit()
        else:
            print("no t'he entès, Desitja continuar? [Y/n]:")
            reinicio()
    reinicio()
    Calc()
Calc()
