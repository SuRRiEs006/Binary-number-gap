#####LIMITS#####
'''
- MAX NUMBER IS 2**25 WHICH SHOULD BE MORE THAN BETTER

'''
#####IMPORTS#####
import copy


##### CODE ######

class BinaryNumber:
    def __init__(self,nVal):
        self.nVal = nVal
        self.countdownArray = []

    def reverseStr(self,stringIn):
        newReversedStr = ""
        for i in range(len(stringIn)-1,-1,-1):
            newReversedStr = newReversedStr + stringIn[i]
        return(newReversedStr)




    def generate_binary_numbers(self,decToBin):
        
        localN = copy.deepcopy(decToBin)

        if decToBin >= 1:
            
            currentBinaryNum = ""
            while localN != 0:
                if (localN % 2) == 1: 
                    currentBinaryNum = currentBinaryNum + "1"
                    localN = (localN-1)/2
                else:
                    currentBinaryNum = currentBinaryNum + "0"
                    localN = (localN)/2
            self.countdownArray.append(self.reverseStr(currentBinaryNum))
            decToBin = decToBin-1
            print(decToBin)
            self.generate_binary_numbers(decToBin)


    def main(self):
        decToBin = copy.deepcopy(self.nVal)
        self.generate_binary_numbers(decToBin)
        print("Output final array: "+str(self.countdownArray))



BinaryNumber(20).main()
