'''100 doors excercise'''
isopen=[]

def touchDoor(counter):
    if counter==101:
        return(isopen) 
    for i in range(0,101,counter):
        isopen[i]= not isopen[i]
    return touchDoor((counter+1))

for i in range(0,101):
    isopen.append(False)

eredmeny_list=touchDoor(1)

for i in range(0,101):
    if eredmeny_list[i]==True:
        print(str(i) + ". door is open! ")