#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


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






if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    find_error("./exemple.txt","./exemple2.txt")

    triplet("./exemple.txt","./exemple2.txt")
