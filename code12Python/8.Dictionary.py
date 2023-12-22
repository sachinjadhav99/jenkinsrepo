myDict={
    "Fast":"In a Quik Manner",
    "name":"Sachin",
    "Marks":[1,23,4] ,
    "Sourname":"Jadhav"     
}

# print(myDict['Fast'])
# print(myDict['name'])
# print(myDict['Marks'])

#Methods
print(list(myDict.keys()))  #Prints the keys of the dictionary
print(myDict.values())     #Prints the Values of the dictionary
print(myDict.items())      #Prints the (key, values) for all contents of the dictionary   
print(myDict)
updateDict={
    "Lovish": "Friend",
    "Shubham":"Friend"
}
myDict.update(updateDict)
print(myDict)