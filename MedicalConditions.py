from email.policy import default
from genericpath import exists
import ast
from pickle import NONE, TRUE
import MainFunctions as mf
from indexing import MyIndex
import re




class Medical_Conditions:
    def __init__(self,Condition_Name,Symptoms,Types_Of_medications):
        # Condition name needs to be a string
        # Symptoms need to be a list of strings
        # Types of medications need to be a list of strings 

        self.Name = Condition_Name
        self.Symptoms = Symptoms
        self.Types_of_Medications = Types_Of_medications

    def Add_Medical_Condition()->dict:
        amc = Medical_Conditions("","","")

        while True:
            try:
                a = input("Type in the name of the medical condition: ")
                if re.search('[\),\(,\*,\&,\%,\^,\@,\!,\-,\+]',a)!=None:
                    raise ValueError
                else:
                    if str(a).upper() == "CLOSE":
                        return 0
                    else:
                        amc.Name = a
                        S = 'type in the symptoms one after the other one line at a time and type "end" once completed\n'
                        amc.Symptoms = Medical_Conditions.Get_My_inPut(S) 
                        #print (amc.Symptoms)
                        if amc.Symptoms == []:
                            mf.MyMainFunctions.request_Work(0)
                        else:
                            S = 'type in the medications one after the other one line at a time and type "end" once completed\n'
                            amc.Types_of_Medications = Medical_Conditions.Get_My_inPut(S)
                            if amc.Types_of_Medications == []:
                                mf.MyMainFunctions.request_Work(0)
                                
                        return dict(amc.__dict__)                    
            except ValueError as e:
                print ("YOU CANNOT HAVE SPECIAL CHARACTORS IN THE NAME OF THE MEDICAL CONDITION")
                Medical_Conditions.Add_Medical_Condition()



    def Edit_Medical_Condition(MatchString):
        try:
            while True:
                if re.search('[\),\(,\*,\&,\%,\^,\@,\!,\-,\+]',MatchString)!= None:
                    print("CONDITION NAME CANNOT CONTAIN SPECIAL CHARACTORS")               
                    raise ValueError
                else:
                    amc = Medical_Conditions("","","")
                    A = input("Type in the name of the medical condition to be edited: ")
                    if str(A).upper() =="CLOSE" :
                        return 0
                    elif re.search('[\),\(,\*,\&,\%,\^,\@,\!,\-,\+]',A)!= None:
                        raise ValueError
                    else:
                        amc.Name = A
                        Val = Medical_Conditions.Find_Medical_Condition_To_Be_Edited(open('MedicalConditions.json').read(), MatchString) 
                        if Val == None:
                        # condition not found
                            print ("Condition not found. please check!")
                            mf.MyMainFunctions.request_Work(0)
                        else:
                            S = 'type in the symptoms one after the other one line at a time and type "end" once completed\n'
                            amc.Symptoms = list(Medical_Conditions.Get_My_inPut(S) )
                            if amc.Symptoms ==[]:
                                exit
                            S = 'type in the medications one after the other one line at a time and type "end" once completed\n'
                            amc.Types_of_Medications = list(Medical_Conditions.Get_My_inPut(S))
                            if amc.Types_of_Medications ==[]:
                                exit
                            Tp = dict(amc.__dict__)
                            if list(dict(Tp).values())[1] == [] or list(dict(Tp).values())[1] == [] or list(dict(Tp).values())[1] == '':
                                exit
                            else:
                    
                                St = str(open('MedicalConditions.json','r').read())
                                Temp = St[1:(len(St)-1)].replace('}, {','}|{')
                                T = Temp.split('|')
                                obj = MyIndex(0,"")
                                obj.id = list(dict(ast.literal_eval(T[Val])).values())[0]
                                obj.value = dict(amc.__dict__)
                                for i in range(len(T)):
                                    if i!= Val:
                                        T[i] = dict(ast.literal_eval(T[i]))
                                    else:
                                        T[Val] = dict(obj.__dict__)
                                
                                print ("Would you like to save this. type 'y/Y' else any key")
                                if str(input()).upper() =='Y':
                                    #pass
                                    with open('MedicalConditions.json','w') as W:
                                        W.write(str(T))
                return 0                    
        except ValueError as ve:
            P = input('Enther the name of the conditon to edit:')
            Medical_Conditions.Edit_Medical_Condition(P)






    def Find_Medical_Condition_To_Be_Edited(MyString, MatchString)-> int:
        St = str(open('MedicalConditions.json','r').read())
        Temp = St[1:(len(St)-1)].replace('}, {','}|{')
        T = Temp.split('|')  
        obj = MyIndex(0,"")
        for i in range (len(T)):
            if int(list(dict(list(dict(ast.literal_eval(T[i])).values())[1]).values())[0]) == MatchString:                               
                return i    
            else:
                return None 


        for le in range (0,len(list(ast.literal_eval(MyString)))):
            Tlist = list(dict(list(ast.literal_eval(MyString))[le]).values())[1]
            for eq in dict(Tlist):
                if eq == 'Name':
                    if Tlist[eq]==MatchString:
                        return le
                    else:
                        pass

    def Save_Medical_Condition(MyValues):
        print ("Would you like to save this. type 'y/Y' else any key")
        if str(input()).upper()=="Y":
            A = mf.MyMainFunctions.Save_Info_to_Files(MyValues, "MedicalConditions") 
            return 0 
        else:
            return 1          

    def Get_My_inPut(Comment):
        print (str(Comment))
        MyL = []
        while True:
            inp = str(input()).upper()
            if (inp!='END'and inp!="CLOSE") :
                if re.search('[\),\(,\*,\&,\%,\^,\@,\!,\-,\+]',inp)== None:
                    MyL.append(inp)
                else:
                    print("CONTAINS SPECIAL CHARACTORS")
            else:
                break 
        return MyL

        
            