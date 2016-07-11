def word_count(filepath):
    filename = open(filepath)
    word_count = {}
    list_of_words = []
    
    #we are going to turn text file into a string of words
    for line in filename:
        line.rstrip()
        list_of_words = list_of_words + line.split(" ")
    
    for word in list_of_words:
        word_count[word] = word_count.get(word, 0) + 1
        return word_count.items()

print word_count("test.txt")

