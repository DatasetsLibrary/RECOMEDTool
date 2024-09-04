# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 06:38:25 2015

@author: IsmailGhodsollahee
"""
import numpy as np
#function of mapping drug list of druglib with drug interaction site

def drugMapper(FileName):
    f=open(FileName,"r")
    endoffile=0     
    drugMapper=[]
    n=0
    while endoffile<1:
        n=n+1
        print(n)
        content=f.readline()
        if "->" in content:
            ti=len(content)
            while ti>0:
                ti=ti-1
                if content[ti]==">":
                    PointSplitter=ti
                    break
            Dru1=content[0:PointSplitter-2]
            Dru2=content[PointSplitter+1:len(content)-1]
            #print(n,Dru1,Dru2)
            drugMapper.append([n-1,Dru1,Dru2])
        elif "*****" in content:
            ti=len(content)
            pi=0
            while ti>pi:
                pi=pi+1
                if content[pi]=="*":
                    PointSplitter=pi
                    break
            Dru1=content[0:PointSplitter]
            Dru2="-@_@-"
            #print(Dru1,Dru2)
            drugMapper.append([Dru1,Dru2])
        elif "$$$" in content:
            endoffile=1
        else:
            break
            print("the data set have incorrect form of data")
    return(drugMapper)

#function for extracting files in a directory        
def FileListExtractor(path):
    import os
    listOfFiles=[]
    listOfList=[]
    for files in os.walk(path):
        listOfList.append(files)
    for i in range(len(listOfList[0][2])):
        listOfFiles.append(path+'\\'+listOfList[0][2][i])
    return listOfFiles

def InterExtraxtor(contentt):
    ti=len(contentt)
    StartSplitter=0
    while ti>0:
        ti=ti-1
        if contentt[ti-2]=="<" and contentt[ti-1]=="/" and contentt[ti]=="a":
            EndSplitter=ti
        elif contentt[ti-1]=='"' and contentt[ti]==">":
            StartSplitter=ti
            break
    return contentt[StartSplitter+1:EndSplitter- 2]

# function that wxtract the incosisteancy of drugs        
def InteractonofADrug(File):
    f=open(File,"r")
    endoffile=0     
    n=0
    drugInteraction=[]
    while endoffile<1:
        n=n+1
        content=f.readline()
        if "<h1>" in content:
            ti=len(content)
            while ti>0:
                ti=ti-1
                if content[ti]=="<":
                    PointSplitter=ti
                    break
            DrugName=content[4:PointSplitter-13]
            print(DrugName)
            drugInteraction.append([DrugName,[],[],[],[],[],[]])
        elif "interactions</h2>" in content:# or "names.<span>" in content
            print("Drug",n)
            endofintruct=0
            while endofintruct<1:
                contentt=f.readline()
                if "int_1" in contentt:
                    nn=InterExtraxtor(contentt)
                    drugInteraction[len(drugInteraction)-1][1].append(nn)
                elif "int_2" in contentt:
                    nn=InterExtraxtor(contentt)
                    drugInteraction[len(drugInteraction)-1][2].append(nn)
                elif "int_3" in contentt:
                    nn=InterExtraxtor(contentt)
                    drugInteraction[len(drugInteraction)-1][3].append(nn)
                elif "interactions</h3>" in contentt:
                    endofintruct=1
        elif "food" in content and "interactions</a>" in content:
            pass 
        elif "disease" in content and "interactions</h3>" in content:
            print("Deseas",n)
            endofintruct=0
            while endofintruct<1:
                contentt=f.readline()
                if "int_1" in contentt:
                    nn=InterExtraxtor(contentt)
                    drugInteraction[len(drugInteraction)-1][3].append(nn)
                elif "int_2" in contentt:
                    nn=InterExtraxtor(contentt)
                    drugInteraction[len(drugInteraction)-1][4].append(nn)
                elif "int_3" in contentt:
                    nn=InterExtraxtor(contentt)
                    drugInteraction[len(drugInteraction)-1][5].append(nn)
                elif "Related treatment guides</h3>" in contentt:
                    endofintruct=1
        elif "<h4>Drug" in content:
            endoffile=1
    return drugInteraction

def IntractionMatrixCreator(listDrugMap,ListFiles):
    interactionOfDrugs=[]
    Si=len(ListFiles)
    for i in range(Si):
        print((i/Si)*100,"% completed")
        print(ListFiles[i])
        ListDrug=InteractonofADrug(ListFiles[i])
        interactionOfDrugs.append(ListDrug)
    interactionMatrix=[]
    listDrug=[]
    for i in range(0,(len(interactionOfDrugs)-1)):
        listDrug.append(interactionOfDrugs[i][0][0])
    interactionMatrix.append(listDrug)
    for i in range(0,len(listDrug)-1):  
        tempList=[]      
        tempList.append(listDrug[i]);
        for j in range(0,len(listDrug)-1): 
            tempList.append("")
        ms=len(interactionOfDrugs[i][0][1]);
        ns=len(interactionOfDrugs[i][0][2])
        os=len(interactionOfDrugs[i][0][3])
        for j in range(0,len(listDrug)-1): 
            for m in range(0,ms):
                if listDrug[j]==interactionOfDrugs[i][0][1][m]:
                    tempList[j]="major"
            for n in range(0,ns):
                if listDrug[j]==interactionOfDrugs[i][0][2][n]:
                    tempList[j]="moderate"
            for o in range(0,os):
                if listDrug[j]==interactionOfDrugs[i][0][3][o]:
                    tempList[j]="minor"
        interactionMatrix.append(tempList)
    return interactionMatrix
