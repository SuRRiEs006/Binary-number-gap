#####LIMITS#####
"""
- HIGHEST N IS 1000 DUE TO MAX RECURSION
"""
######IMPORTS####
from cgitb import reset
import copy
import sys

##### CODE ######

# SETTING MAX RECURSION DEPTH TO ALLOW MAX N OF 1000
sys.setrecursionlimit(1018)


class BinaryNumber:
    def __init__(self, nVal):
        # nVal is the n value provided by the user
        self.nVal = nVal
        # nValBin is the n value in binary form
        self.nValBin = None
        # countdownArray is an array of all binary numbers being counted down to one. Default is 10 indexes
        self.countdownArray = [None] * 10
        # countdownArray is the count of binary gap, its updated with higher values if found
        self.gapValue = 1
        # default fill value of countdownArray
        self.memoryAllocated = 10

    # a recursive function that calculates each number from N to 1 to binary
    def generate_binary_numbers(self, decToBin):

        # local deep copy of decToBin to work with in current funtion
        localN = copy.deepcopy(decToBin)

        # If statement gives a place to provide an end point for recursion
        # in this situation if calculating the binary to 1 then stop after.
        if decToBin >= 1:

            # initialize string to add current binary digits to
            currentBinaryNum = ""

            # while loop ensures that the number keeps geing through the
            # halfing cycle till localN is 0 where it can no longer half
            while localN != 0:

                # if odd number then add 1 to currentBinaryNum and add one to number and half
                if (localN % 2) == 1:
                    currentBinaryNum = "1" + currentBinaryNum
                    localN = (localN - 1) / 2

                # else must be even; then add 0 to currentBinaryNum and half number
                else:
                    currentBinaryNum = "0" + currentBinaryNum
                    localN = (localN) / 2

            # up to first 10 time the generate_binary_numbers method run
            # it must repalce default values of None on self.countdownArray
            if decToBin + self.memoryAllocated > (self.nVal):
                # print(self.nVal-decToBin)
                self.countdownArray[(self.nVal - decToBin)] = currentBinaryNum

            # else all default values filled then must start appending
            else:
                self.countdownArray.append(currentBinaryNum)

            # checks to see if n value entered by user is the binary output
            # as its more efficient to save it now than to calculate it again later
            # saves the value to self.nValBin for future use
            if decToBin == self.nVal:
                self.nValBin = currentBinaryNum

            # decreases decToBin by one to pass as a parameter for next call of funtion
            decToBin -= 1
            self.generate_binary_numbers(decToBin)

    # convers the array (self.countdownArray) into an string that can be outputted
    def output_binary_numbers_reverse(self):
        outputString = ""
        for i in range(0, len(self.countdownArray)):
            if self.countdownArray[i] == None:
                break
            outputString = f"{outputString} {str(self.countdownArray[i])},"
        # removes last extra "," and replaces with "."
        outputString = f"{outputString[:-1]}. "
        return outputString

    # calculates binary gap recursivly
    # index is the currect digit check of binary string
    # streak is the count of cap that increments if applicable
    def binaryGap(self, index, streak):

        # checks all indexes not covered already
        if index <= len(self.nValBin) - 1:
            # checks more than 1 one and a zero is present.

            if (self.nValBin.count("1") > 1) & (self.nValBin.find("0") != -1):

                # if index value 0 then increment streak by by 1
                if self.nValBin[index] == "0":
                    streak = streak + 1

                # else see if one then see if a new largest gap. If largest then overwrite previous, reset streaks to 0
                elif self.nValBin[index] == "1":
                    if streak >= self.gapValue:
                        self.gapValue = streak + 1
                    streak = 0

                index += 1  # increment index by one for next look
                self.binaryGap(index, streak)
            # if the if statement not met then the answer is clearly either 0 or 1 respectivly.
            else:
                if self.nValBin.count("1") <= 1:
                    self.gapValue = 0
                else:
                    self.binaryGap = 1

    # main method just co-ordinates inputs and outputs and calls other methods to get the output results to user
    def main(self):
        decToBin = copy.deepcopy(self.nVal)

        self.generate_binary_numbers(decToBin)
        print(
            f"Binary numbers between 1 and {self.nVal} are: {self.output_binary_numbers_reverse()} \n"
        )

        self.binaryGap(0, 1)
        print(f"The binary gap of {self.nVal} is {self.gapValue}.")


if __name__ == "__main__":
    # re-run variable to check if should run script again, validN checks input validity
    reRun = True
    validN = False

    # keeps looping till valid N is provided by the user
    while reRun == True:
        while validN == False:
            try:
                ClassNVal = int(input("Please input a whole number: "))
                if (ClassNVal == 0) or ((ClassNVal > 1000)):
                    raise ("INPUT IS NOT BE 0")
                validN = True
            except:
                print(
                    "ERROR PLEASE ENSURE:\n\n     - THE INPUT IS AN INTEGER \n     - MAX N INPUT IS 1000 \n     - INPUT IS NOT BE 0 \n_________________________________________________ "
                )

        # runs main function with N input being provided to initialization method, then resets validN for menu
        BinaryNumber(ClassNVal).main()
        validN = False

        # valid input ensures that the while loop runs till a valid input to menu is provided.
        validInput = False
        while validInput == False:
            reRunQ = input(
                """\n_________________________________________________ \nDo you want to input another number? (y/n) :"""
            ).lower()

            if (reRunQ == "y") or (reRunQ == "n"):
                validInput = True
                if reRunQ == "n":
                    print(
                        "You are now exiting the program...\nThank you for trying it out!\n_________________________________________________"
                    )
                    reRun = False
            else:
                print(
                    "Your input wasn't recognized, please ensure there are no spaces in your input! "
                )
