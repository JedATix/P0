from genericpath import exists
from getpass import getpass
import ast
from ssl import create_default_context
import MainFunctions as M
from indexing import MyIndex
import re
import logging

class MyCred:
    def __init__(self,UserName,Password):
        try:
            if re.search('[\),\(,\*,\&,\%,\^,\@,\!,\-,\+]',UserName) !=None:
                raise ValueError
            else:
                self.UserName = UserName
                self.PassWord = Password
        except ValueError as Vs:
            print ("ERROR! YOU CANNOT HAVE SPECIAL CHARACTORS IN USER NAME") 
            M.MyMainFunctions.Error_Logging_Function("Attempeted to inser special charctors")
            if Vs !=None:
                MyCred.__init__(self, UserName, Password)            

    

    def New_User_Creation():
        S = open("Greeting.txt",'r',encoding="UTF-8").read()
        print ('\n'+S+ '\n')
        print ("Create your username and password")
        T = MyCred.Enter_UserDetails()
        print ("Your user name and password are: ", str(T)) 
        if MyCred.Get_Response_To_Save_Credentials(T) ==0:
            return 0
        else:
            return 1

    def Enter_UserDetails()->dict:
        P= MyCred("","")
        A = input("Enter Username:")

        try:
            if re.search('[\),\(,\*,\&,\%,\^,\@,\!,\-,\+]',A) !=None:
                raise ValueError
            else:
                P.UserName =  A
                P.PassWord = getpass("Enter Password:")
                return P.__dict__
        except ValueError as V:
            print ("ERROR! YOU CANNOT HAVE SPECIAL CHARACTORS IN USER NAME") 
            M.MyMainFunctions.Error_Logging_Function("Attempeted to inser special charctors")
            if V !=None:
                MyCred.Enter_UserDetails()       


    def Get_Response_To_Save_Credentials(UserDetails):
        crd = MyIndex(0,"")    
        print ("Would you like to save this type 'y/Y' else any key")
        if str(input()).upper()=="Y":
            A = M.MyMainFunctions.Save_Info_to_Files(UserDetails, "Credentials")   
            if A>0:
                M.MyMainFunctions.request_Work(0)
            return 0
        else:
            return 1  
    
    def User_Authentication():
        S = open("Greeting.txt",'r',encoding="UTF-8").read()
        print ('\n'+S+ '\n')
        try:
            V1 = input("\tEnter User name\t\t:")
            V2 = ""
            if re.search('[\),\(,\*,\&,\%,\^,\@,\!,\-,\+]',V1) != None:
                raise ValueError
            else:
                if V1.upper() == "CLOSE":
                    return 1
                V2 = getpass("\tEnter Your Password\t:")
                if V2.upper() =="CLOSE":
                    return 1 

                if V2.upper() !="CLOSE" and V1.upper()!="CLOSE":

                    Cb = str(MyCred(V1,V2).__dict__)
                    if str(Cb) in open('Credentials.json','r').read():
                        print (f'****************************************\n\n      Welcome {V1} !\n\n****************************************\n\n')
                        return 0
                    else:
                        return 1 # intended to terminate the program                                       
        except ValueError as Ve:
            print ("ERROR! YOU CANNOT HAVE SPECIAL CHARACTORS IN USER NAME") 
            M.MyMainFunctions.Error_Logging_Function("Attempeted to inser special charctors")
            if Ve !=None:
                MyCred.User_Authentication()
    
                    