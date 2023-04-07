import pandas as pd
import numpy as np
import sys

castList = []
cleanedCast = []
file_name = "example1.csv"

#reading the csv file having cast data
try:
    myfile = pd.read_csv(file_name)
    print("Reading "+file_name+" .....")
except OSError:
    print("File not found !!")
    sys.exit()
#Data cleaning (removing nan values)
for files in myfile:
    if str(files) != "nan": 
        castList.append(myfile[files].tolist())
cleanedCast = [list(filter(lambda x:x == x, y)) for y in castList]
print("*****************Cast List*****************")
print(cleanedCast)

cast0 = cleanedCast[0]
cast1 = cleanedCast[1]
flag = 0
print("********************************************************************")
#if connection = 1 checking in cast0 and cast1 
for each_cast in cleanedCast[0]:
    for each_cast1 in cleanedCast[1]:
        if each_cast == each_cast1:
            print("Shortest Connection = 1, Actor = ",each_cast )
            flag = 1

#If there is no connection = 1 then this loop exists and checks for conneciton = 2
if flag == 0:
    for each_cast in cast0:
        for i in range(0, len(cleanedCast)):
            for j in cleanedCast[i]:
                if each_cast in cleanedCast[i]:
                    for each_cast1 in cast1:
                        if each_cast1 == j:
                            print("Shortest Connection = 2, Cast = ", cleanedCast[i]) 
                            flag = 1
#if connection>2 or no connection
if flag == 0:
    print("Connection > 2 or no connection.")