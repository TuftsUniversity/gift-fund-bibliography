import sys
import requests
import json
import os
import csv
import re
from tkinter.filedialog import askopenfilename
from django.utils.encoding import smart_bytes
# import ntpath
#for dataframes
import pandas as pd
import numpy as np


import time

def parseCreatorList(cList, relator):
    count = len(cList)
    x = 0
    creatorLine = ""
    while x < count and x < 3:



        #print("Creator: " + cList[x] + "; counter: " + str(x) + "; Count: " + str(len(cList)) + "\n")

        # try:
        #

        #print("Relator: " + relator + "\n")
        if "author" in relator:
            #print("In author loop\n")
            if x == 0 and count == 1:
                creatorLine += "\tauthor = {" + cList[x] + "}"
                break
            elif x == 0 and count > 1:
                creatorLine += "\tauthor = {" + cList[x]
            elif 0 < x < 2 and count > 2:
                creatorLine += " and " + cList[x]
            else:
                creatorLine += " and " + cList[x] + "}"
        elif "editor" in relator:
            #print("In editor loop\n")
            if x == 0 and count == 1:
                creatorLine += "\teditor = {" + cList[x] + "}"
                break
            elif x == 0 and count > 1:
                creatorLine += "\teditor = {" + cList[x]
            elif 0 < x < 2 and count > 2:
                creatorLine += " and " + cList[x]
            else:
                creatorLine += " and " + cList[x] + "}"
        elif "translator" in relator:
            #print("In transalator loop\n")
            if x == 0 and count == 1:
                creatorLine += "\ttranslator = {" + cList[x] + "}"
                break
            elif x == 0 and count > 1:
                creatorLine += "\ttranslator = {" + cList[x]
            elif 0 < x < 2 and count > 2:
                creatorLine += " and " + cList[x]
            else:
                creatorLine += " and " + cList[x] + "}"
        #if it's uncaught relator
        else:
            #print("In uncaught relator loop\n")
            if x == 0 and count == 1:
                creatorLine += "\tauthor = {" + cList[x] + "}"
                break
            elif x == 0 and count > 1:
                creatorLine += "\tauthor = {" + cList[x]
            elif 0 < x < 2 and count > 2:
                creatorLine += " and " + cList[x]
            else:
                creatorLine += " and " + cList[x] + "}"
        #if there's no relator
        # except:
        #     #print("In no relator loop\n")
        #     if x == 0 and count == 1:
        #         creatorLine += "\tauthor = {" + cList[x] + "}"
        #         break
        #     elif x == 0 and count > 1:
        #         creatorLine += "\tauthor = {" + cList[x]
        #     elif 0 < x < count - 1 and count < 3:
        #         creatorLine += " and " + cList[x]
        #     else:
        #         creatorLine += " and " + cList[x] + "}"
        x += 1

    return creatorLine
def parseCreator(c, cR):
    creatorFlag = False
    relatorFlag = False

    if c != "":
        cList = c.split(";")
        creatorFlag = True
    else:
        creatorFlag = False
    if cR != "":
        cRList = cR.split(";")
        relatorFlag = True
    else:
        relatorFlag = False

    if relatorFlag:
        del cRList[-1]
    if creatorFlag:
        del cList[-1]

    authorList = []
    editorList = []
    translatorList = []
    y = 0
    nullVariable = ""
    if creatorFlag == True:
        for creator in cList:


            if cList[y][-1] == "," or cList[y][-1] == ".":
                cList[y] = cList[y][:-1]

            nullVariable = "+"
            cList[y] = re.sub(r'([^,.]+?)[,.]\W(.+),?', r'\2 \1', str(cList[y]))
            creator = cList[y]
            #if relatorFlag:
            if relatorFlag == True:
                try:
                    relator = cRList[y]
                    if "author" in relator:
                        authorList.append(creator)
                    elif "editor" in relator:
                        editorList.append(creator)
                    elif "translator" in relator:
                        translatorList.append(creator)
                except:
                    authorList.append(creator)
            else:
                authorList.append(creator)
            #else:
                #authorList.append(creator)
            y += 1
        # this is because the semicolon follows every entry in the string/list, even
        # the last one, so this deletes the last element in the list



    returnCreator = ""

    authorLine = ""
    editorLine = ""
    translatorLine = ""


    if len(authorList) > 0:
        authorLine = parseCreatorList(authorList, "author")
    if len(editorList) > 0:
        editorLine = parseCreatorList(editorList, "editor")
    if len(translatorList) > 0:
        translatorLine = parseCreatorList(translatorList, "translator")

    if authorLine != "":
        returnCreator += authorLine + ",\n"
    if editorLine != "":
        returnCreator += editorLine  + ",\n"
    if translatorLine != "":
        returnCreator += translatorLine + ",\n"
    return returnCreator

def parsePublication(a1, a2, a3, b1, b2, b3):
    address = ""
    publisher = ""
    year = ""


    if a2 != "":
        a2 = a2.split(";")
        a2String = str(a2[0])
        a2String = re.sub(r',$', '', str(a2String))
        if a1 != "":
            a1 = a1.split(";")
            a1String = str(a1[0])
            a1String = re.sub(r'\s+\:.*$', '', str(a1String))
            address = "\taddress = {" + str(a1String) + "},\n"
            publisher = "\tpublisher = {" + str(a2String) + "},\n"
            if a3 != "":
                a3 = a3.split(";")
                a3String = str(a3[0])
                a3String = re.sub(r'.*(\d{4}).*', r'\1', str(a3String))
                a3String = re.sub(r'[\[\]]', '', str(a3String))
                year = "\tyear = {" + str(a3String) + "},\n"

    elif b2 != "":
        b2 = b2.split(";")
        b2String = str(b2[0])
        b2String = re.sub(r'\s\:.*$', '', b2String)
        b2String = re.sub(r',$', '', b2String)
        if b1 != "":
            b1 = b1.split(";")
            b1String = str(b1[0])
            b1String = re.sub(r'\s+\:.*$', '', b1String)
            address = "\taddress = {" + str(b1String) + "},\n"
            publisher = "\tpublisher = {" + str(b2String) + "},\n"
            if b3 != "":
                b3 = b3.split(";")
                b3String = str(b3[0])
                b3String = re.sub(r'.*(\d{4}).*', r"\1", b3String)
                b3String = re.sub(r'[\[\]]', '', b3String)
                year = "\tyear = {" + str(b3String) + "},\n"

    return address + publisher + year
