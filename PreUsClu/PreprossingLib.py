# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:41:35 2021

@author: IsmailGhodsollahee
"""
"""
Preprosessing
"""
import math
from random import random
#Bag of Word
def TFIDFCondition():
    ConditionList=["high","blood","pressure","chronic","insomnia","depression","anxiety","OCD","nausea","panic","attacks","asthma","flares","mytral","valve","prolapse","HIV","alzheimers","short","term","memory","loss","memory","headache","pain","chronic","pain","sleep","CAD","lower","back","pain","hot","flashes","arthritis","pain","crohns","colitis","fibromyalgia","carpal","tunnel","pain","relief","after","outpatient","hernia","surgery","bursitis","and","tennis","elbow","osteoarthritis","reactive","arthritis","broken","ribs","headaches","cancer","constant","pain","cancer","related","pain","recurrent","depression","GAD","chronic","pain","due","to","neck","injury","and","surgeries","chronic","regional","pain","syndrome","migraines","tension","headaches","cervical","spondylosis","menstrual","cramps","arthritis","pain","from","neck","injury","flu","rheumatoid","arthritis","","bipolar","bipolar","II","oral","surgery","pain","from","recovering","from","abdominal","surgery","neuropathic","knee","pain","back","pain","muscle","spasm","neck","pain","hip","pain","opiate","addiction","opiod","addiction","oral","infection","oral","swelling","ankylosing","spondylitis","","fever","earache","difficulty","sleeping","because","of","nervous","system","prob","kidney","stones","pain","control","pain","after","surgery","ACL","surgery","foot","surgery","sleep","distubance","mild","depression","opioid","Addiction","heroin","addiction","epilepsy","neuropathic","pain","pain","after","dental","surgery","budging","disk","in","neck","respiratory","infection","mycoplasma","bronchitis","pain","after","minor","surgery","herniated","disk","in","my","lower","back","tooth","infection","post","surgery","stomach","pain","i","got","my","tooth","pulled","dizziness","stress","mood","swings","felt","bipolar","sciatica","pain","hives","hypertension","blood","pressure","diabetes","high","blood","pressure","after","pregnancy","labyrinthitis","benign","proxysmal","positional","vertigo","itching","swelling","due","to","allergies","allergies","rhinitis","seasonal","allergies","chronic","sinus","congestion","allergies","sneezing","watery","runny","nose","allergy","to","trauma","to","the","face","allergy","runny","nose","hay","fever","eye","allergies","anxiety","from","a","reaction","obsessive","compulsive","disorder","bipolor","worry","situational","anxiety","severe","performance","anxiety","mild","sedative","nausea","after","surgery","anxiety","due","to","relationship","stress","temporary","anxiety","anxiety","related","to","severe","premenstrual","syndrome","anxiety","attacks","anxiety","rapid","onset","cystic","acne","strep","throat","throat","infection","and","cough","persistent","chest","infection","symptoms","eye","infection","acne","ear","infection","tonsilitis","possible","strep","sinus","infection","cystic","fibrosis","sinusitis","bronchitis","simple","laceration","ballanitis","severe","sinus","infection","strep","throat","inner","ear","infection","upper","respiratory","infection","on","vacation","UTI","skin","infection","streptoccocus","severe","sore","throat","high","fever","mild","local","skin","infection","vaginal","bacteria","tooth","abscess","tonsillitis","throat","skin","probles","balckheads","fungus","tinea","barbae","post","surgery","antibiotic","infected","lymph","node","acute","sinusitis","treatment","of","acne","conjunctivitus","yeast","diaper","rash","candida","rashes","perioral","dermatitis","rosacea","mild","acne","dental","surgery","periodontal","disease","blackheads","oily","skin","cold","herpes","fever","blisters","cold","sores","malaria","hepatitis","B","sore","throat","urinary","tract","infection","epidimytis","infection","dermatitis","herpetiformis","vaginal","yeast","infection","candida","caused","yeast","infection","chronic","fatigue","epstein","barr","virus","bacterial","vaginosis","gum","infection","yeast","infection","systemic","fungus","tuberculosis","hair","loss","dandruff","athletes","foot","fingernail","fungus","fungal","toenails","MRSA","bladder","infecton","malaria","prevention","preventing","malaria","prostatitis","family","flu","outbreak","i","was","in","a","risk","group","frontline","pharmacist","acid","reflux","pre-barrett","errosion","of","the","esophagus","indigestion","kidney","infection","pneumonia","urinary","infection","shingles","RA","spondolitis","ankylizing","spondolitis","ulcerative","colitis","severe","poison","ivy","all","over","face","migraine","relief","migraine","headaches","idiopathic","excema","eczema","atopic","dernatitis","interstitial","cystitis","pentasa","melasma","stomach","nervousness","GERD","arthritis","nausea","after","eating","heartburn","functional","dyspepsia","gastrointestinal","disorder","excess","acidity","reflux","gastritis","atrial","fibulation","hay","fever","type","allergy","reactions","tachycardia","an","unknown","EKG","wave","abnormality","menopausal","symptoms","sleep","disturban","menopause","incontinence","high","cholestrol","cholestrol","problems","with","my","prostate","BPH","surgical","menopause","perimenopause","hormone","replacement","therapy","night","sweats","menopause","symptoms","hypercholestrolemia","very","high","cholestrol","hysterectomy","total","hysterectomy","contraceptive","oral","contraceptive","hormone","replacement","","unable","to","sleep","contraception","originally","brain","lesions","then","lower","cholestrol","pregnancy","avoidance","LDL","cholestrol","skin","breakouts","birth","control","unregulated","periods","preventing","pregnancy","ovarian","cysts","diaheria","assc","chemo","IBS","DVT","heart","murmer","leg","blood","clot","hyperhidrosis","blood","thinning","circulation","during","pregnancy","blood","clot","as","a","cause","of","early","stage","misscarriage","hypothyroidism","hypothyroid","problem","low","thyroid","levels","hypothyroid","low","thyroid","TSH","level","was","low","no","clinical","symtoms","panic","disorder","tonic","clonic","seizures","bipolar","disorder","seizure","disorder","seizures","anticonvulsant","simple","partial","seizure","grand","mal","seizures","right","temporal","lobe","epilepsy","tri","geminal","neuralgia","ADHD","anti-depressant","lose","weight","major","chronic","depressive","disorder","overeating","weight","gain","over","eating","reduce","wieght","gain","weight","loss","joint","issues","muscular","issues","fibro","musle","relaxant","clinical","depression","severe","anxiety","head","injuries","bipolar","disorder","II","smoking","cessation","smoking","high","level","of","prolactin","psoriatic","arthritis","restless","leg","syndrome","pain","in","legs","diagnosis","restless","leg","syndrome","morning","sickness","delayed","gastric","emptying-nausea","agitation","management","r/t","lewy","body","syndrome","demen","glaucoma","itchy","watery","eyes","psosiasis","sinus","allergies","chronic","idiopathic","urthicaria","with","pruritis","allergic","rhinitis","chest","pain","palpitations","cardiomyopathy","heart","high","interoccular","pressure","general","fluid","retention","conns","syndrome","high","LDL","gout","lupus","basal","cell","carcinoma","scar","revision","bowens","cancer","on","tip","of","nose","post","breast","cancer","breast","cancer","eostrogen-positive","breast","cancer","hyper","pigmentation","wrinkles","anti","ageing","prolactinoma","","prolactin","inhibitor","partial","hysterectomy","HRT","hysterectomy","frequent","urination","kidney","pain","difficult","urination","muscle","strain","uterine","fibroids","heavy","bleeding","endometriosis","CFS","sleeplesness","hypokalemia","environmental","allergies","none","adult","ADD","low","blood","pressure","skipped","beats","hernia","teeth","problems","severe","head","pain","feel","like","throwing","up","sleep","problems","shy","overal","healthy","sarcoidosis","insulin","resistance","secondary","joint","inflammation","from","the","crohns","colitis","a-fib","undifferentiated","connective","tissue","disease","coronary","artery","disease","rosacea","on","face","recent","BCG","wash","after","polyps","removed","in","baldder","broken","leg","torn","acl","shunt","was","replaced","cancer","within","lung","spinal","column","arteries","etc","cancer","of","the","esophagus","chronic","tiredness","joint","pain","eating","disorder-Bulimia","anorexia","post-partum","depression","PTSD","arthritis","migraine","hashimotos","thyroiditis","vitiligo","HBP","ventricular","tachycardia","hay","fever","seasonal","sinus","extreme","diarrhea","upset","stomach","arm","pain","hands","numbness","asteproesis","severe","spasms","severe","osteoarthritis","polymyalgia","rheumatica","whiplash","thyroid","disease","severe","headaches","brusing","swelling","osteopenia","recovery","from","vein","surgery","tearfullness","bad","dreams","hepatitis","c","celiac","disease","diabetes","type","2","perennial","allergic","rhinitis","irregular","heartbeat","sinus","problems","AV","reentry","tachycardia","tiredness","pain","all","over","restless","legs","extreme","chronic","dysphasia","osteopena","hormone","changes","-","weaning","baby","at","time","pregnancy","high","blood","pressure","osteoporosis","sudden","anxiety","for","1st","time","scaring","possible","strep","throat","diarrhea","rash","reaction","no","sleep","horrible","diaper","rash","","nasal","cogestion","eyes","swelling","took","the","medication","few","day","after","recovering","from","chicken","pox","adult","acne","hair","thinning","light","allergies","mitral","valve","prolapse","hyperpigmentation","chills","kidney","scarring","chronic","anemia","stomach","upset","twitching","of","eyes","possibly","hypochondria","bacterial","skin","infection","fingernail","had","to","be","clipped","off","misc","not","applicable","numbness","in","arm","indigestion","through","the","night","kidney","area","bronchiectasis","ramsay-hunt","syndrome","enlarged","pores","pits","over","the","skin","blemishes","over","the","skin","sjogrens","syndrome","skin","allergies","cold","sores","sometimes","on","the","lips","and","under","the","nose","lyme","disease","sinus","stuffiness","frequent","colds","fine","lines","and","wrinkles","overall","healthy","eating","while","not","hungry","to","calm","my","stomach","colostomy","ulcer","poor","digestive","assimilation","dry","skin-childhood","excema","diabetes","type","I","SOB","continual","lack","of","control","over","bladder","due","to","chemical","imbalance","mitral","valve","murmer","mood","swings","depressed","mood","rynauds","syndrome","PAT","irregular","menstrual","mycles;painful","menstruations","multiple","schlerosis","digestive","disorder","no","sex","drive","TIA","mouth","sores","urge","incontinence","wetting","at","night","mild","hypertension","autism","developmental","delay","post","traumatic","stress","major","depression","taken","after","identified","AVM","prior","to","surgery","atrial-fib","stroke","dry","mouth","mild","headaches","hypoglycemia","sleep","issues","due","to","pain","but","was","alleviated","by","meds","facial","nerve","pain","upper","back","pain","generaly","healthy","schitzophrenia","inreased","sweating","at","night","mild","dehydration","trouble","sleeping","at","times","sexual","dysfunction","","menopausal","midly","elevated","Prolactin","pregnant","vomiting","abdominal","surgery","anorexia","nervosa","obesity","SVTs","osteoporosis","ocular","hypertension","hypertention","AS","elevated","blood","pressure","brachioradial","pruritis","cervical","radiopathy","ADD","hypogonadism","post","nasal","drip","aortic","insufficiency","chronic","back","pain","apnea","overweight","BP","thinning","hair","on","crown","and","temples","anemia","food","allergies","dermatomyositis","hypothyroidism","","low","thyroid","netropenia","actinic","keratoses","under-active","thyroid","sensitive","skin","chronic","fatigue","syndrome","barrettes","esophagus","previous","hysterectomy"];
    NoMeaaningWords=["to","after","the","of","from","","and","in","over","due","on","my","was","at","a","type","an","i","then","as","for","day","by"]
    SizeofCondition=len(ConditionList)
    TfIdf= [[(i,j) for j in range(2)] for i in range(SizeofCondition)] 
    for i in range(0,len(ConditionList)):
        TfIdf[i][1]=0;
    jj=0;maxfrequency=0;
    for i in range(0,len(ConditionList)):
        ii=0;detected=0;meaning=1;
        for j in range(0,len(NoMeaaningWords)):
            if ConditionList[i]==NoMeaaningWords[j]:
                meaning=0;
        if meaning == 1:
            while(detected==0 and ii<len(TfIdf)-1):
                if(TfIdf[ii][0]==ConditionList[i]):
                    detected=1;
                    TfIdf[ii][1]=TfIdf[ii][1]+1;
                    if TfIdf[ii][1]>maxfrequency:
                        maxfrequency=TfIdf[ii][1]
                ii=ii+1;  
            if detected==0:
                TfIdf[jj][0]=ConditionList[i]
                TfIdf[jj][1]=1
                jj+=1
            
    NumberOfWord=jj;
    jj=0;
    NewTfIdf= [[(i,j) for j in range(2)] for i in range(NumberOfWord)] 
    for i in range(0,34):
        for j in range(0,NumberOfWord):
            if  TfIdf[j][1]==34-i:
                NewTfIdf[jj][0]=TfIdf[j][0]
                NewTfIdf[jj][1]=TfIdf[j][1]
                jj=jj+1;
    return NewTfIdf,NumberOfWord


def Tagger(FileName,DFileName,NewTfIdf,NumberOfWord):
    K=open(FileName,"r")           
    SizeofDataset=0;
    content=K.readline()
    cont=content.strip().split(",");
    SizeofDataset=int(cont[0])
     
    DataSet= [[(i,j) for j in range(14)] for i in range(SizeofDataset)] 
    for i in range(0,SizeofDataset):
        content=K.readline()
        cont=content.strip().split(",");
        for j in range(0,14):
            DataSet[i][j]=cont[j];
    
    D=open(DFileName,"r") 
    NumberofDrug=480
    DrugList= [[(i,j) for j in range(2)] for i in range(SizeofDataset)] 
    D.readline()
    j=0
    for i in range(0,NumberofDrug):
        Temp=D.readline().split(",")
        DrugList[j]=Temp[0]
        print(DrugList[j])
        j+=1
            
    
    DrugList= [[(i,j) for j in range(2)] for i in range(NumberofDrug)] 
    jj=0;
    for i in range(2,SizeofDataset-7):
        ii=0;detected=0;
        while(detected==0 and ii<NumberofDrug):
            if(DrugList[ii]==DataSet[i-2][6]):
                detected=1;
            ii=ii+1;  
        if detected==0:
            DrugList[jj]=DataSet[i-2][6]
            jj+=1
    
    
    
    PreProcessDataSet= [[(i,j) for j in range(14)] for i in range(SizeofDataset-2)]     
    for i in range(2,SizeofDataset):
        if  DataSet[i][0]=="patient": #patient = 1 ;care giver = 2;
            PreProcessDataSet[i-2][0]=1;
        else:
            PreProcessDataSet[i-2][0]=2;
        print(i)
        PreProcessDataSet[i-2][1]=int(DataSet[i][1]);   #age
        if  DataSet[i][2]=="female": #female = 1 ;male = 2;
            PreProcessDataSet[i-2][2]=1;
        else:
            PreProcessDataSet[i-2][2]=2;
            
          
        contr=DataSet[i][3].replace(";"," ");
        contr=contr.replace("  "," ");
        contr=contr.replace("/"," ");
        cont=contr.strip().split(" ");   
        print(cont)
        Tag=0;
        searchsize=min(4,len(cont))
        print(len(cont),searchsize)
        for m in range(0,searchsize):
            ii=0;detected=0;
            while(detected==0 and ii<NumberOfWord-1):
                if(cont[m]==NewTfIdf[ii][0]):
                    detected=1;
                
                ii=ii+1; 
            if detected==1:
                Tag=Tag+math.pow(1000,m)*ii
        PreProcessDataSet[i-2][3]=int(Tag)
        
        contr=DataSet[i][4].replace(";"," ");
        contr=contr.replace("  "," ");
        contr=contr.replace("/"," ");
        cont=contr.strip().split(" ");   
        print(cont)
        Tag=0;
        searchsize=min(4,len(cont))
        print(len(cont),searchsize)
        for m in range(0,searchsize):
            ii=0;detected=0;
            while(detected==0 and ii<NumberOfWord-1):
                if(cont[m]==NewTfIdf[ii][0]):
                    detected=1;
                
                ii=ii+1; 
            if detected==1:
                Tag=Tag+math.pow(1000,m)*ii
        PreProcessDataSet[i-2][4]=int(Tag)        
            
        #Column 5 not proccessed yet
        
        cont=DataSet[i][6]
        ii=0;detected=0;
        while(detected==0 and ii<NumberofDrug-1):
            if(cont==DrugList[ii]):
                detected=1;
            ii=ii+1; 
        PreProcessDataSet[i-2][6]=ii  
        
        #
        
        PreProcessDataSet[i-2][8]=int(DataSet[i][8]);   #Rate
        
        if  DataSet[i][9]=="Highly Effective": #Highly Effective = 1 Considerably Effective = 2 Moderately Effective = 3 Marginally Effective = 4 Ineffective = 5
            PreProcessDataSet[i-2][9]=1;
        elif DataSet[i][9]=="Considerably Effective":
            PreProcessDataSet[i-2][9]=2;
        elif DataSet[i][9]=="Moderately Effective":
            PreProcessDataSet[i-2][9]=3;
        elif DataSet[i][9]=="Marginally Effective":
            PreProcessDataSet[i-2][9]=4;
        elif DataSet[i][9]=="Ineffective":
            PreProcessDataSet[i-2][9]=5;
          
            
    
        contr=DataSet[i][10]
        cont=contr.strip().split(" ");
        
        NumTag=0;
        lengUnit=0;
        if "mg/day" in cont[0]:
            lengUnit=6;NumTag=1;
        elif "mg" in cont[0]:
            lengUnit=2;NumTag=2;
        elif "pill" in cont[0]:
            lengUnit=4;NumTag=3;
        elif "puff" in cont[0]:
            lengUnit=4;NumTag=4;
        elif "inhalation" in cont[0]:
            lengUnit=10;NumTag=5;
        elif "tablet" in cont[0]:
            lengUnit=6;NumTag=6;
        elif "tab" in cont[0]:
            lengUnit=3;NumTag=7;
        elif "capsule" in cont[0]:
            lengUnit=7;NumTag=8;
        elif "spoon" in cont[0]:
            lengUnit=5;NumTag=10;
        elif "teaspoon" in cont[0]:
            lengUnit=8;NumTag=11;
        elif "drop" in cont[0]:
            lengUnit=4;NumTag=12;
        elif "ml" in cont[0]:
            lengUnit=2;NumTag=13;
        elif "ounce" in cont[0]:
            lengUnit=5;NumTag=14;
        elif "cc" in cont[0]:
            lengUnit=2;NumTag=15;
        elif "mcg" in cont[0]:
            lengUnit=3;NumTag=16;
        elif "sprays" in cont[0]:
            lengUnit=6;NumTag=17;
        elif "patch" in cont[0]:  
            lengUnit=5;NumTag=18;
        #elif "g" in cont[0]:
        #    lengUnit=1;NumTag=17;
        
        if NumTag>0:
            ti=len(cont[0])-lengUnit-1
            Temp=cont[0]
            TagTemp=""
            while ti>-1:
                TagTemp=Temp[ti]+TagTemp
                ti=ti-1;
            if len(TagTemp)>0:
                print(i,"++++++++++++++++",cont[0])
                intTag=math.floor(float(TagTemp)*10)
                NumTag=intTag*100+NumTag
        
            LenCont=len(cont);
            TNumTag=0;TempVar=0;detectedij=0;
            for ij in range(1,LenCont):
                if "EveryNight" in cont[ij]:
                    lengUnit=10;TNumTag=1;detectedij=ij;
                elif "EveryMorning" in cont[ij]:
                    lengUnit=12;TNumTag=2;detectedij=ij;
                elif "WhenNecessary" in cont[ij]:
                    lengUnit=13;TNumTag=3;detectedij=ij;
                elif "TimePerDay" in cont[ij]:
                    lengUnit=10;TNumTag=4;detectedij=ij;
                elif "TimePerWeek" in cont[ij]:
                    lengUnit=11;TNumTag=5;detectedij=ij;
                elif "TimePerYear" in cont[ij]:
                    lengUnit=11;TNumTag=6;detectedij=ij;
                elif "SeparateTimes" in cont[ij]:
                    lengUnit=13;TNumTag=7;detectedij=ij;
                elif "Every2Week" in cont[ij]:
                    lengUnit=10;TNumTag=8;TempVar=2;detectedij=ij;
                elif "Every8Week" in cont[ij]:
                    lengUnit=10;TNumTag=9;TempVar=8;detectedij=ij;
                elif "Every15Day" in cont[ij]:
                    lengUnit=10;TNumTag=10;TempVar=15;detectedij=ij;  
                elif "Every2Hours" in cont[ij]:
                    lengUnit=11;TNumTag=11;TempVar=2;detectedij=ij; 
                elif "Every4Hours" in cont[ij]:
                    lengUnit=11;TNumTag=12;TempVar=4;detectedij=ij;  
                elif "Every5Hours" in cont[ij]:
                    lengUnit=11;TNumTag=13;TempVar=5;detectedij=ij;
                elif "Every6Hours" in cont[ij]:
                    lengUnit=11;TNumTag=14;TempVar=6;detectedij=ij; 
                elif "Every8Hours" in cont[ij]:
                    lengUnit=11;TNumTag=15;TempVar=8;detectedij=ij; 
                elif "Every10Hours" in cont[ij]:
                    lengUnit=12;TNumTag=16;TempVar=10;detectedij=ij; 
                elif "Every12Hours" in cont[ij]:
                    lengUnit=12;TNumTag=17;TempVar=12;detectedij=ij; 
                elif "Every48Hours" in cont[ij]:
                    lengUnit=12;TNumTag=18;TempVar=48;detectedij=ij; 
                elif "Every72Hours" in cont[ij]:
                    lengUnit=12;TNumTag=19;TempVar=72;detectedij=ij; 
                elif "StandardDosage" in cont[ij]:
                    lengUnit=14;TNumTag=20; 
            if TNumTag>3 and TempVar==0:
                ti=len(cont[detectedij])-lengUnit-1
                Temp=cont[detectedij]
                TagTemp=""
                while ti>-1:
                    TagTemp=Temp[ti]+TagTemp
                    ti=ti-1;
                print(contr,TagTemp)
                if len(TagTemp)>0:
                    TempVar=math.floor(float(TagTemp))
                    print(TempVar)
                
            NumTag=TNumTag*100000+NumTag
            NumTag=TempVar*1000000+NumTag
        PreProcessDataSet[i-2][10]=int(NumTag)
    return PreProcessDataSet,NumberofDrug,DataSet,DrugList
