# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 23:34:59 2021

@author: IsmailGhodsollahee
"""
"""
"""
#import DatLib as DL

import numpy as np
from random import random
import DatLib as DL

def LoadDrugFeatures(FileName):
    K=open(FileName,"r")               
    DataSet= [[(i,j) for j in range(370)] for i in range(481)] 
    for i in range(0,481):
        content=K.readline()
        cont=content.strip().split(",");
        for j in range(0,370):
            DataSet[i][j]=cont[j];
    return DataSet
            

def InitalMatrix(TrainSize,LatentFactors,NumberofDrug,DrugFeaturesNum,DrugSet):
    UsersMat=np.zeros(shape=(TrainSize,LatentFactors))
    #RatingMat=np.zeros(shape=(TrainSize,NumberofDrug))
    DrugMat=np.zeros(shape=(DrugFeaturesNum,NumberofDrug))
    
    DrugMatForClass=np.zeros(shape=(NumberofDrug,DrugFeaturesNum))
    
    for i in range(0,TrainSize):
        for j in range(0,LatentFactors):
            UsersMat[i,j]=random();
            
    for i in range(0,NumberofDrug):
        Temp=DrugSet[i+2]
        for j in range(2,DrugFeaturesNum):
            if (Temp[j]==''):
                DrugMat[j-2,i]=0;
            else:
                DrugMat[j-2,i]=1;
    
    for i in range(0,NumberofDrug):
        Temp=DrugSet[i+2]
        for j in range(2,DrugFeaturesNum):
            if (Temp[j]==''):
                DrugMatForClass[i,j-2]=0;
            else:
                DrugMatForClass[i,j-2]=1;
                
    return UsersMat,DrugMat,DrugMatForClass
    
DrugSet=LoadDrugFeatures("DruSet.csv")
OrginalRatingMat=DL.LoadDat("DATS/OrginalRatingMat.DAT",1075,706)
DataSet=DL.LoadDat("DATS/Dataset.DAT",1075,14)    
PreProcessDataSet=DL.LoadDat("DATS/PreProcessDataSet.DAT", 1073, 14) 
UsersMat,DrugMat,DrugMatForClass=InitalMatrix(500,6,479,370,DrugSet)


trainSize=500
Kclusters=30;
FeatureNum=370;
DrugNum=479
MaxDistance=0.001;
DetectedClusters=0;
cluster=np.zeros(shape=(Kclusters,FeatureNum))
clusterSize=np.zeros(shape=(Kclusters))
clusterMeanS=np.zeros(shape=(Kclusters))
Classified=np.zeros(shape=(DrugNum))
AllClassified=0;
CRatingMat=np.zeros(shape=(trainSize,Kclusters))

cluster[0,:]=DrugMatForClass[1]
DetectedClusters=1;
ClassifiedNumber=0;
for i in range(0,Kclusters):
    Classified[i]=-1
    clusterSize[i]=0
    clusterMeanS[i]=2
    
for i in range(0,trainSize):
    for j in range(0,Kclusters):
        CRatingMat[i,j]=-1 

                
clusterSize[0]=1
while(AllClassified==0):
    print(ClassifiedNumber,MaxDistance,DetectedClusters)
    ClassifiedNumber=0;
    kdirect=int(random()*2);
    for inv in range(0,DrugNum): 
        i=inv
        """if kdirect==1:
            i=inv
        else:
            i=DrugNum+2-inv-1"""
        
        Temp=DrugMatForClass[i][:];
        #Dj=Temp[6]
        if Classified[i]==-1:
            for j in range(0,DetectedClusters):
                distance=0
                for m in range(0,FeatureNum):
                    distance=distance+abs(cluster[j,m]-DrugMatForClass[i,m])
                #print("distance",distance,Classified[i])
                if (distance<MaxDistance and Classified[i]==-1 and clusterSize[j]<(trainSize/Kclusters)):
                    Classified[i]=j
                    for ii in range(1,trainSize):
                        if CRatingMat[ii,j]<0:
                            CRatingMat[ii,j]=OrginalRatingMat[ii,i]
                    clusterSize[j]=clusterSize[j]+1;
                    ClassifiedNumber=ClassifiedNumber+1;
                    for m in range(0,FeatureNum):
                        cluster[j,m]=(cluster[j,m]+(DrugMatForClass[i,m]*(clusterMeanS[j]-1)))/clusterMeanS[j]
                        clusterMeanS[j]=clusterMeanS[j]+1
        if Classified[i]==-1 and DetectedClusters<Kclusters:
            clusterAdded=0;jj=0
            while clusterAdded==0 and jj<Kclusters:
                if sum(cluster[jj,:])==0:
                    clusterAdded=1
                    Classified[i]=jj
                    ClassifiedNumber=ClassifiedNumber+1;
                    for m in range(0,FeatureNum):
                        cluster[jj,m]=cluster[jj,m]+DrugMatForClass[i,m]
                    clusterSize[jj]=clusterSize[jj]+1;
                jj=jj+1;
                    
    print("step forward 1")
    for j in range(0,Kclusters):
        if clusterSize[j]==0 and sum(cluster[j,:])!=0:
            for m in range(0,FeatureNum):
                cluster[j,m]=0;
                clusterMeanS[j]=2
            for m in range(j,Kclusters-1):
                cluster[j,:]=cluster[j+1,:];
    DetectedClusters=0
    for j in range(0,Kclusters):
        if sum(cluster[j,:])!=0:
            DetectedClusters=DetectedClusters+1;
    
    print("step forward 2")
    for i in range(0,DrugNum):
        Temp=DrugMatForClass[i][:];
        if Classified[i]==-1:
            minDis=100000;minInd=-1;
            for j in range(0,Kclusters):
                distance=0
                for m in range(0,FeatureNum):
                    distance=distance+abs(cluster[j,m]-DrugMatForClass[i,m])
                if distance<minDis and clusterSize[j]<(2*DrugNum/Kclusters):
                    minDis=distance
                    minInd=j
            if (minInd>0):
                Classified[i]=minInd
                for ii in range(1,trainSize):
                    if CRatingMat[ii,minInd]<0:
                        CRatingMat[ii,minInd]=OrginalRatingMat[ii,i]
                clusterSize[minInd]=clusterSize[minInd]+1;
                ClassifiedNumber=ClassifiedNumber+1;
                for m in range(0,FeatureNum):
                    cluster[minInd,m]=(cluster[minInd,m]+(DrugMatForClass[i,m]*(clusterMeanS[minInd]-1)))/clusterMeanS[minInd]
                    clusterMeanS[minInd]=clusterMeanS[minInd]+1
    
    print("step forward 3")
    if (DetectedClusters==Kclusters and ClassifiedNumber>DrugNum-5):
        AllClassified=1;
    elif (ClassifiedNumber<DrugNum-2):
        MaxDistance=MaxDistance+0.001;
        for i in range(0,DrugNum):
            Classified[i]=-1;
        for i in range(0,Kclusters):
            clusterSize[i]=0
        for ii in range(0,trainSize):
            for j in range(0,Kclusters):
                CRatingMat[ii,j]=-1

DL.SaveDat("OutPut/Drugcluster.DAT", "Numpy", Kclusters, FeatureNum, cluster)
DL.SaveDat("OutPut/DrugClassified.DAT", "Array", DrugNum, 1, Classified)

DL.SaveDat("OutPut/DrugCRatingMatEmp.DAT", "Array", trainSize, Kclusters, CRatingMat)
