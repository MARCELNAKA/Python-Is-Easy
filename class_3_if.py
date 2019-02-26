#homework

a = "5"
b = 6
c = 9

x = int(a)
y = int(b)
z = int(c)

result= False

def check(x,y,z):
    if x==y and x==z:
        result = True
    elif x==y and y==z:
        result = True
    else:
        result = False
        
print (result)
