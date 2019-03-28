#Details:
#
#Return to your first homework assignments, when you described your favorite song.
#Refactor that code so all the variables are held as dictionary keys and value.
#Then refactor your print statements so that it's a single loop that passes through each item
#in the dictionary and prints out it's key and then it's value.

music = {"band":"The Killers", "genre": "Indie Rock", "disc":5 }
for x in music:
    print ("key:", end = "")
    print (x)
    print ("value:", end = "")
    print (music[x])

#Extra Credit:
#
#Create a function that allows someone to guess the value of any key in the dictionary,
#and find out if they were right or wrong. This function should accept two parameters:
#    Key and Value. If the key exists in the dictionary and that value is the correct value,
#    then the function should return true. In all other cases, it should return false.

dict = {"grey":2, "red":10, "yellow":7, "blue":9}

x = input("select a  color:")

if x in dict:
    y = input("select an number:")
    z = dict[x]
    if y == z:
        print(True)
    else:
        print(False)

else:
    print(False)
    
