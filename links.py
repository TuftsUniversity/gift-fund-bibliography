#!/usr/bin/env python3
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
########
########
########    Author:           Henry Steele, Library Technology Services, Tufts University
########    Name of Program:  Links
########	Files:			  links.py
########    Date created:     2019-06
########
########    Purpose:
########      - using a CSV file from Analytics of MMS IDs, fund codes, and the IEP that relates Alma records to Primo records, export a list of
########        Primo links that can be used in the gift fund section of library websites.  It has to merge this with a list of MMS IDs and
########        fund codes from Titles Purchased with Gift Funds - MMS and Fund to get the fund code
########      - The Analtyics report uses MMS Ids from Titles Purchased with Gift Funds - MMS and Fund as a filter
########

import sys
import requests
import json
import os
import csv
import re
from tkinter.filedialog import askopenfilename
# from django.utils.encoding import smart_str, smart_unicode
# import shutil as shu
# import subprocess
# import ntpath
#for dataframes
import pandas as pd
import numpy as np

iep_filename = askopenfilename(title = "Select CSV containing Gift Fund records with MMS Id and IEP")
gift_filename = askopenfilename(title = "Select CSV .csv file containing titles with gift funds data")

iep_df = pd.read_csv(iep_filename, encoding='utf-8', dtype={'MMS Id': 'str', 'Item Id': 'str', 'IEP': 'str'})
fund_df = pd.read_csv(gift_filename, encoding='utf-8', dtype={'MMS Id': 'str', 'Item Id': 'str', 'IEP': 'str'})

df = pd.merge(iep_df, fund_df, on='MMS Id')

oDir = "./Output"
if not os.path.isdir(oDir) or not os.path.exists(oDir):
       os.makedirs(oDir)

#output_file = open(oDir + "/Primo Links for Website.txt")

link_prefix = "https://tufts-primo.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=01TUN_ALMA"

link_suffix = "&context=L&vid=01TUN&search_scope=EVERYTHING&tab=everything&lang=en_US"

df['Link'] = df['IEP'].apply(lambda x: link_prefix + str(x) + link_suffix)

df.to_excel(oDir + "/Titles with Links to Primo.xlsx", index=False)
