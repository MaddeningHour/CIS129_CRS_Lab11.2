#Christopher Robles Serrano
#Module 11 Lab 2
#12/11/2024
#This program reads the file from the previous lab. It returns the count, total, and average.

#Reading from grades.txt
with open('grades.txt', 'r') as grades:
    #Creating our variables
    myCount = 0
    myTotal = 0 

    print(f'\nGrades:\n')

    #For loop to read line by line in grades.txt
    for grade in grades:
        try:
            print(f'{grade}')
            #Stripping and convert the data to a float.
            studentGrade = float(grade.strip())       

            #Adding to total and incrementing myCount   
            myTotal += studentGrade
            myCount += 1
        except:
            #Error handling in case the row of data cannot be convert to a float.
            print(f"Error!'{grade.strip()}' cannot be converted into a float.")

    #Error handling to check that our grades.txt file actually has data. 
    if myCount > 0:
        #Printing count, sum, and average.
        print(f"grades.txt has a count of {myCount} grade(s) for a total of {myTotal}. The average grade of 'grades.txt' is: {(myTotal / myCount):.2f}")
    else:
        print('The text document being opened is empty.')
