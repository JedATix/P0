from asyncore import read
from datetime import datetime
from operator import truediv
from pickle import NONE, TRUE
from urllib import request
from MyCredentials import MyCred
from genericpath import exists
import ast
import MedicalConditions as med
from MedicalConditions import Medical_Conditions
import indexing as id
import Patient as pt
import os
import logging
import re

class MyMainFunctions:
    def __init__(self,In):
        self.In = In

    def Error_Logging_Function(Msg):
         logging.basicConfig(filename="Log.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
         logging.info(Msg)

    def Opening_Function (In):
        logging.basicConfig(filename="Log.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
        if In ==0:
            if exists('Credentials.json') != True:
                if MyCred.New_User_Creation() ==0:
                    logging.info("New user Created...")
                    return 0
                else:
                    return 1
                    
            else:
                if MyCred.User_Authentication()==0:
                    logging.info("User Authentication Successfull...")
                    return 0
                else:
                    return 1
        else:
            return 1
    
    def Save_Info_to_Files(MyValues, FileName):
        Ffile = ""
        Obj = id.MyIndex(0,"") 
        Obj.id = 0
        inc = 0
        L=[]
        if FileName == "MedicalConditions":
            Ffile = "MedicalConditions.json"
            
        elif FileName == "Credentials":
            Ffile = "Credentials.json"
        elif FileName == "Patient":
            Ffile = "Patient.json"
        elif FileName == "PatientRecords":
            Ffile = "PatientRecords.json"
        
        if exists(Ffile):
            St = str(open(Ffile,'r').read())
            Temp = St[1:(len(St)-1)].replace('}, {','}|{')
            T = Temp.split('|')
            for i in T:
                Values = dict(ast.literal_eval(i))
                for elem in range (0,len(Values.values()),2):
                    Obj.id = list(Values.values())[elem]
                    inc = list(Values.values())[elem]
                    Obj.value = dict(list(Values.values())[elem+1]) 

                L.append(dict(Obj.__dict__))

            Obj.id = inc+1
            Obj.value =MyValues
            L.append(dict(Obj.__dict__))
            with open(Ffile,'w') as w:
                w.write(str(L)) 
            logging.info(f"new content inclued into {Ffile} ...")
        else:
            Obj.id +=1
            Obj.value = MyValues

            L.append (dict(Obj.__dict__))    
            with open(Ffile,'w') as w:
                w.write(str(L)) 
            logging.info(f"{Ffile} created for the first time and new content inclued into {Ffile} ...")
        return int(Obj.id)
        
    def request_Work(In):

        if str(In).upper() =='Close'.upper():
            return 1
        else: 
            print("\n\nWhat do you want to do? select from the below list\n\n" + 
            "1:Add Medical Condition\t|2:Edit Medical Condition\t|3:Diagnose patient\t|4:View Patient Records\n"+
            "|5:Add New User\t|6:Close \n\n")
            T = str(input())
            if T =='1':
                Tp = med.Medical_Conditions.Add_Medical_Condition()

                if Tp !=0:            
                    if list(dict(Tp).values())[1] == [] or list(dict(Tp).values())[1] == [] or list(dict(Tp).values())[1] == '':
                        Tp = None
                        return 0
                    else:
                        print (f"Details of the medical conditon are: \n\n{Tp}")
                        if Tp != None:
                            if med.Medical_Conditions.Save_Medical_Condition(Tp)==0:
                                return 0
                    logging.info("New Medical Condoition included to the DB ...")                
            elif T =='2':
                P = input('Enther the name of the conditon to edit:')
                print (P)
                Tp = med.Medical_Conditions.Edit_Medical_Condition(P)
                #print (">>>>>",Tp)
                logging.info("Existing Medical Condition has been Updated in the DB ...")     
                return 0
            elif T =='3':
            
                F1 = "MedicalConditions.json"
                F2 = "Credentials.json"

                if (exists(F1) == False or exists(F2)==False):
                    print ("ERROR: ESSENTIAL FILES NOT FOUND. PLEASE INCLUDSE THEM")
                else:
                    # Clear the content of the File
                    with open('Rx.txt','w') as w:
                        w.write("")
                    # Diagnising illness
                    print("\n\n****************************************\n\n"+
                        "            Patient Diagnosis            "+
                        "\n\n****************************************\n\n")
                    MyName = (input("Patient Name:"))
                    #MyName = MyMainFunctions.nameCheck(True,MyName)
                    while True:
                        if ValueError != None:
                            try:
                                if str(MyName).upper()=='Close'.upper():
                                    return 1
                                else:
                                    if re.search('[\),\(,\*,\&,\%,\^,\@,\!,\-,\+]',MyName) !=None:
                                        raise ValueError
                                    else:
                                        break
                            except ValueError as C:
                                print ("YOU CANNOT ENTER SPECIAL CHARACTORS INTO A NAME")
                                MyMainFunctions.Error_Logging_Function("Attempeted to inser special charctors...")
                                MyName = (input("Patient Name:"))

                    MyAge = (input("Patient Age:"))
                    msg= ""
                    while True:
                        if ValueError != None:
                            try:
                                if str(MyAge).upper()=='Close'.upper():
                                    return 1
                                if len(MyAge)>3:
                                    msg = "Age is more than 3 charactors long"
                                    raise ValueError
                                    
                                else:
                                    for elem in MyAge:
                                        if re.search('[A-Z,a-z,\),\(,\*,\&,\%,\^,\@,\!,\-,\+]',elem)!= None:
                                            msg = "Age contains non numeric charactors"
                                            raise ValueError
                                                                        
                                    if int(MyAge)>119:
                                        msg = "Age is greater than 119"
                                        raise ValueError
                                    else:
                                        break
                            except ValueError as D:
                                print (msg)
                                MyMainFunctions.Error_Logging_Function("Attempeted to enter an illogial age...")
                                MyAge = (input("Patient Age:"))


                    Gender = (input ("Enter Gender (M/F):"))
                    while True:
                        if ValueError != None:
                            try:
                                if str(Gender).upper()=='Close'.upper():
                                    
                                    return 1
                                else:    
                                    if str(Gender).upper() == 'M' or  str(Gender).upper() == 'F':
                                        break
                                    else:
                                        raise ValueError
                            except ValueError as de:    
                                print("YOU CAN ONLY ENTER EITHER 'M/F' FOR GENDER")
                                MyMainFunctions.Error_Logging_Function("Invalid gender included...")
                                Gender = (input ("Enter Gender (M/F):"))

                    

                    Condi = []
                    print ("Enter the symptoms of the patient one by one. once completed type 'end' to end list \n\n")
                    while True:
                        A = str(input()).upper()
                        if A  == "CLOSE":
                            return 1
                        else:
                            if A == "END":
                                break
                            else:
                                Condi.append(A)

                    # create percentages of matches for matches with illnesses
                    Var = Medical_Conditions('','','')
                    Obj = id.MyIndex(0,"") 
                    Obj.id = 0
                    L=[]
                    MedMatchList = []
                    St = str(open('MedicalConditions.json','r').read())
                    Temp = St[1:(len(St)-1)].replace('}, {','}|{')
                    T = Temp.split('|')                             
                    C = set()
                    D = dict()
                    for i in T:
                        Values = dict(ast.literal_eval(i)) 
                        Patient_Symptoms_Set = set(Condi)
                        Condition_Name = list(dict(list(Values.values())[1]).values())[0]
                        Symptom_Checking_Set = set(list(dict(list(Values.values())[1]).values())[1])
                        Medication_Checking_List = list(dict(list(Values.values())[1]).values())[2]
                        MyIntercept = Patient_Symptoms_Set.intersection(Symptom_Checking_Set)
                        pct = (len(MyIntercept)/len(Symptom_Checking_Set))*100
                
                        if pct >50:
                            L.append(f"Condion: {Condition_Name} was found with a {pct}% match")
                            MedMatchList.append(set(Medication_Checking_List))

                            C =set(MedMatchList[0])
                            for elem in range(len(MedMatchList)):
                                C = set(MedMatchList[elem]).union(C)
                                for kl in list(MedMatchList[elem]):
                                    if kl in D:
                                        D[str(kl)] = D[str(kl)] +1
                                        
                                    else:
                                        D[str(kl)] = 1

                    if len(L)>0:
                        print (f"the follwoing were found{str(L)}\n")
                        print ("Among the diagnosed conditions commonly used medications include" )
                        for el in range(len(list(D.keys()))):
                            V = int(list(D.values())[el])*100/len(C)
                            print (str(list(D.keys())[el]) + " showing a commonality of " + 
                            "{:.{}f}".format(round(V,2),2))

                        print ("\nand all possible recommdned medications include: ", str(C))
                        print ("type in the medications to be prescribed one by one and type 'end' once completed")

                        Rx = []
                        while True:
                            T =str(input()).upper() 
                            if T !="END" and T!="CLOSE":
                                Rx.append(T)
                            else:
                                break
                                
                        with open("Rx.txt",'w') as W:    
                            W.write(f"Date:{datetime.today().strftime('%d/%m/%Y %H:%M')}\n")
                            W.write(f"Patient Name: {MyName}\n")
                            W.write(f"Gender: {Gender}\n")
                            W.write(f"Age: {MyAge}\n\n")
                            W.write(f"History and Physiology:\n {Condi}\n\n")
                            W.write("Recommended Medications Include:\n")
                            for elem in Rx:
                                W.write(f'{elem}\n')
                            K = input("Enter Doctor Name to certify:")
                            W.write(f"Prescribed by:{K}")
                    else:
                        print ("Patient symptoms are not enough to properly diagnose a condtion. Further investigation required")

                    I = input("Has this ptient being registers at this medical institute? type 'y/Y' for yes, else press any key")
                    if I.upper() == 'Y':
                        Inc = input('Enter Patient ID:')
                        # search for the patient
                        # Enter infor to the consultation recrods                                  
                        St = str(open('Patient.json','r').read())
                        Temp = St[1:(len(St)-1)].replace('}, {','}|{')
                        T = Temp.split('|')
                        obj = id.MyIndex(0,"")
                        for i in range (len(T)):
                            if int(list(dict(ast.literal_eval(T[i])).values())[0]) == int(Inc):
                                obj.id = int(Inc)
                                obj.value = dict(pt.Mypatient.__dict__)
                                T[i]=dict(obj.__dict__)  
                                A = T[i]
                                Fl = pt.Patient_Records.Get_Details(int(Inc),f"Patient symptoms were insuffucuent to provide proper Diagnose on Date:{datetime.today().strftime('%d/%m/%Y %H:%M')}\n")
                                A = MyMainFunctions.Save_Info_to_Files(Fl,"PatientRecords")                                  
                                return 0    
                        return 0
                    else:
                        # getting and saving patient basic detail in to system 
                        A = pt.Mypatient.Get_Patient_Info(MyAge,Gender,MyName)
                        A = MyMainFunctions.Save_Info_to_Files(A,"Patient")

                        # getting and saving patient consultation recrods
                        # first clear contents in file

                        Fl = pt.Patient_Records.Get_Details(A,open('Rx.txt','r').read())
                        A = MyMainFunctions.Save_Info_to_Files(Fl,"PatientRecords")
                        logging.info(f"Running Patient Diagnosis for patient {MyName} ...") 
                        # Display patient prescription
                        if Fl !=None:
                            os.system('Rx.txt')
                        return 0
                return 0
            elif T =='4':
                if exists("Records.txt"):
                    ID = input("Please Enter Patient Id:")
                    L = pt.Patient_Records.Display_Patient_Records(ID)
                    logging.info(f"Retrieving patient records for patient id {ID} ...") 
                    for elem in L:
                        with open("Records.txt",'w') as W:
                            W.write(elem)                
                    os.system("Records.txt")
                    return 0
                else:
                    print("FILE NOT FOUND. PLEASE ENTER PATIENT DETIALS PRIOR TO ACCESSING INFORMATION")
                    print ("DO YOU WANT TO CREATE THE FILE?, TYPE 'Y/Y' ")
                    Abc = input()
                    if str(Abc).upper() == "Y":
                        with open ("Records.txt",'w') as w:
                            w.write ("")
                        ID = input("Please Enter Patient Id:")
                        L = pt.Patient_Records.Display_Patient_Records(ID)
                        logging.info(f"Retrieving patient records for patient id {ID} ...") 
                        for elem in L:
                            with open("Records.txt",'w') as W:
                                W.write(elem)                
                        os.system("Records.txt")                            
                    return 0
            elif T =='5':
                MyCred.New_User_Creation()
                logging.info("Creating new User ...") 
            elif T == '6':
                # closing the console program
                logging.info(f"System Close ...") 
                return 1
            elif T.upper() == "CLOSE":
                logging.info(f"System Close ...") 
                return 1
            else:
                return 0

        
