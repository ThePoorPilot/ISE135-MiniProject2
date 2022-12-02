#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:43:54 2022

@author: michael
"""
from itertools import combinations
import pandas as pd

#input text files toggle (comment out and enable correct files)

#Michael Monaco
projectData1="/home/michael/Documents/projectData1.txt"
projectData2="/home/michael/Documents/projectData2.txt"


infile=open(projectData1, "r")

projectdata=[line for line in infile.readlines()]

#Convert to dictionary(for human readable purposes)
projectdict={}
i=0
for line in projectdata:
    key=i
    i=i+1
    
    (factory, cost, N1, N2, N3, N4, N5, N6, N7, N8, N9, N10)=line.rstrip().split(",")
    variables=(factory, cost)
    #convert neighborhhod coverage to list
    #there might be a better way to do the eval
    ncoverage=(eval(N1), eval(N2), eval(N3), eval(N4), eval(N5), eval(N6), eval(N7), eval(N8), eval(N9), eval(N10))
    
    projectdict.setdefault(key,{})["factory"]=factory
    projectdict.setdefault(key,{})["cost"]=eval(cost)
    projectdict.setdefault(key,{})["ncoverage"]=ncoverage

infile.close()

#list of coverage tuples for all possible combinations
posscovlists=[]
#for final determination
combolist=[]
for i in range(11):
    for combo in combinations(range(10), i):
        #make list of ncoverage lists for combo
        combolist.append(combo)
        comboncoverage=[]
        for factorynum in combo:
            comboncoverage.append(projectdict[factorynum]["ncoverage"])
        posscovlists.append(comboncoverage)

find=-1
foundlist=[]
#possibilty: list of tuples
for possibility in posscovlists:
    find=find+1
    #go through each neighborhood
    for i in range(10):
        found=True
        numsum=[]
        for test in range(len(possibility)):
            numsum.append(possibility[test][i])
        if sum(numsum)<1:
            found=False
            break
    if found==True:
        foundlist.append(find)


#find least expensive option
costsums=[]
for num in foundlist:
    costs=[]
    converttocombo=combolist[num]
    for i in converttocombo:
        costs.append(projectdict[i]["cost"])
    costsums.append(sum(costs))

lowestcost=-1
#print minmum
for costsum in costsums:
    lowestcost=lowestcost+1
    if costsum==min(costsums):
        break

for factory in combolist[foundlist[lowestcost]]:
    print(projectdict[factory]["factory"], end=" ")

print("\n"+"\n"+"Lowest cost is ${0:.2f} Million".format(min(costsums)))




