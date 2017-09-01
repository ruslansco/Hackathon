#!/usr/bin/env python3
# Ruslan Shakirov CSC223 
# LabA4 Problem 2: Indian Pearl

def pearl():
    """This function opens file - 'indian_test.in', gets items from the file and stores each item into a list.
        Finally it calculates total amount of pearl found by both parties."""
    List1=[]     # Creates empty list.
    with open('indian_test.in') as file: # Opens file 'indian_test,.in' in reading mode.
        for line in file:       # For each line of the input file.
            inputLine = [int(i) for i in line.split()]  # inputLine converts and splits each line from string to int'.
            firstIndex=inputLine[0]      # firstIndex gets index zero from inputFile.
            indexAll=inputLine[1:]     # indexAll gets all items starting from index one till end.
            print("List: ", inputLine)
            try:
                for fraction in indexAll: # For each index in indeAll
                    fraction=1/fraction # Fraction makes a fraction from each number in indexAll.
                    List1.insert(0, fraction) # Inserts fraction  in to List1.
            except ZeroDivisionError: # So it can perform calculations with zeros.
                pass
            sumOfList=sum(List1)  # Adds all integers in List1. 
            del List1[:]    # Empties the list
            pComp= (100*sumOfList) # Creates percentage from fraction number found by companies.
            pComp = round(pComp, 1)
             
            pPrinc =100-pComp # Calculates percentage from fraction number found by Princess.
            pPrinc = round(pPrinc, 1)
            
            pearlComp=firstIndex*pComp/pPrinc # Calculates amount of pearls found by companies.
            pearlComp=round(pearlComp)
            
            pearlTotal = firstIndex+pearlComp # Calculates total amount of pearls found by both parties.
            pearlTotal = round(pearlTotal)
            
            print("Princess found",pPrinc,"% =",firstIndex,"pearls")
            print("Companies found",pComp,"% =",pearlComp,"pearls")
            print("Total number of pearls found is:",pearlTotal,"pearls \n")
    file.close()
    return None
pearl()

