# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:27:20 2022

@author: IsmailGhodsollahee
"""


DrugNum=482
K=open("DrugFeatureSet.csv","r",encoding='utf8')           
content=K.readline()
Category=content.strip().split(",");
content=K.readline()
Benefits=content.strip().split(",");
content=K.readline()
SideEffects=content.strip().split(",");

Temp=[]
Temp.append("DrugName")
for i in range(0,len(Category)):
    Temp.append(Category[i])
for i in range(0,len(Benefits)):
    Temp.append(Benefits[i])
for i in range(0,len(SideEffects)):
    Temp.append(SideEffects[i])
Features=[]
Features.append(Temp)

for i in range(0,DrugNum):
    Features.append(['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
    
K=open("Dataset.csv","r",encoding='utf8') 
SizeofDataset=0;
content=K.readline()
cont=content.strip().split(",");
SizeofDataset=cont[0]
TxtBenefits=""
Dnumfound=0

Chars=K.readline();
Chars=K.readline();
for i in range(2,int(SizeofDataset)+2):
    Chars=K.readline();
    cont=Chars.strip().split(",");
    DName=cont[6]
    DCate=cont[7].split(' ')
    new=1
    print(i/int(SizeofDataset)*100)
    for j in range(1,DrugNum):
        if DName==Features[j][0]:
            new=0
            """for m in range(0, len(DCate)-1):
                for n in range(1, len(Category)):
                    if DCate[m]==Features[0][n]:
                        Features[j][n]=1"""
    if new==1:
        Dnumfound=Dnumfound+1
        Features[Dnumfound][0]=DName
        for m in range(0, len(DCate)-1):
            for n in range(1, len(Category)):
                if DCate[m]==Features[0][n]:
                    Features[Dnumfound][n]=1
        
K.close()


import DrugFeatureLib as DI
import os
listOfSides=[]
listDr=DI.drugMapper("druglist.txt")

n=0
for i in range(len(listDr)):
    listOfList=[]
    DoThing=0
    if len(listDr[i])>2:
        for files in os.walk("SaveAddress"+listDr[i][2]):
            listOfList.append(files)
        n=n+1

        DrName=str(listDr[i][1]).replace(' ','')
        for j in range(0,DrugNum):
            if DrName==str(Features[j][0]).replace(' ',''):
                DrDnamNum=j
                DoThing=1
                break
    if DoThing==1:
        if len(listOfList)>0:
            if len(listOfList[0])>0:
                for m in range(len(listOfList[0][1])-1):
                    for n in range(len(Benefits)+len(Category),len(Benefits)+len(Category)+len(SideEffects)):
                        if Features[0][n]==listOfList[0][1][m]:
                            Features[DrDnamNum][n]=1
                            print(DrDnamNum,n,DrName)

K=open("Dataset.csv","r",encoding='utf8') 
SizeofDataset=0;
content=K.readline()
cont=content.strip().split(",");
SizeofDataset=cont[0]
TxtBenefits=""
for i in range(1,int(SizeofDataset)+3):
    Chars=K.readline();
    cont=Chars.strip().split(",");
    TxtBenefits=cont[11].split(' ')
    DName=cont[6].replace(' ','')
    
    for j in range(0,DrugNum):
        if DName==str(Features[j][0]).replace(' ',''):
            DrDnamNum=j
            DoThing=1
            break
            
    for m in range(0,len(TxtBenefits)):
        for n in range(len(Category),len(Benefits)+len(Category)):
            if TxtBenefits[m]==Features[0][n]:
                Features[DrDnamNum][n]=1
                print(DrDnamNum,n,DName)
    
K.close()                 

K=open("DruSet.csv","w",encoding='utf8') 
for i in range(0,DrugNum):
    Temp=str(Features[i][0])+","
    for j in range(0,len(Features[0])-1):
        Temp=Temp+str(Features[i][j])+","
    Temp=Temp+str(Features[i][j])+"\n"
    K.writelines(Temp)
    
K.close()