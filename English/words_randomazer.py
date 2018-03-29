import random
import datetime

WORD_TO_LEARN = 5


# Read default file
default_file = open("english_words_to_learn.txt", "r")
words_list = default_file.readlines()
default_file.close()

# Re-write file without selected words
with open("english_words_to_learn.txt", "w") as default_file:
    rand_lines = [random.choice(words_list) for i in range(WORD_TO_LEARN)]
    for line in words_list:
        if line not in rand_lines:
            default_file.write(line)
    for line in rand_lines:
        print(line.split()[1].upper())

# Write learned words to another file
with open("learned_words.txt", "a") as learned_files:
    learned_files.write(str(datetime.datetime.now()) + "\n")
    learned_files.write("*" * 20 + "\n")
    for line in rand_lines:
        learned_files.write(str(line.split()[1]) + "\n")

    learned_files.write("*" * 20 + "\n")
    learned_files.write("\n")
