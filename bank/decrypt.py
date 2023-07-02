#! /usr/bin/python3.9
import sys
import os.path

                                #DECRYPT
                            #COPY PASTE BITCH
fBank = open("bank.txt", "rt")
sCode = fBank.read()
fBank.close()

sPlainText = ""

def ConvertChar(cChar) :
    return  chr(ord(cChar) - 13)

for i in range(1, len(sCode)+1) :
    cChar = sCode[i-1]
    sPlainText = sPlainText + ConvertChar(cChar)
fBank = open("bank.txt", "wt")
fBank.write(sPlainText)
fBank.close()

