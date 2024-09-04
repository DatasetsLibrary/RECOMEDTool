# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:27:20 2022

@author: IsmailGhodsollahee
"""
import DrugFeatureLib as DI

listDr=DI.drugMapper("druglist.txt")

import os
listOfSides=[]

n=0
for i in range(len(listDr)):
    listOfList=[]
    if len(listDr[i])>2:
        for files in os.walk("DatasetAddress"+listDr[i][2]):
            listOfList.append(files)
        n=n+1

    if len(listOfList)>0:
        if len(listOfList[0])>0:
            print(listOfList[0][1])
            for j in range(len(listOfList[0][1])):
                if (len(listOfSides)==0):
                    listOfSides.append(listOfList[0][1][j])
                else:
                    isnew=0
                    for m in range(len(listOfSides)):
                        if listOfSides[m]==listOfList[0][1][j]:
                            isnew=1   
                    if isnew==0:
                        listOfSides.append(listOfList[0][1][j])

SideEffectArray=[]
for i in range(len(listDr)):
    listOfList=[]
    temp=[]
    if len(listDr[i])>2:
        for files in os.walk("DatasetAddress"+listDr[i][2]):
            listOfList.append(files)
        n=n+1
        temp.append(listDr[i][2])

    if len(listOfList)>0:
        if len(listOfList[0])>0:
            print(listOfList[0][1])
            for j in range(len(listOfList[0][1])):
                for m in range(len(listOfSides)):
                    if listOfSides[m]==listOfList[0][1][j]:
                        temp.append("1")   
                    else:
                        temp.append("0")
    SideEffectArray.append(temp)

K=open("Dataset.csv","r",encoding='utf8') 
SizeofDataset=0;
content=K.readline()
cont=content.strip().split(",");
SizeofDataset=cont[0]
TxtBenefits=""
for i in range(1,int(SizeofDataset)+3):
    Chars=K.readline();
    cont=Chars.strip().split(",");
    TxtBenefits=TxtBenefits+cont[11]
K.close()
TxtbenefitList=TxtBenefits.split(" ")
listOfBenefit=[]
for i in range(len(TxtbenefitList)):
    print(i/len(TxtbenefitList)*100,"%")
    if len(TxtbenefitList[i])>4:
        if (len(listOfBenefit)==0):
            listOfBenefit.append([TxtbenefitList[i],0])
        else:
            isnew=0
            for m in range(len(listOfBenefit)):
                if listOfBenefit[m][0]==TxtbenefitList[i]:
                    isnew=1   
                    listOfBenefit[m][1]=listOfBenefit[m][1]+1
            if isnew==0:
                listOfBenefit.append([TxtbenefitList[i],0])
listOfBenefit2=[]
for i in range(len(listOfBenefit)):
    if listOfBenefit[i][1]>6 and listOfBenefit[i][0]!="almost" and listOfBenefit[i][0]!="other" and listOfBenefit[i][0]!="three" and listOfBenefit[i][0]!="There" and listOfBenefit[i][0]!="didn't" and listOfBenefit[i][0]!="hours" and listOfBenefit[i][0]!="within" and listOfBenefit[i][0]!="while" and listOfBenefit[i][0]!="before" and listOfBenefit[i][0]!="which" and listOfBenefit[i][0]!="first" and listOfBenefit[i][0]!="every" and listOfBenefit[i][0]!="after" and listOfBenefit[i][0]!="because" and listOfBenefit[i][0]!="without" and listOfBenefit[i][0]!="should" and listOfBenefit[i][0]!="where" and listOfBenefit[i][0]!="three" and listOfBenefit[i][0]!="could":
        listOfBenefit2.append(listOfBenefit[i])





D=open("DrugFeatureSet.csv","w",encoding='utf8')

Categories=["Acetylcholine-Agonists","Adrenergic-Alpha-Agonists","Adrenergic-Alpha-Antagonists","Adrenergic-Beta-Agonists","Adrenergic-Beta-Antagonists","AIDS-HIV","Alkylating-Agents","Alzheimers-Disease","Aminoglycosides","Analgesics-Pain-Relievers","Anesthesia-Adjuvants","Anesthetics","Angiotensin-Converting-Enzyme-Inhibitors","Angiotensin-II-Receptor-Antagonists","Anthelmintics","Anti-Allergic-Agents","Anti-Anxiety-Agents","Anti-Arrhythmia-Agents","Anti-Bacterial-Agents","Anti-Infectives-Non-Systemic","Anti-Infectives-Systemic","Anti-Inflammatory-Agents","Anti-Ulcer-Agents","Antiarrhythmic-Agents","Anticholesteremic-Agents","Anticholinergic-Agents","Anticoagulants","Anticonvulsants","Antidepressants","Antidyskinetics","Antiemetics","Antifungal-Agents","Antifungals","Antiglaucomic-Agents","Antihistamines","Antihypertensive-Agents","Antihypoparathyroid-Agents","Antilipemic-Agents","Antimalarials","Antimanic-Agents","Antimetabolites","Antinematodal-Agents","Antineoplastics-Cancer-Treatments","Antiprotozoals","Antipruritics","Antipsychotics","Antiresorptives","Antirheumatic-Agents","Antispasmodics","Antithyroid-Agents","Antitussives","Antiviral-Agents","Appetite-Stimulants","Appetite-Suppressants","Barbiturates","Benzodiazepines","Biological-Response-Modifiers","Biologicals","Bisphosphonates","Blood-Modifiers","Bone-Metabolism-Regulators","Bronchodilator-Agents","Calcium-Channel-Blockers","Carbonic-Anhydrase-Inhibitors","Cardioprotectors","Cardiotonic-Agents","Cardiovascular-Agents","Central-Nervous-System-Depressants","Central-Nervous-System-Stimulants","Cephalosporins","Cholinesterase-Inhibitors","Coagulants","Contraceptives","Cyclooxygenase-Inhibitors","Cystic-Fibrosis","Diabetes-Management","Dihydropyridines","Diuretics","Dopamine-Agents","Dopamine-Agonists","Dopamine-Antagonists","Dopamine-Uptake-Inhibitors","Enzyme-Inhibitors","Erectile-Dysfunction","Estrogens","Excitatory-Amino-Acid-Antagonists","Fibrinolytic-Agents","Folic-Acid-Antagonists","Gaba-Modulators","Gastrointestinal-Agents","Glucocorticoids","Gout","Histamine-H1-Antagonists","HMG-COA-Reductase-Inhibitors","Hormones","Hypocalcemia","Immunomodulators","Immunosuppressants","Infertility","Lipoxygenase-Inhibitors","Mast-Cell-Stabilizers","Migraine","Multiple-Sclerosis","Muscarinic-Antagonists","Muscle-Relaxants","Narcotic-Antagonists","Nasal-Preparations","Neuroprotective-Agents","Norepinephrine-Reuptake-Inhibitors","Nucleic-Acid-Synthesis-Inhibitors","Nucleoside-Analogs","Obesity-Weight-Control","Ophthalmic-Preparations","Opioid-Analgesics","Osteoporosis","Otic-Preparations","Oxytocics","Parasympatholytics","Parasympathomimetics","Parkinsons-Disease","Penicillins","Phenothiazines","Photosensitizing-Agents","Platelet-Aggregation-Inhibitors","Prostaglandins","Protease-Inhibitors","Proton-Pump-Inhibitors","Psychotherapeutic-Agents","Quinolones","Radiation-Protective-Agents","Respiratory-Agents","Reverse-Transcriptase-Inhibitors","Sedatives-Hypnotics","Selective-Serotonin-Agonists","Selective-Serotonin-Reuptake-Inhibitors","Serotonin-Antagonists","Smoking-Cessation","Sulfonamides","Sulfonylureas","Sympatholytics","Sympathomimetics","Tetracyclines","Thrombolytic-Agents","Thrombotic-Agents","topical-agents-skin-and-mucous-membranes","Tricyclic-Antidepressants","Urinary-Tract-Agents","Vaginal-Preparations","Vasoconstrictor-Agents","Vasodilators"]
TxtBenefits=""
for i in range(1,len(Categories)):
    TxtBenefits=TxtBenefits+Categories[i]+","
TxtBenefits=TxtBenefits+"\n"
D.writelines(TxtBenefits)
TxtBenefits=""    
for i in range(1,len(listOfBenefit2)):
    TxtBenefits=TxtBenefits+listOfBenefit2[i][0]+","
TxtBenefits=TxtBenefits+"\n"
D.writelines(TxtBenefits)
TxtBenefits=""
for i in range(1,len(listOfSides)):
    TxtBenefits=TxtBenefits+listOfSides[i]+","
TxtBenefits=TxtBenefits+"\n"
D.writelines(TxtBenefits)

K.close();
D.close();    
      
