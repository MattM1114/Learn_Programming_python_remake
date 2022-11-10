# how many elements will be in your_set after the 
# following code executes?

your_set = set()
for i in range(10):
    if i % 2 == 0:
        your_set.add("even")
    else:
        your_set.add("odd")
# the answer is 2
# to remove something form a list
your_set.remove("odd")