# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:41:35 2021

@author: IsmailGhodsollahee
"""

import PreprossingLib as Pl
import UserClusterLib as UC
import numpy as np
import DatLib as DL
NewTfIdf,NumberOfWord=Pl.TFIDFCondition()
TrainSize=500
SizeOfDatast=1073
LatentFactor=6
PreProcessDataSet,NumberofDrug,DataSet,DrugList=Pl.Tagger("Dataset.csv","DruSet.csv",NewTfIdf,NumberOfWord)

UsersMat,DrugMat,OrginalRatingMat=UC.InitalMatrix(TrainSize,LatentFactor,PreProcessDataSet,NumberofDrug,DataSet)
Classified,cluster,CRatingMat,EffectiveMat,DosageMat,NormUsersMat=UC.UserClassifier(TrainSize,LatentFactor,UsersMat,DrugMat,NumberofDrug,PreProcessDataSet)


DL.SaveDat("OutPut/Classified.DAT", "Numpy", TrainSize, 1, Classified)
DL.SaveDat("OutPut/DataSet.DAT", "Array", SizeOfDatast+2, 14, DataSet)               

DL.SaveDat("OutPut/PreProcessDataSet.DAT", "Array", SizeOfDatast, 14, PreProcessDataSet) 

DL.SaveDat("OutPut/cluster.DAT", "Numpy", 40, LatentFactor-1, cluster)
DL.SaveDat("OutPut/DrugMat.DAT", "Numpy", LatentFactor, NumberofDrug, DrugMat) 
DL.SaveDat("OutPut/CRatingMatEmp.DAT", "Numpy", 40, NumberofDrug, CRatingMat)
DL.SaveDat("OutPut/EffectiveMat.DAT", "Numpy", 40, NumberofDrug, EffectiveMat) 
DL.SaveDat("OutPut/DosageMat.DAT", "Numpy", 40, NumberofDrug, DosageMat) 

DL.SaveDat("OutPut/NormUsersMat.DAT", "Numpy", TrainSize,LatentFactor-1, NormUsersMat) 
DL.SaveDat("OutPut/OrginalRatingMat.DAT", "Numpy", SizeOfDatast, NumberofDrug, OrginalRatingMat) 

DL.SaveDat("OutPut/DrugList.DAT", "Array", NumberofDrug, 1, DrugList)
