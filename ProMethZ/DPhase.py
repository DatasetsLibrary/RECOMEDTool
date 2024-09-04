"""
Created on Thu Dec 31 23:03:59 2022

@author: IsmailGhodsollahee
"""
"""
US Fact
"""
import numpy as np
from random import random,randint
import math as ma
import matplotlib.pyplot as plt
import DatLib as DL

SizeOfDatast=1073
NumberofDrug=480
TrainSize=500
LatentFactor=6
Kclusters=30
FeatureNum=370

DataSet=DL.LoadDat("DATS/DataSet.DAT", SizeOfDatast+2, 14)               
DrugList=DL.LoadDat("DATS/DrugList.DAT", NumberofDrug, 1)
NormUsersMat=DL.LoadDat("DATS/NormUsersMat.DAT", TrainSize,LatentFactor-1) 

Drugcluster=DL.LoadDat("DATS/Drugcluster.DAT", Kclusters, FeatureNum)
DrugClassified=DL.LoadDat("DATS/DrugClassified.DAT", NumberofDrug, 1)
DrugCRatingMat=DL.LoadDat("DATS/DrugCRatingMatEmp.DAT", TrainSize, Kclusters)

for i in range(len(DrugCRatingMat)):
    for j in range(len(DrugCRatingMat[0])):
        DrugCRatingMat[i][j]=float(DrugCRatingMat[i][j])

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

def Cost(CRDrug,DSize,Population,DrugCRatingMat,NumberLatentFactor):
    HiP=Population.shape[0]
    HiD=len(DrugCRatingMat[0])
    CostT=np.zeros(shape=(DSize,HiP))
    CUsser=np.zeros(shape=(NumberLatentFactor))  
    CostTT=np.zeros(shape=(HiP))
    
    for m in range(0,HiP):
        for j in range(0,DSize):
            CUsser=Population[m,j,:]
            for i in range(0,HiD):
                cd=CRDrug[i,:]
                if (DrugCRatingMat[j][i])>0:
                    CostT[j,m]=CostT[j,m]+abs(DrugCRatingMat[j][i]-np.dot(CUsser,np.transpose(cd)))
    for m in range(0,HiP):
         for j in range(0,DSize):
             CostTT[m]=CostTT[m]+CostT[j,m]
    return(CostTT)

def NonDominateSorting(Pop,CostT):
    for i in range(0,CostT.shape[0]):
        Minn=1000000;MinIndex=0
        for ii in range(i,CostT.shape[0]):
            cc=ma.pow(CostT[ii],2)
            if cc < Minn:
                Minn=cc
                MinIndex=ii
        if Minn<1000000:
            Temp=CostT[i];CostT[i]=CostT[MinIndex];CostT[MinIndex]=Temp;
            Temp=Pop[i,:,:]
            Pop[i,:,:]=Pop[MinIndex,:,:]
            Pop[i,:,:]=Temp
    return Pop,CostT

def SelectionElimination(Pop,EleminationFactor,GenerationFactor,MutationFactor):
    SelectionSize=ma.floor(Pop.shape[0]*EleminationFactor)
    GenerationSize=ma.floor(Pop.shape[0]*GenerationFactor)
    for j in range(0,Pop.shape[0]):
        if j==0:
            """a=1"""
        elif j<=SelectionSize+GenerationSize and j>SelectionSize:
            DoMutation=int(random()*2*MutationFactor)
            NumMutation=int(random()*Pop.shape[1])
            if DoMutation>0:
                for nn in range(0,NumMutation):
                    place=randint(0,Pop.shape[1]-1)
                    place2=randint(0,Pop.shape[2]-1)
                    Pop[j,place,place2]=random()     
        elif j<=SelectionSize:
            parent1=randint(0,Pop.shape[0]-SelectionSize-GenerationSize-1)
            parent2=randint(0,Pop.shape[0]-SelectionSize-GenerationSize-1)
            FactorofParent=randint(0,Pop.shape[1]-1)
            for n in range(0,Pop.shape[1]):
                if n<FactorofParent:
                    Pop[j,n,:]= Pop[parent1,n,:]
                else:
                    Pop[j,n,:]= Pop[parent2,n,:]
        else:
            for n in range(0,Pop.shape[1]):
                for m in range(0,Pop.shape[2]):
                    Pop[j,n,m]=random();
            
    return Pop

def InitialPopulation(DSize,NumPopulationForEachCluster,GenSize):
    Pop=np.zeros(shape=(NumPopulationForEachCluster,DSize,GenSize))
    for i in range(0,NumPopulationForEachCluster):
        for n in range(0,DSize):
            for j in range(0,GenSize):
                Pop[i,n,j] = random()    
    return Pop

Rmaxx,DrugCRatingMat=Normalize(DrugCRatingMat)
LatentFactors=5
DSize=30

Pop=InitialPopulation(DSize,20,LatentFactors)  

IterationNumber=500;
it=0
history=np.zeros(shape=(IterationNumber))
CostT=Cost(NormUsersMat,DSize,Pop,DrugCRatingMat,LatentFactors)


sizecost=CostT.shape[0];
while (it<IterationNumber-1):  
    CostT=Cost(NormUsersMat,DSize,Pop,DrugCRatingMat,LatentFactors)
    Pop,CostT=NonDominateSorting(Pop,CostT)
    history[it]=CostT[0]/sizecost;
    Pop=SelectionElimination(Pop,0.3,0.3,10)#EleminationFactor+GenerationFactor must be less than 1
    it=it+1;print(it,CostT[0])

plt.plot(history[1:IterationNumber-1],label="Absolute Error of 500 epochs");
plt.legend(loc=2, ncol=2)
plt.savefig('Rating.png', dpi=300)


CDrug=np.zeros(shape=(LatentFactors,len(DrugCRatingMat[0])))

for j in range(0,len(DrugCRatingMat[0])):
    for m in range(0,LatentFactors):
        CDrug[m,j]=Pop[0,j,m]

for i in range(0,TrainSize-2):
    for j in range(0,len(DrugCRatingMat[0])):
        if DrugCRatingMat[i][j]<0:
            DrugCRatingMat[i][j]=np.dot(NormUsersMat[i,:],CDrug[:,j])*Rmaxx

DL.SaveDat("OutPut/DDrugCRatingMatUSPhase.DAT","Array",TrainSize,Kclusters,DrugCRatingMat)
