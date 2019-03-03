'''
You're about to do an assignment called "Fizz Buzz", which is one of the classic programming challenges. 
It is a favorite for interviewers, and a shocking number of job-applicants can't get it right. 
But you won't be one of those people. Here are the rules for the assignment (as specified by Imran Gory):
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz". 
'''

for x in range (1,101):
    if x %3 ==0 and x %5 ==0:
        print ("FizzBuzz")
        continue    
    elif x %3 ==0:
        print ("Fizz")
        continue
    elif x %5 ==0:
        print ("Buzz")
        continue
    else:
        print (x)
