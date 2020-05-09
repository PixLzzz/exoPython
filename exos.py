import math
import re
import sys

#EPISODE 2 :
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


# ex 12
# my_list = ["yaya","yoyo", "yeye"]
# for i in my_list:
#     print(i)

# ex 13

# for i in range(1,15):
#     if i%3==0:
#         print(i)

#ex 14

# n = int(input("n : "))
# i = 0
# while i < n:
#     i+=1
#     if i%2==0:
#       print(i)

# for r in range(1,n+1):
#     if r%2==0:
#         print(r)

#ex 15

# mliste = [17, 38, 10, 25, 72]
# mliste.sort()
# print(mliste)
# mliste.append(12)
# print(mliste)
# mliste.reverse()
# print(mliste)
# print(mliste.index(17))
# mliste.remove(38)
# print(mliste)
# print(mliste[1:3])
# print(mliste[:2])
# print(mliste[2:])
# print(set(mliste))

# ex 16
#s = "loup"
#print(s[::-1])

# ex 17
#a = "aza"
#b = a [:: -1]
#if a==b:
#    print("Est un palindrome")
#else:
#    print("No")

#18
#string = str(input("variable : "))
#
#if(re.search(r"^[^@]+@[^@]+\.[^@]+$",string)):  
#  print("ok")

#exerice 19
#truc = []
#print(truc)
#machin = ["0.0", "0.0", "0.0", "0.0", "0.0",]
#print(machin)

#exercice 20
#print(" ------ ")
#for x in range(0,4) :
#    print(x)
#print(" ------ ")
#for x in range(4,8) :
#    print(x)
#print(" ------ ")
#for x in range(2,9) :
#    print(x)
#print(" ------ ")

#chose = [0, 1, 2, 3, 4, 5]

#if 3 in chose :
#    print("3 is ok")
#else : 
#    print("3 is not ok")
#if 6 in chose : 
#    print("6 is ok")
#else : 
#    print("6 is not ok")

#ex21
#nbString = int(input("nb string : "))
#f = open("data.txt", "a+")
#for x in range(nbString):
#  temp = str(input("Mot : "))
#  f.write(temp)
#  f.write("\n")
#f.close()

#22
#f = open('data.txt')
#for line in f:
#  if(re.search(r"^[^@]+@[^@]+\.[^@]+$", str(line))):
#    print(line)
#f.close()

#23
#def compterMots(str):
#  count = dict()
#  words = str.split()
#  for word in words:
#      if word in count:
#          count[word] += 1
#      else:
#          count[word] = 1
#  return count

# ex 24

#r = int(sys.argv[1])
#pi = 3.1415926535897931
#V= 4.0/3.0*pi* r**3
#print('The volume of the sphere is: ',V," pour un rayon de ",r)

#exercice 25

#def somme(a, b, c) :
#    return print((a+b+c))

#montuple = (1, 2, 1)
#somme(montuple[0], montuple[1], montuple[2])




# Episode 3
#def converter(conversion):
#    euros = 0
#    aryAry = 0

#    if conversion[:2] == "AE":
#        print(float(conversion[3:])*aryAry)
#    elif conversion[:2] == "EA":
#        print(float(conversion[3:])*euros)

#converter("AE 4000")

#EPISODE 5 
#myList = ["\b\t80cm\t60cm\n" , "\b\t81cm\t51cm\n" , "\b\t105cm\t145cm\n" ]
#print(myList)

#for x in range(len(myList)) :
#  temp = re.findall(r'\d+', myList[x])
#  res = list(map(int, temp))
#  if res[0] < res[1] :
#    print(res[0])



