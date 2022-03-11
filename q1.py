#####LIMITS#####
'''
- MAX NUMBER IS 2**25 WHICH SHOULD BE MORE THAN BETTER

'''
#####IMPORTS#####
import copy

##### CODE ######

class BinaryNumber:
    def __init__(self,nVal):
        self.nVal = None
        self.highestPower = None
        self.countdownArray = []

    def biggestSquare(self,localDenNum):
        Nnum = copy.deepcopy(localDenNum)
        for x in range(0,25):
            if Nnum <= (2**x):
                highestPower = (x)
                break
        
        Nnum = Nnum-1
        BinaryNumber.generate_binary_numbers(self,Nnum)
        return(highestPower)


    def generate_binary_numbers(self,denNum):
        localDenNum = copy.deepcopy(denNum)
        if localDenNum > 0:
            highestPower = self.biggestSquare(localDenNum)
            binaryOutput = []
            
            workingNumber = copy.deepcopy(localDenNum)

            #print(str(2**highestPower) +" is the biggest square")
            for i in range((highestPower+0),-1,-1):
                if (2**i) <= workingNumber:
                    binaryOutput.insert(0,"1")
                    workingNumber = workingNumber - (2**i)
                else:
                    binaryOutput.insert(0,"0")
                
            if (localDenNum%2 == 1) & ("".join(binaryOutput) != "1"):
                self.countdownArray.append("".join(binaryOutput)[:-1] )
            else:
                if ("".join(binaryOutput[::-1]))[0] == "0":
                    self.countdownArray.append(("".join(binaryOutput[::-1]))[1:])
                else:
                    self.countdownArray.append("".join(binaryOutput[::-1]))
            #print(localDenNum)
            #print("".join(binaryOutput))
            return((' ,'.join(self.countdownArray))[::-1])



    def main(self):
        denNum = copy.deepcopy(self.nVal)
        print(self.generate_binary_numbers(20))



BinaryNumber(20).main()
