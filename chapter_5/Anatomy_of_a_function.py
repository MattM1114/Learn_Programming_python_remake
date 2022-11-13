# this is what a functions looks like
def get_user_data():
    return input().split()

def count_vowels(data):
    count = 0
    for c in data:
        if c in {"a", "e", "i", "o", "u"}:
            count += 1
        return count

#this is how this function works
user_data = get_user_data()
for s in user_data:
    print(s + " " + str(count_vowels(s)))