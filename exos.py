import math
import re

# ex1
# time = 6.892
# distance = 19.7
#vitesse = distance/time
# print(round(vitesse))

# ex2
# name = str(input("nom : "))
# age = int(input("age : "))
# print("vous vous appelez", nom, "et vous avez", age)

# ex3
# x = 2.15
# if x >= 0 :
#     print(math.sqrt(x))
# else:
#     print("err")

# ex4
# word1 =  "mot1"
# word2 = "mot2"
# print(min(word1, word2))

# # ex5
# pressSeuil = 2.3
# volSeuil = 7.41

# p = float(input("pression : "))
# v = float(input("volume courant : "))

# # –si le volume et la pression sont supérieurs aux seuils : arrêt immédiat ;
# # –si seule la pression est supérieure à la pression seuil : demander d’augmenter le volume de l’enceinte ;
# # –si seul le volume est supérieur au volume seuil : demander de diminuer le volumede l’enceinte ;
# # –sinon déclarer que « tout va bien ».
# if p > pressSeuil and v > volSeuil :
#     print("Arret immédiat")
# elif p > pressSeuil:
#     print("augmenter le volume de l’enceinte")
# elif v > volSeuil:
#     print("diminuer le volume de l’enceinte")
# else:
#     print('tout va bien ')

# ex6

# mail = str(input("votre mail : "))
# if(re.search(r"\b@\b.*\b.com\b", mail)):
#     print("Valid mail")
# else:
#     print("Invalid mail")

# ex7
# for x in range(0, 10):
#     print('yoyo')

# ex8
# for x in ("pipo"):
#     print(x)

# ex9
# a = 0 
# b = 10
# while a < b:
#   print(a)
#   a += 1

# ex 10
# b = 10
# while b > 0:
#     if b%2 != 0:
#         print("impair")
#     else:
#         print("pair")
#     b = b-1

# ex 11
# check=True
# while check:
#     n = int(input("Entrez un nombre:"))
#     if 1 <= n <= 10:
#         print(n)
#         check = False
