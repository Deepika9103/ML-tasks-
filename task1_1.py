modern_family=['CLaiRe_DunPhY','PHiL_dUnpHY','GLoRIA_PriTCheTt','CaMErOn_TuCKEr','StELLa']

#Enumerate and Append functions
a=list(enumerate(modern_family))
indices=[]
character=[]

for index, item in a:
    indices.append(index)
    character.append(item)


print("The new lists are:\n")  
print(indices)
print(character)

#Lower and replace functions
for i in range(len(character)):
    character[i]=character[i].lower()
    character[i]=character[i].replace("_","-")

print(character)

#lamda and map functions
length=lambda x: len(x)
print(length(modern_family))

temp=list(map(length,character))
print(temp)

#zip and add functions
list1=list(zip(indices,temp))
for i in range(len(indices)):
    indices[i]=indices[i]+temp[i]
    
print(list1)
print(indices)

#sort function
indices.sort(reverse=True)
print(indices)

#adding the characters and indices
Phew_finally=dict(zip(indices,character))
print(Phew_finally)






