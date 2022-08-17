sentence = input("Enter your sentence : ")
counterW = 0
counterS = 0
for i in range (len(sentence)) :
    if sentence[i] == '.' or sentence[i] == '?' :
        counterS += 1 
    if sentence[i] == ' ' :
        counterW += 1 
if sentence == '' :
    print("That paragraph is composed of " , counterS , " sentences and " , counterW , " words ")
else :
    print("That paragraph is composed of " , counterS , " sentences and " , counterW + 1 , " words ")