# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:40:14 2021

@author: IsmailGhodsollahee
"""

import HtmlLib as htm
from os.path import exists

Categories=["Acetylcholine-Agonists","Adrenergic-Alpha-Agonists","Adrenergic-Alpha-Antagonists","Adrenergic-Beta-Agonists","Adrenergic-Beta-Antagonists","AIDS-HIV","Alkylating-Agents","Alzheimers-Disease","Aminoglycosides","Analgesics-Pain-Relievers","Anesthesia-Adjuvants","Anesthetics","Angiotensin-Converting-Enzyme-Inhibitors","Angiotensin-II-Receptor-Antagonists","Anthelmintics","Anti-Allergic-Agents","Anti-Anxiety-Agents","Anti-Arrhythmia-Agents","Anti-Bacterial-Agents","Anti-Infectives-Non-Systemic","Anti-Infectives-Systemic","Anti-Inflammatory-Agents","Anti-Ulcer-Agents","Antiarrhythmic-Agents","Anticholesteremic-Agents","Anticholinergic-Agents","Anticoagulants","Anticonvulsants","Antidepressants","Antidyskinetics","Antiemetics","Antifungal-Agents","Antifungals","Antiglaucomic-Agents","Antihistamines","Antihypertensive-Agents","Antihypoparathyroid-Agents","Antilipemic-Agents","Antimalarials","Antimanic-Agents","Antimetabolites","Antinematodal-Agents","Antineoplastics-Cancer-Treatments","Antiprotozoals","Antipruritics","Antipsychotics","Antiresorptives","Antirheumatic-Agents","Antispasmodics","Antithyroid-Agents","Antitussives","Antiviral-Agents","Appetite-Stimulants","Appetite-Suppressants","Barbiturates","Benzodiazepines","Biological-Response-Modifiers","Biologicals","Bisphosphonates","Blood-Modifiers","Bone-Metabolism-Regulators","Bronchodilator-Agents","Calcium-Channel-Blockers","Carbonic-Anhydrase-Inhibitors","Cardioprotectors","Cardiotonic-Agents","Cardiovascular-Agents","Central-Nervous-System-Depressants","Central-Nervous-System-Stimulants","Cephalosporins","Cholinesterase-Inhibitors","Coagulants","Contraceptives","Cyclooxygenase-Inhibitors","Cystic-Fibrosis","Diabetes-Management","Dihydropyridines","Diuretics","Dopamine-Agents","Dopamine-Agonists","Dopamine-Antagonists","Dopamine-Uptake-Inhibitors","Enzyme-Inhibitors","Erectile-Dysfunction","Estrogens","Excitatory-Amino-Acid-Antagonists","Fibrinolytic-Agents","Folic-Acid-Antagonists","Gaba-Modulators","Gastrointestinal-Agents","Glucocorticoids","Gout","Histamine-H1-Antagonists","HMG-COA-Reductase-Inhibitors","Hormones","Hypocalcemia","Immunomodulators","Immunosuppressants","Infertility","Lipoxygenase-Inhibitors","Mast-Cell-Stabilizers","Migraine","Multiple-Sclerosis","Muscarinic-Antagonists","Muscle-Relaxants","Narcotic-Antagonists","Nasal-Preparations","Neuroprotective-Agents","Norepinephrine-Reuptake-Inhibitors","Nucleic-Acid-Synthesis-Inhibitors","Nucleoside-Analogs","Obesity-Weight-Control","Ophthalmic-Preparations","Opioid-Analgesics","Osteoporosis","Otic-Preparations","Oxytocics","Parasympatholytics","Parasympathomimetics","Parkinsons-Disease","Penicillins","Phenothiazines","Photosensitizing-Agents","Platelet-Aggregation-Inhibitors","Prostaglandins","Protease-Inhibitors","Proton-Pump-Inhibitors","Psychotherapeutic-Agents","Quinolones","Radiation-Protective-Agents","Respiratory-Agents","Reverse-Transcriptase-Inhibitors","Sedatives-Hypnotics","Selective-Serotonin-Agonists","Selective-Serotonin-Reuptake-Inhibitors","Serotonin-Antagonists","Smoking-Cessation","Sulfonamides","Sulfonylureas","Sympatholytics","Sympathomimetics","Tetracyclines","Thrombolytic-Agents","Thrombotic-Agents","topical-agents-skin-and-mucous-membranes","Tricyclic-Antidepressants","Urinary-Tract-Agents","Vaginal-Preparations","Vasoconstrictor-Agents","Vasodilators"]

DrugsCategories=htm.Categorizer("DatasetAdress",Categories)#put All Drug In Categories
Druglist=htm.DrugCategorizer(Categories,DrugsCategories)
  
ExistedFiles=0
ReviewNumber=0
PerTemp = [[(m,n) for n in range(15)] for m in range(0)] 
for i in range(0,len(Druglist)):
    print("->i",i,"-----------")
    print(Druglist[i][0])

    FileNameT="FileAddress"+str(Druglist[i][0])+"/index.html"        
    exist=exists(FileNameT) 
    if exist==True:
        print(FileNameT)
        ExistedFiles=ExistedFiles+1
        debug=0
        #if i>917:
        #    debug=1
        Temp,NumberofReview=htm.HtmOpener(FileNameT,str(Druglist[i][1]),debug)
        ReviewNumber=ReviewNumber+NumberofReview
        
        PerLeng=len(PerTemp)
        NewTemp = [[(m,n) for n in range(15)] for m in range(PerLeng+NumberofReview)] 
        for mm in range (0,PerLeng):
            for nn in range (0,15):
                NewTemp[mm][nn]=PerTemp[mm][nn]
                    
        for mm in range (0,NumberofReview):
            for nn in range (0,15):
                NewTemp[mm+PerLeng][nn]=Temp[mm][nn]
                
        PerTemp=NewTemp


htm.DatasetUpdater("Dataset2.csv","Dataset1.csv",NewTemp)

