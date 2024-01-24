# File  Manipulation program

file = open("file.txt", "r") 
dictionary = dict() 
  
for lines in file: 
    lines = lines.strip() 
    lines = lines.lower()  
    names = lines.split(" ")

    for name in names: 
        if name in dictionary: 
            dictionary[name] = dictionary[name] + 1
        else: 
            dictionary[name] = 1
for key in list(dictionary.keys()): 
    print(key, ":", dictionary[key])