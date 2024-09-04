# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 06:38:25 2015

@author: IsmailGhodsollahee
"""

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
    #for i in range(len(listOfList[0][2])):
    #    listOfFiles.append(path+'\\'+listOfList[0][2][i])
    return listOfList

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
