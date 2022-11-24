#-------------------------#
#Sieve of Eratosthenes    #
#By Willy Lennox          #
#Change maxNum as needed  #
#-------------------------#


import random
import datetime
import math

#Open file for output
out = open("primes.txt", "w")

def main():
    #Ask user for max number
    maxNum = int(input("Enter N: "))

    #Print boring watermark
    out.write("#" * 27 + "\n")
    out.write("|Sieve of Eratosthenes    |" + "\n")
    out.write("|Developed by Willy Lennox|" + "\n")
    out.write("#" * 27 + "\n\n\n\n")

    x = datetime.datetime.now()
    print(x.strftime("%c") + ": Inisialisation successful, preparing to sieve")
    #Run the sieve up to maxNum(N)
    nums = doErato(maxNum)

    #Print the final list
    printOut(nums)

    #Final touches
    x = datetime.datetime.now()
    print(x.strftime("%c") + ": Je Suis Finis")
    out.close()

def doErato(n):
    #Create a list from 2 to N
    nums = [i for i in range(2, n + 1)]
    
    #Repeat up to the square of n + 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if i in nums:
            j = i * i
            while j <= n:
                #Check if number has been deleted already
                if j in nums:
                    #Remove from list
                    nums.remove(j)
                #Get next multiple of i
                j += i
    return nums

def printOut(nums):
    for i in nums:
        out.write(str(i) + "\n")
    return


main()

#Old coloured watermark (haven't figured out how to print it to file)
"""
#Print watermark
    out.write(c[0] + "#" * 27 + colour.END + "\n")
    out.write(c[1] + colour.BOLD + "|Sieve of Eratosthenes    |" + colour.END + "\n")
    out.write(c[2] + "|Developed by Willy Lennox|" + colour.END + "\n")
    out.write(c[3] + "#" * 27 + colour.END + "\n")
"""

#This gets a bit annoying after a while
"""
                counter += 1
                if ((counter % 10000) == 0):
                    x = datetime.datetime.now()
                    print("Still sieving at " + x.strftime("%c"))
"""
