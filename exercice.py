#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici

def comparateur(premier_fichier, deuxieme_fichier):
    if premier_fichier != deuxieme_fichier:
        with open(premier_fichier, encoding="utf-8") as fichier1, open(deuxieme_fichier, encoding="utf-8") as fichier2:
            for index, line1 in enumarate(fichier1):
                line2 = fichier2.readline()
                if line1 != line2:
                    print(f"Les fichiers sont différents à la ligne {index + 1}, on a")
                    print(line1)
                    print("et on a:")
                    print(line2)
                    break
def triple_espace(input_file, output_file):
    with open(input_file, encoding= "utf-8") as in_file, open(output_file, "w", encoding="utf-8") as out_file:
        for line in in_file:
            words = line.split()
            line_triple = "   ".join(words)
            out_file.write(line_triple)                 # out_file.write(line_triple)








if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
