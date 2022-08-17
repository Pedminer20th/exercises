string = input("Enter a string : ")
new = int(input("Which character you want to change(write the index of the character) : ")) - 1
replace = input("Enter a new character : ")
a = string[ : new]
b = string[new + 1 : ]
print(a + replace + b)
