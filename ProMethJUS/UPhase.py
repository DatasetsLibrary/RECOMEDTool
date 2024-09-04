# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 03:39:05 2021

@author: IsmailGhodsollahee
"""
"""
UsFact
"""

import numpy as np
import math as ma
from random import random,randint
import matplotlib.pyplot as plt
import DatLib as DL

SizeOfDatast=1073
NumberofDrug=480
TrainSize=500
LatentFactor=6
FeatureNum=370

cluster=DL.LoadDat("DATS/cluster.DAT", 40, LatentFactor-1)
DrugMat=DL.LoadDat("DATS/DrugMat.DAT", LatentFactor, NumberofDrug) 
CRatingMat=DL.LoadDat("DATS/CRatingMatEmp.DAT", 40, NumberofDrug)

for i in range(len(CRatingMat)):
    for j in range(len(CRatingMat[0])):
        CRatingMat[i][j]=float(CRatingMat[i][j])

def Normalize(OrginalRatingMat):
    Rmax=np.zeros(len(OrginalRatingMat))
    for i in range(0,len(OrginalRatingMat)):
        Rmax[i]=max(OrginalRatingMat[i])
    Rmaxx=max(Rmax)
    for i in range(0,len(OrginalRatingMat[0])):
        for j in range(0,len(OrginalRatingMat)):
            if OrginalRatingMat[j][i]>0:
                OrginalRatingMat[j][i]= OrginalRatingMat[j][i]/Rmaxx
    return Rmaxx,OrginalRatingMat

def Cost(cluster,Population,CRatingMat,NumberLatentFactor):
    HiP=Population.shape[1]
    HiD=CRatingMat.shape[1]
    CostR=np.zeros(shape=(HiD,HiP))
    CDrugR=np.zeros(shape=(NumberLatentFactor))  

    for m in range(0,HiP):
        for j in range(0,HiD):
            CDrugR=Population[0,m,j,:]
            for i in range(0,NumberLatentFactor):
                CUser=cluster[i,:]
                if (CRatingMat[i,j])>0:
                    CostR[j,m]=CostR[j,m]+abs(CRatingMat[i,j]-np.dot(CUser,np.transpose(CDrugR)))
    return(CostR)

def NonDominateSorting(Pop,CostR,CoefR):
    for i in range(0,CostR.shape[0]):
        for j in range(0,CostR.shape[1]):
            Minn=1000000;MinIndex=0
            for jm in range(j,CostR.shape[1]):
                cc=ma.pow(CoefR*CostR[i,jm],2)
                if cc < Minn:
                    Minn=cc
                    MinIndex=jm
            Temp=CostR[i,j];CostR[i,j]=CostR[i,MinIndex];CostR[i,MinIndex]=Temp;
            for m in range(0,Pop.shape[3]):
                Temp=Pop[:,j,i,m]
                Pop[:,j,i,m]=Pop[:,MinIndex,i,m]
                Pop[:,j,i,m]=Temp
    return Pop,CostR

def SelectionElimination(Pop,EleminationFactor,GenerationFactor,MutationFactor):
    SelectionSize=ma.floor(Pop.shape[1]*EleminationFactor)
    GenerationSize=ma.floor(Pop.shape[1]*GenerationFactor)
    for i in range(0,Pop.shape[0]):
        for j in range(0,Pop.shape[1]):
            if j==0:
                """a=1"""
            elif j<SelectionSize+GenerationSize and j>SelectionSize:
                DoMutation=int(random()*2*MutationFactor)
                if DoMutation==1:
                    place=randint(0,Pop.shape[2]-1)
                    place2=randint(0,Pop.shape[3]-1)
                    Pop[i,j,place,place2]=random()
            elif j<SelectionSize:
                parent1=randint(0,Pop.shape[1]-SelectionSize-GenerationSize-1)
                parent2=randint(0,Pop.shape[1]-SelectionSize-GenerationSize-1)
                FactorofParent=randint(0,Pop.shape[2]-1)
                for n in range(0,Pop.shape[2]):
                    if n<FactorofParent:
                        Pop[i,j,n,:]= Pop[i,parent1,n,:]
                    else:
                        Pop[i,j,n,:]= Pop[i,parent2,n,:]
            else:
                for n in range(0,Pop.shape[2]):
                    for m in range(0,Pop.shape[3]):
                        Pop[i,j,n,m]=random();
    return Pop


def InitialPopulation(OutputSize,cluster,NumPopulationForEachCluster,GenSize):
    Pop=np.zeros(shape=(OutputSize,NumPopulationForEachCluster,CRatingMat.shape[1],GenSize))
    for m in range(0,OutputSize):
        for n in range(0,CRatingMat.shape[1]):
            for i in range(0,NumPopulationForEachCluster):
                for j in range(0,GenSize):
                    Pop[m,i,n,j] = random()    
    return Pop


Rmaxx,CRatingMat=Normalize(CRatingMat)
LatentFactors=5
Pop=InitialPopulation(3,cluster,10,LatentFactors)  

IterationNumber=500;
it=0
history=np.zeros(shape=(IterationNumber,3))
CostR=Cost(cluster,Pop,CRatingMat,LatentFactors)
sizecost=CostR.shape[0];
while (it<IterationNumber-1):  
    CostR=Cost(cluster,Pop,CRatingMat,LatentFactors)
    Pop,CostR=NonDominateSorting(Pop,CostR,2)
    history[it,0]=sum(CostR[:,0])/sizecost;
    Pop=SelectionElimination(Pop,0.3,0.3,2)#EleminationFactor+GenerationFactor must be less than 1
    it=it+1;print(it,sum(CostR[:,0]))

    
plt.plot(history[1:IterationNumber-1,0],label="Absolute Error of 500 epochs");
plt.legend(loc=2, ncol=2)
plt.savefig('Rating.png', dpi=300)

sizecluster=cluster.shape[0];
CUser=np.zeros(shape=(sizecluster,LatentFactors))
CDrug=np.zeros(shape=(3,LatentFactors,CRatingMat.shape[1]))
for j in range(0,sizecluster):
    for m in range(0,LatentFactors):
        CUser[j,m]=cluster[j,m]
for j in range(0,CRatingMat.shape[1]):
    for m in range(0,LatentFactors):
        CDrug[:,m,j]=Pop[:,0,j,m]

for i in range(0,CRatingMat.shape[0]):
    for j in range(0,CRatingMat.shape[1]):
        if CRatingMat[i,j]<0:
            CRatingMat[i,j]=np.dot(CUser[i,:],CDrug[0,:,j])*Rmaxx

DL.SaveDat("OutPut/CUser2.DAT", "Numpy", 40, 5, CUser)
DL.SaveDat("OutPut/CDrug2.DAT", "Array", 5, 480, CDrug[0,:,:]) 
DL.SaveDat("OutPut/Rating2.DAT", "Numpy", 40, 480, CRatingMat)

#testing the proposed method
