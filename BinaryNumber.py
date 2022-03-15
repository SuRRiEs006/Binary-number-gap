#####LIMITS#####
'''
- HIGHEST N IS 1000 DUE TO MAX RECURSION
'''
######IMPORTS####
from cgitb import reset
import copy
import sys
# SETTING MAX RECURSION DEPTH TO ALLOW MAX N OF 1000
sys.setrecursionlimit(1018)
##### CODE ######

class BinaryNumber:
    def __init__(self,nVal):
        self.nVal = nVal
        self.nValBin = None
        self.countdownArray = [None]*5
        self.gapValue = 1

    def generate_binary_numbers(self,decToBin):
        
        localN = copy.deepcopy(decToBin)

        if decToBin >= 1:
            currentBinaryNum = ""
            while localN != 0:
                if (localN % 2) == 1: 
                    currentBinaryNum = "1"+currentBinaryNum
                    localN = (localN-1)/2
                else:
                    currentBinaryNum ="0"+ currentBinaryNum
                    localN = (localN)/2
            if decToBin+5 > (self.nVal):
                #print(self.nVal-decToBin)
                self.countdownArray[(self.nVal-decToBin)] = currentBinaryNum
            else:
                self.countdownArray.append(currentBinaryNum)
            if decToBin == self.nVal:
                self.nValBin = (currentBinaryNum)
            decToBin = decToBin-1
            self.generate_binary_numbers(decToBin)

    def output_binary_numbers_reverse(self):
        outputString = ""
        for i in range(0,len(self.countdownArray)):
            if self.countdownArray[i] == None:
                break
            outputString = f"{outputString} {str(self.countdownArray[i])},"
        outputString = f"{outputString[:-1]}. "
        return(outputString)



    def binaryGap(self,index,streak):
        
        if (index <= len(self.nValBin)-1):
            if (self.nValBin.count("1") > 1) & (self.nValBin.find("0") != -1):
                if self.nValBin[index] == "0":
                    streak = streak+1
                elif self.nValBin[index] == "1":

                    if streak >= self.gapValue:

                        self.gapValue = streak+1
                    streak = 0
                index = index + 1
                self.binaryGap(index,streak)
            else:
                if (self.nValBin.count("1") <= 1):
                    self.gapValue = 0
                else:
                    self.binaryGap = 1



    def main(self):
        decToBin = copy.deepcopy(self.nVal)
        self.generate_binary_numbers(decToBin)
        print(f"Binary numbers between 1 and {self.nVal} are: {self.output_binary_numbers_reverse()} \n")
        self.binaryGap(0,1)
        print(f"The binary gap of {self.nVal} is {self.gapValue}.")



if __name__ == "__main__":
    reRun = True
    validN = False
    while reRun == True:
        while validN == False:
            try:
                ClassNVal = int(input("Please input a whole number: "))
                validN = True
            except:
                print("ERROR: PLEASE ENSURE THE INPUT IS AN INTEGER AND  ")

        BinaryNumber(ClassNVal).main()
        validN = False

        validInput = False
        while validInput == False:
            reRunQ = input('''\n\n\n------------------------------------------------- \nDo you want to input another number? (y/n) :''').lower()
            if (reRunQ == "y") or (reRunQ == "n"):
                validInput = True
                if reRunQ == "n":
                    print("You are now exiting the program...\nThank you for trying it out!")
                    reRun = False
            else:
                print("Your input wasn't recognized, please ensure there are no spaces in your input!")
