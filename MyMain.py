

from multiprocessing import Value
from MainFunctions import MyMainFunctions


def main():

    A = 0
    inc = 0
    Pr = 0
    if (A==0):
        while True:

            if inc ==0:
                inc+=1
                A = MyMainFunctions.Opening_Function(0)
                if A == 0:
                    Pr = MyMainFunctions.request_Work(A)
                    if Pr!=0:
                        break
                else:
                    break
            
            else:
                Pr = MyMainFunctions.request_Work(0) 
                if (Pr==0):
                    continue
                else:
                    break
                

if __name__ == "__main__":
    main()