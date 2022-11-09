# what will be printed when the code below is executed
text = "alphabet"
i = 0
while i <= 5 :
    if text[i] == "h":
        print("pla")
        break
    print(text[i], end="")
    i += 1
# the answer is alppla

# what will be printed when the code below is executed?
text = "alphabet"
i = 0
while i <= 5 :
    if text[i] == "h":
        print("pla", end=",")
        i += 1
        continue
    print(text[i], end="")
    i += 1
# the answer is alppla,ab