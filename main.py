import numpy as np 
import json
print("Grade Calculator by TanErIsTIQUe v1.0")
def agno(credit:list,grade:list,l:int,kr_LastSem=None,nxkr_lastSem=None):
    """The parameters that agno function needs must be given by config.json
    To give your lesson credits write them on credits_current_semester at config.json.
    To give your grades write them as letter grade on givenLetterCredits at config.json example ["AA","BB",...].
    To give your credits for last semester or semesters which is kr_LastSem in agno function write them on credit_sums_of_past_semesters 
    as array they are None by default.
    so write them like [25.5,..] example as format at config.json.
    To give your nxkr, for the last semester or semesters, which is nxkr_lastSem in agno function write them on nxkrPast_semesters as array they are None by default.
    so write them like [25.5,..] example as format at config.json.
    Please do not touch on N which defines the float values for letter grades at config json!!!
    As user you have nothing to change in source file just make required configuration explained above at config.json!
    Also an example is given on README.md to show how to configure config.json file.
    """
    kr=[*credit]
    kr_s=np.array(kr).sum()
    kr_s+=kr_LastSem if kr_LastSem!=None else 0
    n=[*grade]
    nxkr=np.array([kr[i]*n[i] for i in range(l)]).sum()
    nxkr+=nxkr_lastSem if nxkr_lastSem!=None else 0
    ano=nxkr/kr_s
    AGNO=round(nxkr/ano if kr_LastSem==None or nxkr_lastSem==None else nxkr/kr_s )  
    print(f'\nCredits : {kr} \nsum of credits : {kr_s}\nLetter Grades : {n}\nnxkr : {nxkr}\nano : {ano}\nagno is {AGNO}')
def didIpast(ssi:float,absence:float,final:float):
    """Check if student passed.This function will work if all the sections in Grades key are filled """
    note=((absence*0.20)+(ssi*0.80))*0.20+final*0.80
    print("You are passed from the calculated lesson!" if note>=60.0 else "Failed from the calculated lesson!")
def howMuchtoPast(ssi:float,absence:float):
    "Check required final exam point for student this function will work if only final section in Grades at config.json remained null"

    need=abs((60-((absence*0.20)+(ssi*0.80)))/0.80)
    print(f'You must get {need} point to pass from the calculated lesson!')
#load json file 
with open('config.json') as conf:
    file=json.load(conf)
    conf.close()
#definitions of basic objects for calculations 
letter_grades=file['Credits']['givenLetterCredits']
letter_grades_meanings=file['Credits']['N']
credits=file['Credits']['credits_current_semester']
past_semesters_credits=np.array(file['Credits']['credit_sums_of_past_semesters']).sum()
nxkr_past=np.array(file["Credits"]["nxkrPast_semesters"]).sum()
ssiGrade=file['Grades']['ssi']
absenceGrade=file['Grades']['absence']
finalExamGrade=file['Grades']['final']
#print("letter_grades are ",letter_grades) #remove to see how was the grades before translation from letter to float
count=0
#convert letter grades to float values
for word in letter_grades:
    for j in range(len(letter_grades_meanings)):
        if word in letter_grades_meanings[j].keys():
            word=letter_grades_meanings[j][word]
            letter_grades[count]=word
    count+=1
#print("letter_grades are ",letter_grades) #remove in case you want to see if for statement makes its task properly
agno(credits,letter_grades,len(credits),past_semesters_credits,nxkr_past)
if (finalExamGrade==None and ssiGrade!=None) and absenceGrade!=None:
    howMuchtoPast(ssiGrade,absenceGrade)
elif (finalExamGrade!=None and ssiGrade!=None) and absenceGrade!=None:
    didIpast(ssiGrade,absenceGrade,finalExamGrade)
else:
    print("You have to write ssi and absence values at least to be able to make a calculation on a specific lesson.")
