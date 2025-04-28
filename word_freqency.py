#
# Matthew Anderson 4/27/2025
#

import os

filename = input("Enter filename: ")

if os.path.isfile(filename):
    
    # open the file and read all contents into a list of words
    word_file = open(filename, "r")

    file_contents = word_file.read().strip()

    all_words = file_contents.split()


    # calculate frequency of each word
    word_frequency = {}

    for word in all_words:
        if word in word_frequency:
            word_frequency[word] += 1
        else: # if the word does not exist, initialize as 1
            word_frequency[word] = 1

    word_file.close()
    
    # prompt user for output file name, if left blank, frequencyOutput.txt will be used
    output_filename = input("Enter output filename (frequencyOutput.txt): ")
    if len(output_filename.strip()) == 0:
        output_filename = "frequencyOutput.txt"
    
    output_file = open(output_filename, "w")

    # string to be used as buffer
    output_contents = ""

    # get all unique words in sorted form through the frequency dict keys
    words = list(word_frequency.keys())
    words.sort()

    # add each word and its freqency, separated by a comma, to the output buffer
    for word in words:
        word_freq = word_frequency[word]
        output_contents += f"{word}, {word_freq}\n"
    
    output_file.write(output_contents) # finally write to the file

    output_file.close()

else:
    print("That file does not exist!") # error if the file cannot be found