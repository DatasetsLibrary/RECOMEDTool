import DatLib as DL
import math as ma
Events=DL.LoadDat("Events.DAT",2487,6)
DP=""
Rules=list()
DrNum=-1
TVar=list()
for i in range(2486):
    DN=Events[i][0]
    if DP==DN:
        Rules[DrNum][5]=Rules[DrNum][5]+1
        TVar.append(int(Events[i][1]))
        if Events[i][2]=="male":
            if "death" in Events[i][4] or "disablity" in Events[i][4] or "hospitalization" in Events[i][4]:
                Rules[DrNum][1]=Rules[DrNum][1]+1
                Rules[DrNum][1]=Rules[DrNum][1]/Rules[DrNum][5]
        if Events[i][2]=="female":
            if "death" in Events[i][4] or "disablity" in Events[i][4] or "hospitalization" in Events[i][4]:
                Rules[DrNum][2]=Rules[DrNum][2]+1
                Rules[DrNum][2]=Rules[DrNum][2]/Rules[DrNum][5]
        if "death" in Events[i][4] or "disablity" in Events[i][4] or "hospitalization" in Events[i][4]:
            Rules[DrNum][3]=Rules[DrNum][3]+int(Events[i][1])
            Rules[DrNum][4]=Rules[DrNum][3]/Rules[DrNum][5]        
    else:
        if len(Rules)>1 and Rules[DrNum][5] >0:
            Sigma=0
            for ii in range(len(TVar)):
                Sigma=Sigma+pow((TVar[ii]-Rules[DrNum][4]),2)
            Var=(Sigma)/Rules[DrNum][5] 
            Var=pow(Var,0.5)
            Rules[DrNum][6]=Var
        #Tem=[DrugName,Male,Female,SumAge,MeanAge,Number,Var]
        TVar=0
        TVar=list()
        Rules.append([Events[i][0],0,0,0,0,0,0])
        DrNum=DrNum+1
    DP=DN

RulesP=list()
for i in range(len(Rules)):   
    RulesP.append(Rules[i][0:5])
for i in range(len(Rules)):
    RulesP[i][1]=RulesP[i][1]*10*pow(ma.e,-RulesP[i][1])
    RulesP[i][2]=RulesP[i][2]*10*pow(ma.e,-RulesP[i][2])
    if(Rules[i][5]>0):
        RulesP[i][3]=RulesP[i][4]-(0.96*(Rules[i][6]/pow(Rules[i][5],0.5)))
        RulesP[i][4]=RulesP[i][4]+(0.96*(Rules[i][6]/pow(Rules[i][5],0.5)))
        
DL.SaveDat("Rules.DAT", "Array", 174, 6, RulesP)    

DeathRate=0;
DisaRate=0;
HospRate=0;
WDeathRate=0;
WDisaRate=0;
WHospRate=0;
for i in range(1,2486):
    DN=Events[i][0]
    Age=int(Events[i][1])
    Gen=Events[i][2]
    Adv=Events[i][4]
    let=0
    
    if "death" in Events[i][4]:
        WDeathRate=WDeathRate+1;
    if "disablity" in Events[i][4]:
        WDisaRate=WDisaRate+1
    if "hospitalization" in Events[i][4]:
        WHospRate=WHospRate+1
                    
    for j in range(174):
        if DN==RulesP[j][0]:
            if Gen=="male":
                if RulesP[j][1]<0.25:
                    if "death" in Events[i][4]:
                        DeathRate=DeathRate+1;
                        let=1
                    if "disablity" in Events[i][4]:
                        DisaRate=DisaRate+1
                        let=1
                    if "hospitalization" in Events[i][4]:
                        HospRate=HospRate+1
                        let=1
            else:
                if RulesP[j][2]<0.25:
                    if "death" in Events[i][4]:
                        DeathRate=DeathRate+1;
                        let=1
                    if "disablity" in Events[i][4]:
                        DisaRate=DisaRate+1
                        let=1
                    if "hospitalization" in Events[i][4]:
                        HospRate=HospRate+1
                        let=1
            if Age<RulesP[j][4] and Age>RulesP[j][3] and let==0:
                if "death" in Events[i][4]:
                    DeathRate=DeathRate+1;
                if "disablity" in Events[i][4]:
                    DisaRate=DisaRate+1
                if "hospitalization" in Events[i][4]:
                    HospRate=HospRate+1
  