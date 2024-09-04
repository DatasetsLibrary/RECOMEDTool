# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:41:35 2021

@author: IsmailGhodsollahee
"""
"""
UserClustring
"""

import numpy as np
from random import random

def InitalMatrix(TrainSize,LatentFactors,PreProcessDataSet,NumberofDrug,DataSet):
    UsersMat=np.zeros(shape=(TrainSize,LatentFactors))
    #RatingMat=np.zeros(shape=(TrainSize,NumberofDrug))
    DrugMat=np.zeros(shape=(LatentFactors,NumberofDrug))
    
    for i in range(0,TrainSize):
        Temp=PreProcessDataSet[i][:]
        for j in range(0,LatentFactors-1):
            UsersMat[i,j]=int(Temp[j])
        UsersMat[i,5]=random();
    
    for i in range(0,LatentFactors):
        for j in range(0,NumberofDrug):
            DrugMat[i,j]=random();
           
    OrginalRatingMat=np.zeros(shape=(len(DataSet),NumberofDrug))
    for i in range(0,TrainSize):
        Temp=PreProcessDataSet[i][:]
        for j in range(0,NumberofDrug):
            if j==Temp[6]:
                OrginalRatingMat[i,j]=Temp[9]
            else:
                OrginalRatingMat[i,j]=-1   
    return UsersMat,DrugMat,OrginalRatingMat
    

def UserClassifier(TrainSize,LatentFactors,UsersMat,DrugMat,NumberofDrug,PreProcessDataSet):
    NormUsersMat=np.zeros(shape=(TrainSize,LatentFactors-1))
    for j in range(0,LatentFactors-1):
        TempMax=max(UsersMat[:,j])
        for i in range(0,TrainSize):
            NormUsersMat[i,j]=UsersMat[i,j]/TempMax
            
    Kclusters=40;
    MaxDistance=0.24;
    FeatureNum=LatentFactors-1;
    DetectedClusters=0;
    cluster=np.zeros(shape=(Kclusters,FeatureNum))
    clusterSize=np.zeros(shape=(Kclusters))
    clusterMeanS=np.zeros(shape=(Kclusters))
    Classified=np.zeros(shape=(len(NormUsersMat)))
    AllClassified=0;
    
    CRatingMat=np.zeros(shape=(Kclusters,NumberofDrug))
    EffectiveMat=np.zeros(shape=(Kclusters,NumberofDrug))
    DosageMat=np.zeros(shape=(Kclusters,NumberofDrug))
    
    Temp=PreProcessDataSet[0][:];
    CRatingMat[0,Temp[6]]=Temp[8]
    EffectiveMat[0,Temp[6]]=Temp[9]
    DosageMat[0,Temp[6]]=Temp[10]
    cluster[0,:]=NormUsersMat[0,:];DetectedClusters=1;
    ClassifiedNumber=0;
    for i in range(0,len(NormUsersMat)):
        Classified[i]=-1
        clusterSize[j]=0
        clusterMeanS[j]=2
        
    for i in range(0,Kclusters):
        for j in range(0,NumberofDrug):
            CRatingMat[i,j]=-1 
            EffectiveMat[i,j]=-1
            DosageMat[i,j]=-1
                    
    clusterSize[0]=1
    while(AllClassified==0):
        print(ClassifiedNumber,MaxDistance,DetectedClusters)
        ClassifiedNumber=0;
        kdirect=int(random()*2);
        for inv in range(0,len(NormUsersMat)): 
            if kdirect==1:
                i=inv
            else:
                i=len(NormUsersMat)-inv-1
            
            Temp=PreProcessDataSet[i][:];
            Dj=Temp[6]
            if Classified[i]==-1:
                for j in range(0,DetectedClusters):
                    distance=0
                    for m in range(0,FeatureNum):
                        distance=distance+abs(cluster[j,m]-NormUsersMat[i,m])
                    #print("distance",distance,Classified[i])
                    if (distance<MaxDistance and Classified[i]==-1 and CRatingMat[j,Temp[6]]<0 and clusterSize[j]<(len(NormUsersMat)/Kclusters)):
                        Classified[i]=j
                        CRatingMat[j,Temp[6]]=Temp[8]
                        EffectiveMat[j,Temp[6]]=Temp[9]
                        DosageMat[j,Temp[6]]=Temp[10]
                        clusterSize[j]=clusterSize[j]+1;
                        ClassifiedNumber=ClassifiedNumber+1;
                        for m in range(0,FeatureNum):
                            cluster[j,m]=(cluster[j,m]+(NormUsersMat[i,m]*(clusterMeanS[j]-1)))/clusterMeanS[j]
                            clusterMeanS[j]=clusterMeanS[j]+1
            if Classified[i]==-1 and DetectedClusters<Kclusters:
                clusterAdded=0;jj=0
                while clusterAdded==0 and jj<Kclusters:
                    if sum(cluster[jj,:])==0:
                        clusterAdded=1
                        Classified[i]=jj
                        ClassifiedNumber=ClassifiedNumber+1;
                        for m in range(0,FeatureNum):
                            cluster[jj,m]=cluster[jj,m]+NormUsersMat[i,m]
                        DetectedClusters=DetectedClusters+1;
                        clusterSize[jj]=clusterSize[jj]+1;
                    jj=jj+1;
                        
    
        for j in range(0,Kclusters):
            if clusterSize[j]==0 and sum(cluster[j,:])!=0:
                for m in range(0,FeatureNum):
                    cluster[j,m]=0;
                    clusterMeanS[j]=2
                DetectedClusters=DetectedClusters-1;
        
        for i in range(0,len(NormUsersMat)):
            Temp=PreProcessDataSet[i][:];
            Dj=Temp[6]
            if Classified[i]==-1:
                minDis=100000;minInd=-1;
                for j in range(0,Kclusters):
                    distance=0
                    for m in range(0,FeatureNum):
                        distance=distance+abs(cluster[j,m]-NormUsersMat[i,m])
                    if distance<minDis and CRatingMat[j,Temp[6]]<0 and clusterSize[j]<(2*len(NormUsersMat)/Kclusters):
                        minDis=distance
                        minInd=j
                if (minInd>0):
                    Classified[i]=minInd
                    CRatingMat[minInd,Temp[6]]=Temp[8]
                    EffectiveMat[minInd,Temp[6]]=Temp[9]
                    DosageMat[minInd,Temp[6]]=Temp[10]
                    clusterSize[minInd]=clusterSize[minInd]+1;
                    ClassifiedNumber=ClassifiedNumber+1;
                    for m in range(0,FeatureNum):
                        cluster[minInd,m]=(cluster[minInd,m]+(NormUsersMat[i,m]*(clusterMeanS[minInd]-1)))/clusterMeanS[minInd]
                        clusterMeanS[minInd]=clusterMeanS[minInd]+1
               
        #print("ClassifiedNumber",ClassifiedNumber,"DetectedClusters",DetectedClusters)
    
        """if (DetectedClusters<Kclusters):
            if MaxDistance>0.002:
                MaxDistance=MaxDistance-0.0001;
            for i in range(0,len(NormUsersMat)):
                Classified[i]=-1;
            for i in range(0,Kclusters):
                clusterSize[i]=0"""
           
        if (DetectedClusters==Kclusters and ClassifiedNumber>len(NormUsersMat)-5):
            AllClassified=1;
        elif (ClassifiedNumber<len(NormUsersMat)):
            MaxDistance=MaxDistance+0.001;
            for i in range(0,len(NormUsersMat)):
                Classified[i]=-1;
            for i in range(0,Kclusters):
                clusterSize[i]=0
            for i in range(0,Kclusters):
                for j in range(0,NumberofDrug):
                    CRatingMat[i,j]=-1
                    EffectiveMat[i,j]=-1
                    DosageMat[i,j]=-1
    return Classified,cluster,CRatingMat,EffectiveMat,DosageMat,NormUsersMat
