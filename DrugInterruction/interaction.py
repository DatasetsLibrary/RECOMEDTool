# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:27:20 2022

@author: IsmailGhodsollahee
"""
import InconsistencyLibrary as IL

listDr=IL.drugMapper("druglist.txt")
ListFiles=IL.FileListExtractor("DataSetAddress")    
IntractionMatrix=IL.IntractionMatrixCreator(listDr,ListFiles);

D=open("DrugIncosistance.csv","w")
for i in range(len(IntractionMatrix)):
    strText=""
    for j in range(len(IntractionMatrix[1])):
        strText=strText+IntractionMatrix[i][j]+","
    strText=strText+"\n"
    D.writelines(strText)    
D.close();            