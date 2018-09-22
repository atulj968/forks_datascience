#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:04:52 2018

@author: atuljain
"""

import urllib2


wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

page = urllib2.urlopen(wiki)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page)

all_tables = soup.find_all('table')

right_table = soup.find('table', class_ = 'table')

A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==5:
     A.append(cells[0].find(text = True))
     B.append(cells[1].find(text = True))
     C.append(cells[2].find(text = True))
     D.append(cells[3].find(text = True))
     E.append(cells[4].find(text = True))
    
    
import pandas as pd
df = pd.DataFrame(A,columns=['Pos'])
df['Team']=B
df['Mateches']=C
df['Pointsts']=D
df['Rating']=E

print df