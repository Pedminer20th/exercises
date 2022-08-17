sentence = input("Write a sentence : ")
counter = 0
for i in range (len(sentence)) :
    if sentence[i] == 'i' or sentence[i] == 'j' or sentence[i] == '.' :
        counter += 1 
print("The sentence contain" , counter , "points") 