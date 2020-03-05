# -*- coding: utf-8 -*-

import os
import time
from os import system, name 
import math
from random import randint

DIC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

def xgcd(number_x, number_y, return_x_and_y):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while number_x != 0:
        q, number_y, number_x = number_y // number_x, number_x, number_y % number_x
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    if return_x_and_y:
        return number_y, x0, y0
    else:
        return number_y

def is_prime(number, strength):
    if number == 2 or number == 3:
        return True
    if number <= 1 or number % 2 == 0:
        return False
    for i in range(0, strength):
        a = randint(1, number-1)
        if (pow(a, number-1, number) != 1):
            return False 
    return True

def random_number(length):
    range_start = 10**(length-1)
    range_end = (10**length)-1
    number = randint(range_start, range_end) | 1
    return number

def number_e(pi_n):
    number = 2
    while not (xgcd(number, pi_n, 0) == 1) and number < pi_n:
        number = randint(2, pi_n-1)
    return number

def inverse_multiplicative(number_e, number_pi):
    gcd, x, y = xgcd(number_e, number_pi, 1)
    if gcd == 1:
        return x % number_pi

def random_prime_number(length, strength):
    number = 4
    while not is_prime(number, strength):
        number = random_number(length)
    return number

def read_file(file_path):
    try:
        file = open(file_path, "r", encoding="ISO-8859-1")
        text = file.read()
        file.close()
        return text
    except FileNotFoundError:
        text = "fail"
        print ("")
        print ("NÃO FOI POSSÍVEL LER O ARQUIVO!")
        return text

def read_keys():
    i = 0
    first = 0
    text = read_file("Keys.txt")
    if text == "fail":
        return 0, 0
    number_e = ""
    number_n = ""
    while i < len(text):
        while i < len(text) and text[i] != '.':
            if first == 0:
                number_e += text[i]
                i += 1
            else:
                number_n += text[i]
                i += 1
        first = 1
        i += 1
    number_e = int(number_e)
    number_n = int(number_n)
    return number_e, number_n

def write_file(file_path, msg):
    try:
        file = open(file_path, "w", encoding="ISO-8859-1")
        file.write(msg)
        file.close()
    except FileNotFoundError:
        print("")
        print("NÃO FOI POSSÍVEL CRIAR O ARQUIVO!")

def encrypt(text, number_e, number_n):
    encrypt_text = ""
    for i in range(0, len(text)):
        letter = DIC.index(text[i])
        encrypt_text += str(pow(letter, number_e, number_n))
        if(i+1 != len(text)):
            encrypt_text += "."
    return encrypt_text

def decrypt(text, number_d, number_n):
    decrypt_text = ""
    i = 0
    while i < len(text):
        encrypted = ""
        while (i < len(text) and (48 <= ord(text[i]) <= 57)):
            encrypted += text[i]
            i += 1
        i += 1
        encrypted = int(encrypted)
        decrypt_text += DIC[pow(encrypted, number_d, number_n)]
    return decrypt_text

def clear(): 
	if name == 'nt': 
	    _ = system('cls') 
	else: 
	    _ = system('clear')

def header():
    print("*--------------------------------------------------------------------------------------------------*")                                                                                            
    print("|                                                                ,----..                           |")
    print("|   ,-.----.    .--.--.      ,---,                 ,----..     /   /   \      ,---,        ,---,.  |")
    print("|   \    /  \  /  /    '.   '  .' \               /   /   \   /   .     :   .'  .' `\    ,'  .' |  |")
    print("|   ;   :    \|  :  /`. /  /  ;    '.            |   :     : .   /   ;.  \,---.'     \ ,---.'   |  |")
    print("|   |   | .\ :;  |  |--`  :  :       \           .   |  ;. /.   ;   /  ` ;|   |  .`\  ||   |   .'  |")
    print("|   .   : |: ||  :  ;_    :  |   /\   \          .   ; /--` ;   |  ; \ ; |:   : |  '  |:   :  |-,  |")
    print("|   |   |  \ : \  \    `. |  :  ' ;.   :         ;   | ;    |   :  | ; | '|   ' '  ;  ::   |  ;/|  |")
    print("|   |   : .  /  `----.   \|  |  ;/  \   \        |   : |    .   |  ' ' ' :'   | ;  .  ||   :   .'  |")
    print("|   ;   | |  \  __ \  \  |'  :  | \  \ ,'        .   | '___ '   ;  \; /  ||   | :  |  '|   |  |-,  |")
    print("|   |   | ;\  \/  /`--'  /|  |  '  '--'          '   ; : .'| \   \  ',  / '   : | /  ; '   :  ;/|  |")
    print("|   :   ' | \.'--'.     / |  :  :                '   | '/  :  ;   :    /  |   | '` ,/  |   |    \  |")
    print("|   :   : :-'   `--'---'  |  | ,'                |   :    /    \   \ .'   ;   :  .'    |   :   .'  |")
    print("|   |   |.'               `--''                   \   \ .'      `---`     |   ,.'      |   | ,'    |")
    print("|   `---'                                          `---`                  '---'        `----'      |")
    print("*--------------------------------------------------------------------------------------------------*")
    print("*--------------------------------------------------------------------------------------------------*")

def menu():
    keys = 0
    start = 1
    p = 0
    q = 0
    n = 0
    pi_n = 0
    e = 0
    d = 0
    while start == 1:
        clear()
        header()
        if keys == 1:
            print("")
            print("KEYS GENERATED!")
            n = p*q
            pi_n = (p - 1)*(q - 1)
            if e == 0:
                e = number_e(pi_n)
            d = inverse_multiplicative(e, pi_n)
            text = str(e) + "." + str(n)
            write_file("Keys.txt", text)
        print("")
        print("CHOOSE AN OPTION: ")
        print("")
        print("GENERATE KEYS------[1]")
        print("ENCRYPT------------[2]")
        print("DECRYPT------------[3]")
        print("EXIT---------------[4]")
        print("")
        choice = eval(input("TYPE THE OPTION HERE: "))
        if choice == 1:
            clear()
            header()
            print("")
            print("CHOOSE AN OPTION: ")
            print("")
            print("GENERATE P & Q-------[1]")
            print("ENTER P, Q & E-------[2]")
            print("BACK-----------------[3]")
            print("")
            choice_1 = eval(input("TYPE THE OPTION HERE: "))
            if choice_1 == 1:
                clear()
                header()
                print("")
                length = eval(input("ENTER THE QUANTITY OF DIGITS FOR P & Q: "))
                p = random_prime_number(length, 128)
                q = random_prime_number(length, 128)
                pi_n = (p - 1)*(q - 1)
                e = number_e(pi_n)
                print("")
                print ("P:")
                print (p)
                print ("Q:")
                print (q)
                print ("E:")
                print (e)
                print("")
                skip = input("SAVE THE KEYS AND PRESS ENTER: ")
                keys = 1
            if choice_1 == 2:
                p_isprime = 0
                q_isprime = 0
                e_iscoprime = 0
                while p_isprime == 0:
                    clear()
                    header()
                    print("")
                    p = eval(input("ENTER P: "))
                    if is_prime(p, 128):
                        p_isprime = 1
                    else:
                        print("")
                        print("P IS NOT PRIMAL!")
                        time.sleep(1)
                while q_isprime == 0:
                    clear()
                    header()
                    print("")
                    q = eval(input("ENTER Q: "))
                    if is_prime(q, 128):
                        q_isprime = 1
                    else:
                        print("")
                        print("Q IS NOT PRIMAL!")
                        time.sleep(1)
                pi_n = (p - 1)*(q - 1)
                while e_iscoprime == 0:
                    clear()
                    header()
                    print("")
                    e = eval(input("ENTER E: "))
                    if xgcd(e, pi_n, 0) == 1 and e > 1:
                        e_iscoprime = 1
                    else:
                        print("")
                        print("E IT IS NOT COPRIME OF FI!")
                        time.sleep(1)
                keys = 1
            if choice_1 == 3:
                clear()
        if choice == 2:
            clear()
            header()
            print("")
            print("CHOOSE AN OPTION: ")
            print("")
            print("TYPE TEXT-----------[1]")
            print("CHOOSE FILE---------[2]")
            print("BACK----------------[3]")
            print("")
            choice_2 = eval(input("TYPE THE OPTION HERE: "))
            if choice_2 == 1:
                clear()
                header()
                print("")
                text = input("TYPE TEXT: ")
                if keys == 1:
                    write_file("Encrypted.txt", encrypt(text, e, n))
                    print("")
                    print("SAVED FILE!")
                    time.sleep(2)
                else:
                    e, n = read_keys()
                    if e == 0 and n == 0:
                        print("")
                        print("CREATE A KEY!")
                        time.sleep(2)
                    else:
                        write_file("Encrypted.txt", encrypt(text, e, n))
                        print("")
                        print("SAVED FILE!")
                        time.sleep(2)
            if choice_2 == 2:
                clear()
                header()
                print("")
                text = input("TYPE THE FILE NAME: ")
                if keys == 1:
                    write_file(text, encrypt(read_file(text), e, n))
                    print("")
                    print("SAVED FILE!")
                    time.sleep(2)
                else:
                    e, n = read_keys()
                    if e == 0 and n == 0:
                        print("")
                        print("CREATE A KEY!")
                        time.sleep(2)
                    else:
                        write_file(text, encrypt(read_file(text), e, n))
                        print("")
                        print("SAVED FILE!")
                        time.sleep(2)
            if choice_2 == 3:
                clear()
        if choice == 3:
            clear()
            header()
            print("")
            print("CHOOSE AN OPTION: ")
            print("")
            print("CHOOSE FILE-------[1]")
            print("BACK--------------[2]")
            print("")
            choice_3 = eval(input("TYPE THE OPTION HERE: "))
            if choice_3 == 1:
                clear()
                header()
                print("")
                text = input("TYPE THE FILE NAME: ")
                if keys == 1:
                    write_file(text, decrypt(read_file(text), d, n))
                    print("")
                    print("SAVED FILE!")
                    time.sleep(2)
                else:
                    print("")
                    p = eval(input("ENTER THE P VALUE: "))
                    q = eval(input("ENTER THE Q VALUE: "))
                    e = eval(input("ENTER THE E VALUE: "))
                    n = p*q
                    pi_n = (p - 1)*(q - 1)
                    d = inverse_multiplicative(e, pi_n)
                    write_file(text, decrypt(read_file(text), d, n))
                    print("")
                    print("SAVED FILE!")
                    time.sleep(2)
            if choice_3 == 2:
                clear()
        if choice == 4:
            clear()
            start = 0

menu()