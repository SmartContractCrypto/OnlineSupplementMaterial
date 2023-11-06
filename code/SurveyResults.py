import pandas as pd
import numpy as np
import re
from collections import Counter

def print_section_header(header_text):
    print("-" * 60, header_text, "-" * 60)


survey = pd.read_csv("../data/6_Survey_Result.CSV")
columns = list(survey.iloc[[0]])


# Demographics
print_section_header("Demographics")
print("Valid Responses:",len(survey))
print("Main Roles of participants:", dict(Counter(survey[columns[1]].tolist())))
Years = [float(x) for x in survey[columns[2]].to_list()]
print(f"Experience in years (avg: {sum(Years)/len(Years):.2f}, min: {min(Years)}, max: {max(Years)}, median: {np.median(Years):.2f}, std: {np.std(Years, ddof=1):.2f})")

print_section_header("Cryptographic Practices")
UsedAPIs = survey[columns[4]].to_list()
UsedAPIs = [re.split(';|┋',x) for x in UsedAPIs]
API2Count={}
for APIs in UsedAPIs:
    for i in APIs:
        i=i.strip().split(' ')[0].lower()
        if i not in API2Count:
            API2Count[i]=1
        else:
            API2Count[i]=API2Count[i]+1
API2Count.pop("none")
API2Ratio = {key: value / len(survey) for key, value in API2Count.items()}
print("Crypto APIs used by Participants:", API2Ratio)

FamiliarPrimitives = survey[columns[5]].to_list()
FamiliarPrimitives = [re.split(';|┋',x) for x in FamiliarPrimitives]
Primitives2Count={}
for primitives in FamiliarPrimitives:
    for i in primitives:
        i=i.strip().split(' ')[0]
        if i not in Primitives2Count:
            Primitives2Count[i]=1
        else:
            Primitives2Count[i]=Primitives2Count[i]+1
Primitives2Ratio = {}
for key in ["Hash","Signature","Zero-knowledge"]:
    Primitives2Ratio[key] = Primitives2Count[key] / len(survey)
print("Primitives that Participants are familiar with:", Primitives2Ratio)


print_section_header("Obstacles in Practitioners' Perspective")
ImplementationHarder = survey[columns[6]].to_list()
print("Is implementing crypto tasks more challenging than common programming tasks in contracts?", dict(Counter(ImplementationHarder)))

RawObstacles = survey[columns[8]].to_list()
Obstacles = [re.split(';|┋',str(x)) for x in RawObstacles if str(x)!='nan']
Obstacles2Count={}
for obs in Obstacles:
    for i in obs:
        i=i.strip().split('.')[0]
        if i not in Obstacles2Count:
            Obstacles2Count[i]=1
        else:
            Obstacles2Count[i]=Obstacles2Count[i]+1
print(Obstacles2Count)

print_section_header("Template Usage")
prefer2Count={}
PreferTemplatesOrAPI = [str(x) for x in survey[columns[10]].to_list() if str(x)!='' and str(x)!='nan']
for l in PreferTemplatesOrAPI:
    for i in l.split(';'):
        if i in prefer2Count:
            prefer2Count[i]=prefer2Count[i]+1
        elif i!='':
            prefer2Count[i]=1
print(prefer2Count)


print_section_header("API Design")
API_Functionality = [str(x) for x in survey[columns[12]].to_list()]
API_Usability = [str(x) for x in survey[columns[13]].to_list()]
Scale={'(Neutrality)': 3, '(Good)': 4, '(Bad)': 2, '(Very Good)': 5, '(Very bad)': 1}
AllFunctionality = 0
AllUsability = 0
All=0
SatisfiedFunctionality=0
SatisfiedUsability=0
SatisfiedBoth=0
for i in range(0,len(survey)):
    if API_Functionality[i]!="nan":
        AllFunctionality = AllFunctionality+1
        if Scale[API_Functionality[i]]>=4:
            SatisfiedFunctionality = SatisfiedFunctionality + 1
    if API_Usability[i]!="nan":
        AllUsability = AllUsability+1
        if Scale[API_Usability[i]]>=4:
            SatisfiedUsability = SatisfiedUsability + 1
    if API_Functionality[i]!="nan" and API_Usability[i]!="nan":
        All = All + 1
        if Scale[API_Functionality[i]]>=4 and Scale[API_Usability[i]]>=4:
            SatisfiedBoth=SatisfiedBoth+1
        
print("Satisfied with API functionality, usability, and both:", SatisfiedFunctionality/AllFunctionality, SatisfiedUsability/AllUsability, SatisfiedBoth/All)

print_section_header("Security")
SecurityHarder = survey[columns[15]].to_list()
print("Is securing crypto tasks more challenging than common programming tasks in contracts?", dict(Counter(ImplementationHarder)))

rawSWC = [str(x) for x in survey[columns[17]].to_list()]
SWC = [re.split(';|┋',x) for x in rawSWC if x!='']
SWC2Count={}
Number2Count={0:0,1:0,2:0,3:0,4:0,5:0}

for obs in SWC:
    if 'I don\'t understand the question' in obs:
        continue
    if "None of them" not in obs:
        Number2Count[len(obs)]=Number2Count[len(obs)]+1
    else:
        Number2Count[0]=Number2Count[0]+1
    for i in obs:
        i=i.strip().split('.')[0]
        if i not in SWC2Count:
            SWC2Count[i]=1
        else:
            SWC2Count[i]=SWC2Count[i]+1

SWCKnowledge = list(Counter(Number2Count).elements())
print(f"Participants' Knowledge about SWC (avg: {sum(SWCKnowledge)/len(SWCKnowledge):.2f}, min: {min(SWCKnowledge)}, max: {max(SWCKnowledge)}, median: {np.median(SWCKnowledge):.2f}, std: {np.std(SWCKnowledge, ddof=1):.2f})")

print_section_header("Resources and Tools")

ResourceDocumentation = [str(x) for x in survey[columns[18]].to_list() if str(x)!='nan']
Score={'(Neutrality)': 3, '(Good)': 4, '(Bad)': 2, '(Very Good)': 5, '(Very bad)': 1}
print("Participants' Perceptions of current documentation", dict(Counter(ResourceDocumentation)))

ResourceTemplate = [str(x) for x in survey[columns[19]].to_list() if str(x)!='nan']
Score={'(Neutrality)': 3, '(Good)': 4, '(Bad)': 2, '(Very Good)': 5, '(Very bad)': 1}
print("Participants' Perceptions of current template", dict(Counter(ResourceTemplate)))

ResourceTestingTool = [str(x) for x in survey[columns[20]].to_list() if str(x)!='nan']
Score={'(Neutrality)': 3, '(Good)': 4, '(Bad)': 2, '(Very Good)': 5, '(Very bad)': 1}
print("Participants' Perceptions of current testing tool", dict(Counter(ResourceTestingTool)))

ResourceAuditTool = [str(x) for x in survey[columns[21]].to_list() if str(x)!='nan']
Score={'(Neutrality)': 3, '(Good)': 4, '(Bad)': 2, '(Very Good)': 5, '(Very bad)': 1}
print("Participants' Perceptions of current testing tool", dict(Counter(ResourceAuditTool)))
