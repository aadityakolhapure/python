
string = "I am a programer. I am am a student. I am am am good."
word = "am"
# splitting the string at space
words = string.split()
# initializing count variable to 0
count = 0
for w in words:
    # checking the match of the word
    if w == word :
        # increment count on match
        count += 1
# printing the count        
print("The count of given word is")
print(count)