# Mid-term is OPEN BOOK

print(type(2+3))
print(type(6/2))
print(type(5 or 6))
print(type(2^2))
print(type(print))

print(2+3)
print(2!=3)
print(6/2)
print(5 or 6)
print([1,2,3].append("john"))
print("bubu"*2)

punctuation = ", . ? !"

def find_words(filename):
    """
    prints the 3 letter words starting with b
    :param filename: the name of the file
    :return: Nothing
    """
    with open(filename, 'r') as f:
        for line in f:
            #sanitize line
            for p in punctuation:
                line = line.replace(p, " ")
            # need to break down the line into words
            words = line.split() # by default splits by space
            #check each word
            for word in words:
                if len(word) == 3 and word.upper()[0] == "B" :
                    print(word)

find_words("input.txt")