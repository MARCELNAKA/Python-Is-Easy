def genre(x):
    output = x
    return output

y = "indie"
z = genre(y)

print(z)
#indie

def year(y):
    output =(5 * y)
    return output

yearRelease = 2000
yearRelease = year(yearRelease)
print (yearRelease)
#10000
yearRelease2 =year(yearRelease)
print (yearRelease2)
#5000

def band(name):
    output = name
    return output
bandName = "the killers"

bandName = band(bandName)

print (bandName)
# the Killers

def addMul (x,y):
    output = x + 20
    output *= y + 10
    return output

calculo = addMul (3,4)
print (calculo)
#322
