#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici

import json
from os import path
from recettes import add_recipes,print_recipe

# TODO: Définissez vos fonction ici

def find_error(file1,file2):
    with open(file1,encoding="utf-8") as f1, open(file2) as f2:
        for index,line1 in enumerate(f1):
            line2=f2.readline()
            if line1!=line2 :
                print(f"il y a une erreur ds la ligne {index+1}")
                break


def triplet(file1,file2):
    with open(file1,encoding="utf-8") as f1, open(file2,"w") as f2 :
        for line in f1 :
            f2.write(line.replace(" ","   "))

def note(file1,file2):
    with open(file1) as f :
        note_percentage=f.read().splitlines()

    with open(file2,"w") as f :
        for note in note_percentage :
         for key,value in PERCENTAGE_TO_LETTER.items() :
            if value[0]<= int(note) < value[1] :
                f.write(note + " " + key + "\n")
                break



def suprimer(recipes) :
    nom=input("donner le nom de la recette a supprimer \n")
    if nom in recipes :
        del recipes[nom]
        print("la recette est supprimée")
    else:
        print("la recette donner ne se trouve pas dans la liste des recettes ! \n")





def exercice4(file_path="./recipes.p") :
    if path.exists(file_path) :
        recipes=json.load(open(file_path,"r"))

    else:
        recipes=dict()

    while True :
        choice = input("choisir une option :\n a) ajouter une recette \n b) modifier une recette\n c) supprimer une recette\n d) afficher une recette \n e) sortir d la fonction \n ").strip()

        if choice=="a" :
            recipes=add_recipes(recipes)
        elif choice=="b" :
            recipes=add_recipes(recipes)
        elif choice == "c":
            recipes=suprimer(recipes)
        elif choice == "d":
            recipes=print_recipe(recipes)
        elif choice == "e":
            break
        else:
            print("le choix n'est pas valide!!")

    json.dump(recipes,open(file_path,"w"))




def exercice5(file1) :
    list_1=[]
    list_2=[]
    with open(file1,encoding="utf-8") as f :
        file1=f.readlines()
        for ligne in file1 :
            list_1.append(ligne.split(" "))

        for ligne in list_1 :
            for elem in ligne :
                try :
                    list_2.append(int(elem))
                except :
                    pass

    return list_2



def exercice6(file1,file2) :
    with open(file1,encoding="utf-8") as f1,open(file2,"w") as f2 :
        liste_1=f1.readlines()
        for index,i in enumerate(liste_1) :
            if index%2 == 0 :
                f2.write(i)






if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    find_error("./exemple.txt", "./exemple2.txt")
    triplet("./exemple.txt", "./exemple2.txt")
    note("./notes.txt", "./exemple2.txt")
    exercice4()
    exercice5("./exemple.txt")
    exercice6("./exemple.txt","./exemple2.txt")

