def word_count(filename):

    file = open(filename)

    word_list = []

    for line in file:

        line = line.rstrip()

        words = line.split(" ")

        word_list.extend(words)

    words_in_file = {}

    for word in word_list:
        words_in_file[word] = words_in_file.get(word, 0) + 1

    for word, number in words_in_file.items():
        print("{} {}".format(word, number))

    file.close()


# word_count("test.txt")

word_count("twain.txt")
