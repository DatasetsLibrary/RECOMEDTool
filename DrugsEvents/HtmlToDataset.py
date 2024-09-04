# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:40:14 2021

@author: IsmailGhodsollahee
"""
import DatLib as DL
def EventAnalyser(FileName,debug):
    f=open(FileName,"r",encoding='utf8',errors='surrogateescape')
    endoffile=0
    NumberofEvent=0;
    count=0;
    while endoffile<1:
        content=f.readline() 
        if debug>0:
            count=count+1
            print(count,NumberofEvent)
              
        if len(content)>0:
            if "<b>Patient:" in content and "year old" in content:
                NumberofEvent=NumberofEvent+1;
            if "</html>" in content:
                endoffile=1
        
    print(NumberofEvent)
    Temp= [[(i,j) for j in range(6)] for i in range(NumberofEvent)]           
    f.close();
    
    if NumberofEvent>0:
        f=open(FileName,"r",encoding='utf8',errors='surrogateescape')
        endoffile=0
        EventN=-1;
        DrugName=""
        while endoffile<1:
            content=f.readline()
            #print(content)
            if len(content)>0:
                if "<b>Patient:" in content and "year old" in content:
                    EventN=EventN+1
                    Temp[EventN][0]=DrugName
                    Temp[EventN][4]=""
                    Temp[EventN][5]=""
                    cont=content.strip().split(" ");
                    for i in range(1,len(cont)):
                        if "year" in cont[i]:
                            effestr="";
                            ti=i-1;
                            while ti>0:
                                effestr=cont[ti]+effestr;
                                if "year" in cont[ti]:
                                    ti=0
                                ti=ti-1; 
                            Temp[EventN][1]=effestr
                        if "male" in cont[i]:
                            Temp[EventN][2]="male"
                        if "female" in cont[i]:
                            Temp[EventN][2]="female"
                if "Reactions:</b>" in content:
                    cont=content.strip().split(" ");
                    effestr="";
                    for i in range(1,len(cont)):
                        effestr=effestr+" "+cont[i]
                    Temp[EventN][3]=effestr
                if "Adverse event resulted in:</b>" in content:
                    cont=content.strip().split(" ");
                    effestr="";
                    for i in range(4,len(cont)):
                        effestr=effestr+" "+cont[i]
                    Temp[EventN][4]=effestr
                if "Other drugs received by patient:</b>" in content:
                    cont=content.strip().split(" ");
                    effestr="";
                    for i in range(5,len(cont)):
                        effestr=effestr+" "+cont[i]
                    Temp[EventN][5]=effestr
                
                if "<title>" in content:
                    cont=content.strip().split(" ");
                    DrugName=cont[0].strip("<title>")
                if "</html>" in content:
                    endoffile=1
    return Temp         
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


path="D:\DrugSetNee\DrugsEvents\Druglib"
listOfFiles=FileListExtractor(path)
Events=list()
Temp=["DrugName","Age","Genius","Reactions","Advent Event","Other Drug"]
Events.append(Temp)
for i in range(len(listOfFiles)):
    print(listOfFiles[i])
    T=EventAnalyser(listOfFiles[i],0)
    for j in range(len(T)):
        Events.append(T[j])
        
        
def DatasetEventSaver(FileNameNew,Temp):
    ReviewN=len(Temp)
    D=open(FileNameNew,"w",encoding='utf8')
    strText=""
    for j in range(ReviewN):    
        strText=str(Temp[j][0])
        for i in range(0,6):
            Tempstr=str(Temp[j][i]).replace(',',';')
            try:
                D.writelines(Tempstr+",");
            except:
                D.writelines(" ,");
        D.writelines(Temp[j][i]+"\n");
    D.close(); 

DatasetEventSaver("Events.csv",Events)
DL.SaveDat("Events.DAT","Array",2487,6,Events)