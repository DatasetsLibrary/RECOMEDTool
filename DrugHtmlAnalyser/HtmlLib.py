# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:40:14 2021

@author: IsmailGhodsollahee
"""
# F1          - F2  - F3     - F4               - F5              - F6         -          - F1       -               -               -        -         -            -                -
# Level       - Age - Genus  - Condition/Reason - Other Condition - Other Drag - DrugName - Category - OverallRating - Effectiveness - Dosage - Benefit - SideEffect - Comment/Review -
# Patient     -     - Male   -                  -                 -            -          -          -               -               -        -         -            -                -
# CareGiver   -     - Female -                  -                 -            -          -          -               -               -        -         -            -                -

def Categorizer(FileName,Categories):
    CategorizedDrug= [[(i,j) for j in range(501)] for i in range(150)] 

    for ii in range(len(Categories)):
        Atr=str(Categories[ii]).replace(" ","^")
        File=FileName+Atr+".html"
        f=open(File,"r",encoding='utf8',errors='surrogateescape')
        
        endoffile=0
        DrugDetected=0
        NumDet=0
        while endoffile<1:
            content=f.readline()
            if ">INDEX OF DRUGS BY CATEGORY<" in content:
               DrugDetected=1 
            if "</td>" in content and DrugDetected==1:
               DrugDetected=0
            if DrugDetected==1:
                if "(<a" in content:
                    print("Some Hybrid Drug")
                if " + " in content:
                    print("Some Hybrid Drug")
                elif "/index.html" in content:
                    effestr="";
                    startstr=0;
                    starstr2=0;
                    ti=len(content)-3
                    while ti>0:
                        if content[ti]==">" and content[ti-1]!="a":
                            ti=ti-13
                            starstr2=1
                        elif content[ti]=="/" and starstr2==0:
                            startstr=1;
                            ti=ti-1;
                        elif content[ti]=="/" and starstr2==1:
                            ti=0;
                        elif content[ti]=="<":
                            ti=ti-1;
                        elif starstr2==1:
                            effestr=str(content[ti])+effestr;
                            ti=ti-1;
                        else:
                            ti=ti-1;
                    print(effestr)
                    NumDet=NumDet+1
                    CategorizedDrug[ii][NumDet]=effestr
            CategorizedDrug[ii][0]=NumDet
            if "</HTML>" in content:
                endoffile=1
        f.close();
    return CategorizedDrug

def DrugCategorizer(Categories,DrugsCategories):
    Druglist= [[(m,n) for n in range(2)] for m in range(0)] 
    for i in range (0,150):
        for j in range (1,DrugsCategories[i][0]+1):
            Drug=DrugsCategories[i][j]
            NotingAdd=0
            PerLeng=len(Druglist)
            for m in range(1,PerLeng):
                if Druglist[m][0]==Drug:
                    NotingAdd=1
                    Druglist[m][1]=str(Druglist[m][1])+" "+str(Categories[i])
            if NotingAdd==0:
                NewDruglist= [[(m,n) for n in range(2)] for m in range(PerLeng+1)] 
                NewDruglist[PerLeng][0]=Drug
                NewDruglist[PerLeng][1]=Categories[i]
                for mm in range (0,PerLeng):
                    NewDruglist[mm][0]=Druglist[mm][0]
                    NewDruglist[mm][1]=Druglist[mm][1]
                Druglist=NewDruglist    
    return Druglist
    
def HtmOpener(FileName,DrugCategory,debug):
#Type must be Defined its imprtant to define drugCategory !!!!!!!!!!!!!!!!!
    f=open(FileName,"r",encoding='utf8',errors='surrogateescape')
    endoffile=0
    NumberofReview=0;
    count=0;
    while endoffile<1:
        content=f.readline() 
        if debug>0:
            count=count+1
            print(count)
            #if count>400:
            #    print(content)
          
        if len(content)>0:
            if "review by" in content:
                NumberofReview=NumberofReview+1;
            if "</HTML>" in content:
                    endoffile=1
    
    print(NumberofReview)
    Temp= [[(i,j) for j in range(15)] for i in range(NumberofReview)]           
    f.close();
    f=open(FileName,"r",encoding='utf8',errors='surrogateescape')
    endoffile=0
    ReviewN=-1;
    while endoffile<1:
        content=f.readline()
        #print(content)
        if len(content)>0:
            """if "Summary prescription drug information" in content:
                cont=content.strip().split(" ");
                for i in range(1,len(cont)):
                   if "Summary" in cont[i]:
                        effestr="";
                        ti=i-1;
                        while ti>0:
                            effestr=cont[ti]+" "+effestr;
                            if "content=" in cont[ti]:
                                ti=0
                            ti=ti-1; 
                        DrugName=effestr[9:len(effestr)] 
                print(effestr)"""
            
            if "- Reviews, Ratings, Comments by Patients</title>" in content:
                content=content.replace(">","");
                cont=content.strip().split(" ");
                for i in range(1,len(cont)):
                   if "Reviews" in cont[i]:
                        effestr="";
                        ti=i-2;
                        while ti>-1:
                            effestr=cont[ti]+" "+effestr;
                            ti=ti-1; 
                        DrugName=effestr[6:len(effestr)] 
                print(effestr)
             
             
            if "review by" in content:
                ReviewN=ReviewN+1
                cont=content.strip().split(" ");
                for i in range(1,len(cont)):
                    if cont[i]=="review" and cont[i+1]=="by":
                        if cont[i+3]=="year" or cont[i+3]=="years":
                            print(cont[i+2])
                            Temp[ReviewN][0]=("patient")
                            Temp[ReviewN][1]=(cont[i+2])
                            Temp[ReviewN][2]=(cont[i+5])
                        if cont[i+4]=="year" or cont[i+4]=="years":
                            print(cont[i+3])
                            Temp[ReviewN][0]=("patient")
                            Temp[ReviewN][1]=(cont[i+3])
                            Temp[ReviewN][2]=(cont[i+6])
                        if cont[i+4]=="of":
                            print(cont[i+2],cont[i+3])
                            print(cont[i+5])
                            Temp[ReviewN][0]=(cont[i+2]+" "+cont[i+3])
                            Temp[ReviewN][1]=(cont[i+5])
                            Temp[ReviewN][2]=(cont[i+8])
                Temp[ReviewN][6]=DrugName
                Temp[ReviewN][7]=DrugCategory                           
            star=0;
            if ">Overall rating:" in content:
                cont=content.strip().split(" ");
                for i in range(1,len(cont)):
                    if "red_star" in cont[i]:
                        star=star+1
                print(star)
                Temp[ReviewN][8]=star
            if ">Effectiveness:" in content:
                cont=content.strip().split(" ");
                for i in range(1,len(cont)):
                    if "</TD></TR>" in cont[i]:
                        ti=i-1
                        effestr=cont[i][0:len(cont[i])-10]
                        while ti>0:
                            if ">" in cont[ti]:
                                ti=0
                            else:
                                effestr=cont[ti]+" "+effestr;
                                ti=ti-1;
                Temp[ReviewN][9]=effestr
                print(effestr)
            
            searched=0;
            if ">Side effects:" in content and "</TD></TR><TR><TD"  in content:
                while searched==0:
                    cont=content.strip().split(" ");
                    for i in range(1,len(cont)):
                        if "</TD></TR><TR><TD" in cont[i]:
                            searched=1;
                            ti=i-1
                            effestr=cont[i][0:len(cont[i])-17]
                            while ti>0:
                                if ">" in cont[ti]:
                                    ti=0
                                else:
                                    effestr=cont[ti]+" "+effestr;
                                    ti=ti-1;
                    if searched==0:
                        ti=len(cont)-1
                        effestr=""
                        while ti>0:
                            if ">" in cont[ti]:
                                ti=0
                            else:
                                effestr=cont[ti]+" "+effestr;
                                ti=ti-1;
                        content=f.readline()
    
               
                Temp[ReviewN][10]=effestr
                print(effestr) 
                
            if ">Condition / reason:" in content:
                cont=content.strip().split(" ");
                for i in range(1,len(cont)):
                    if "</TD></TR>" in cont[i]:
                        ti=i-1
                        effestr=cont[i][0:len(cont[i])-10]
                        while ti>0:
                            if ">" in cont[ti]:
                                ti=0
                            else:
                                effestr=cont[ti]+" "+effestr;
                                ti=ti-1;
                Temp[ReviewN][3]=effestr
                print(effestr)
                
            if ">Other conditions:" in content:
                cont=content.strip().split(" ");
                for i in range(1,len(cont)):
                    if "</TD></TR>" in cont[i]:
                        ti=i-1
                        effestr=cont[i][0:len(cont[i])-10]
                        while ti>0:
                            if ">" in cont[ti]:
                                ti=0
                            else:
                                effestr=cont[ti]+" "+effestr;
                                ti=ti-1;
                Temp[ReviewN][4]=effestr
                print(effestr)   
            if ">Other drugs taken:" in content:
                cont=content.strip().split(" ");
                for i in range(1,len(cont)):
                    if "</TD></TR><TR><TD" in cont[i]:
                        ti=i-1
                        effestr=cont[i][0:len(cont[i])-17]
                        while ti>0:
                            if ">" in cont[ti]:
                                ti=0
                            else:
                                effestr=cont[ti]+" "+effestr;
                                ti=ti-1;
                Temp[ReviewN][5]=effestr
                print(effestr)   
                
                 
            searched=0;    
            if ">Dosage & duration:" in content:
                while searched==0:
                    cont=content.strip().split(" ");
                    for i in range(1,len(cont)):
                        if "</TD></TR>" in cont[i]:
                            searched=1;
                            ti=i-1
                            effestr=cont[i][0:len(cont[i])-10]
                            while ti>0:
                                if ">" in cont[ti]:
                                    ti=0
                                else:
                                    effestr=cont[ti]+" "+effestr;
                                    ti=ti-1;
                    if searched==0:
                        ti=len(cont)-1
                        effestr=""
                        while ti>0:
                            if ">" in cont[ti]:
                                ti=0
                            else:
                                effestr=cont[ti]+" "+effestr;
                                ti=ti-1;
                        content=f.readline()
               
                Temp[ReviewN][11]=effestr
                print(effestr)
                
            searched=0;
            if ">Benefits:" in content:
                while searched==0:
                    cont=content.strip().split(" ");
                    for i in range(1,len(cont)):
                        if "</TD></TR>" in cont[i]:
                            searched=1;
                            ti=i-1
                            effestr=cont[i][0:len(cont[i])-10]
                            while ti>0:
                                if ">" in cont[ti]:
                                    ti=0
                                else:
                                    effestr=cont[ti]+" "+effestr;
                                    ti=ti-1;
                    if searched==0:
                        ti=len(cont)-1
                        effestr=""
                        while ti>0:
                            if ">" in cont[ti]:
                                ti=0
                            else:
                                effestr=cont[ti]+" "+effestr;
                                ti=ti-1;
                        content=f.readline()
               
                Temp[ReviewN][12]=effestr
                print(effestr)
            searched=0;
            if ">Side effects:" in content:
                while searched==0:
                    cont=content.strip().split(" ");
                    for i in range(1,len(cont)):
                        if "</TD></TR>" in cont[i]:
                            searched=1;
                            ti=i-1
                            effestr=cont[i][0:len(cont[i])-10]
                            while ti>0:
                                if ">" in cont[ti]:
                                    ti=0
                                else:
                                    effestr=cont[ti]+" "+effestr;
                                    ti=ti-1;
                    if searched==0:
                        ti=len(cont)-1
                        effestr=""
                        while ti>0:
                            if ">" in cont[ti]:
                                ti=0
                            else:
                                effestr=cont[ti]+" "+effestr;
                                ti=ti-1;
                        content=f.readline()
    
               
                Temp[ReviewN][13]=effestr
                print(effestr) 
            searched=0;
            if ">Comments:" in content:
                while searched==0:
                    cont=content.strip().split(" ");
                    for i in range(1,len(cont)):
                        if "</TD></TR>" in cont[i]:
                            searched=1;
                            ti=i-1
                            effestr=cont[i][0:len(cont[i])-10]
                            while ti>0:
                                if ">" in cont[ti]:
                                    ti=0
                                else:
                                    effestr=cont[ti]+" "+effestr;
                                    ti=ti-1;
                    if searched==0:
                        ti=len(cont)-1
                        effestr=""
                        while ti>0:
                            if ">" in cont[ti]:
                                ti=0
                            else:
                                effestr=cont[ti]+" "+effestr;
                                ti=ti-1;
                        content=f.readline()
               
                Temp[ReviewN][14]=effestr
                print(effestr) 
                 
            if "</HTML>" in content:
                endoffile=1
    f.close(); 
    return Temp,NumberofReview

def DatasetUpdater(FileNameNew,FileNameOld,Temp):
    ReviewN=len(Temp)
    K=open(FileNameOld,"r",encoding='utf8')           
    SizeofDataset=0;
    content=K.readline()
    cont=content.strip().split(",");
    SizeofDataset=cont[0]
    
    D=open(FileNameNew,"w",encoding='utf8')
    cont[0]=int(cont[0])+ReviewN;
    strText=str(cont[0])
    print(SizeofDataset,ReviewN)
    
    for i in range(1,15):
        strText=strText+","+str(cont[i])
    strText=strText+"\n"
    D.writelines(strText)    
    for i in range(1,int(SizeofDataset)+3):
        D.writelines(K.readline());
    
    for j in range(int(SizeofDataset),ReviewN):    
        strText=str(Temp[j][0])
        for i in range(0,14):
            if type(Temp[j][i]) is tuple:
                D.writelines("-"+",");
            else:
                Tempstr=str(Temp[j][i]).replace(',',';')
                try:
                    D.writelines(Tempstr+",");
                except:
                    D.writelines(" ,");
            #strText=strText+","+str(Temp[j][i]).replace(","," ")
        #strText=strText+"\n";
        #print("===",j,"-----")
        #print(strText)
        i=i+1
        if type(Temp[j][i]) is tuple:
            D.writelines("-"+"\n");
        else:
            Temp[j][i]=Temp[j][i].encode('ascii',errors='ignore').decode('ascii')
            Temp[j][i]=Temp[j][i].replace(",",";")
            D.writelines(Temp[j][i]+"\n");
            print(Temp[j][i])
        #D.writelines(strText)
    
    K.close();
    D.close();            