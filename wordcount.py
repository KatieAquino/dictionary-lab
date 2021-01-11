def count_word_dict(file_name):
    """Count each word in file"""

    text_file = open(file_name)

    word_count = {}


    for line in text_file:

        line = line.rstrip()

        words = line.split(" ")

        for word in words:

            word_count[word] = word_count.get(word, 0) + 1
    
    for key, value in word_count.items():
        print("key = {}, value = {}".format(key, value))
    

count_word_dict("test.txt")
count_word_dict("twain.txt")