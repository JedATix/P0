import re
import MainFunctions as M
class Mypatient:
    def __init__(self,age,gender,name):
        self.name = str(name)
        self.age= int(age)
        self.gender = str(gender)         
    
    def Get_Patient_Info(Name,Age,Gender)->dict:
        obj = Mypatient(Name,Age,Gender)
        return dict(obj.__dict__)  

    


class Patient_Records:
    def __init__(self, Patient_ID,Details):    
        self.ID = int(Patient_ID)    
        self.Details = str(Details)
            


    def Get_Details(Patien_ID,Details)->dict:

        Obj = Patient_Records(Patien_ID,Details)
        return dict(Obj.__dict__)

    def  Display_Patient_Records(Patient_ID)->list:
        L = []
        St = open("PatientRecords.json",'r').read()
        Temp = St[1:(len(St)-1)].replace('}, {','}|{')
        T = Temp.split('|')        
        for elem in T:
            if Patient_ID in elem:
                L.append(f"{elem} \n........................................................." )
        return L



