# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 03:51:41 2022

@author: IsmailGhodsollahee
"""
"""
Evaluation 3
"""
import numpy as np
import DatLib as DL

SizeOfDatast=1073
NumberofDrug=480
TrainSize=500
LatentFactor=6
FeatureNum=370

cluster=DL.LoadDat("DATS/cluster.DAT", 40, LatentFactor-1)
DrugMat=DL.LoadDat("DATS/DrugMat.DAT", LatentFactor, NumberofDrug) 
CRatingMat=DL.LoadDat("OutPut/DDrugCRatingMatUSPhase.DAT", 40, NumberofDrug)

Dataset=DL.LoadDat("DATS/DataSet.DAT", SizeOfDatast+2, 14)               
DrugList=DL.LoadDat("DATS/DrugList.DAT", NumberofDrug, 1)

CUser=DL.LoadDat("OutPut/CUser2.DAT", 40, 5)
CDrug=DL.LoadDat("OutPut/CDrug2.DAT", 5, 480) 
CRatingMat=DL.LoadDat("OutPut/Rating2.DAT", 40, 480)
Classified=DL.LoadDat("DATS/Classified.DAT", TrainSize, 1)

DrugCRatingMat=DL.LoadDat("OutPut/DDrugCRatingMat.DAT", 40, NumberofDrug)
DrugClassified=DL.LoadDat("DATS/DrugClassified.DAT", NumberofDrug, 1)


MaxCR=np.zeros(shape=(40))
for i in range(0,40):
    MaxCR[i]=max(CRatingMat[i,:])

MaxDD=np.zeros(shape=(499))
for i in range(0,499):
    MaxDD[i]=max(DrugCRatingMat[i])
his=[]   
TP=0;FP=0;TN=0;FN=0;    
for i in range(2,499):
    T=0;P=0;
    if (int(Dataset[i][8])>=5):
        T=1;
    for j in range(1,479):
        if Dataset[i][6]==DrugList[j]:
            DrugID=j+2

    cc=int(Classified[i]);
    dd=float(DrugClassified[DrugID])
    print (cc,dd)
    #print(CRatingMat[int(cc),DrugID],DrugCRatingMat[i,int(dd)])
    a=CRatingMat[cc][DrugID]
    b=DrugCRatingMat[i][int(dd)-1]
    his.append([a,b,T,P])
    if (float(b)>=5):
        P=1;
    if (T==1 and P==1):
        TP=TP+1
    if (T==0 and P==1):
        FP=FP+1
    if (T==1 and P==0):
        TN=TN+1
    if (T==0 and P==0):
        FN=FN+1

Precision=TP/(TP+FP)
Recall=TP/(TP+FN)
Accuracy=TN/(497)
Specifity=TN/(TP+TN)
F1_Score=2*(Precision*Recall)/(Precision+Recall)
F2_Score=5*TP/(5*TP+4*FN+FP)

print("Accuracy",Accuracy)
print("Specifity",Specifity)
print("Precision",Precision)
print("Recall",Recall)
print("F1_Score",F1_Score)
print("F2_Score",F2_Score)

import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_confusion_matrix
conf_matrix=np.array([[TP/4.6,FP/4.6],[FN/4.6,TN/4.6]])

fig, ax = plot_confusion_matrix(conf_mat=conf_matrix, figsize=(5,5), cmap=plt.cm.Blues,colorbar=True,class_names=['proper','not_proper'])
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Just Drug Rating', fontsize=18)
plt.show()



FPRD=[]
TPRD=[]
for n in range(0,100):
    print(n)
    TP=0;FP=0;TN=0;FN=0;    
    for i in range(2,499):
        T=0;P=0;
        if (int(Dataset[i][8])>=5):
            T=1;
        for j in range(1,479):
            if Dataset[i][6]==DrugList[j]:
                DrugID=j+2
    
        cc=int(Classified[i]);
        dd=float(DrugClassified[DrugID])
        #print (cc,dd)
        #print(CRatingMat[int(cc),DrugID],DrugCRatingMat[i,int(dd)])
        a=CRatingMat[cc][DrugID]
        b=DrugCRatingMat[i][int(dd)-1]
        if (float(b)>=n/10):
            P=1;
        if (T==1 and P==1):
            TP=TP+1
        if (T==0 and P==1):
            FP=FP+1
        if (T==1 and P==0):
            TN=TN+1
        if (T==0 and P==0):
            FN=FN+1
    FPRD.append(FP/(FP+TN))
    TPRD.append(TP/(TP+TN))

plt.plot(FPRD,TPRD,label="Just Drug Rating")
plt.ylabel("TPR",fontsize=18)
plt.xlabel("FPR",fontsize=18)
plt.title("ROC",fontsize=18)
plt.legend()
plt.show()
