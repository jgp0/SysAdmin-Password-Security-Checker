from random import *
import os

u_pwd = input("Introduce una contraseña: ")
pwd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','ñ','Ñ','0','1','2','3','4','5','6','7','8','9','`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[','{',']','}','\\','|',';',':','"',',','<','.','>','/','?']

pw=""
while(pw!=u_pwd):
    pw=""
    for letter in range(len(u_pwd)):
      guess_pwd = pwd[randint(0,17)]
      pw=str(guess_pwd)+str(pw)
      print(pw)
      print("Resolviendo contraseña")
      os.system("cls")
print("La contraseña es: ",pw)