# problem 1 
text = 'ahmed mohammed atta '
sp = text.split(" ")
mySeparator =' '
x = mySeparator.join(sp[::-1])

print(x)

# problem 2 
def is_playing(name):
    if name[0] == 'r' or name[0] == 'R':

        return name + " plays banjo" 
    return name + " does not play banjo"

your_name= input("enter your name : ")
print(is_playing(your_name))