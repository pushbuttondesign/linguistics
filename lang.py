"""
Collection of functions for linguistic analysis

TODO:
- add senterment analysis
- add lexical chain identification
"""

import pandas
import os

#word list locations on unix systems
NAMES = "/usr/share/dict/propernames"
DICT = "/usr/share/dict/words"

def cvmap(word):
    """
    FUNCTION DESCRIPTION
    Computs the consonant-vowel map of a word

    INPUTS
    word, string, an english word

    OUTPUTS
    map, string, a cv map where c indicates consonant and v a vowel
    """
    vowels = ('A','E','I','O','U','a','e','i','o','u')
    consonants = (  'B','C','D','F','G','H','J','K','L','M', \
                    'N','P','Q','R','S','T','V','W','X','Y','Z', \
                    'b','c','d','f','g','h','j','k','l','m', \
                    'n','p','q','r','s','t','v','w','x','y','z')
    map = ''
    for letter in word:
        if letter in vowels:
            map = map + 'v'
        elif letter in consonants:
            map = map + 'c'
    return map

def wordfreq(word_list):
    """
    FUNCTION DESCRIPTION
    Computes the number of times each word appears in a text

    INPUTS
    word_list, iterable, list of words

    OUTPUTS
    freq, dictionary, word, string, and frequency, int, pairs
    """
    freq = {}
    for word in word_list:
        if word in freq.keys():
            freq[word] = freq.get(word) + 1 #increment frequency value
        else:
            freq[word] = 1
    return freq

def cvfreq(cvword):
    """
    FUNCTION DESCRIPTION
    Compares a consonant-vowel map of a word to those of the Webster Dictionary

    INPUTS
    cvword, string, a consonant-vowel map of a word

    OUTPUTS
    webster_freq.get(cvword), int, frequency of that map in the dictionary
    """
    #load dictionary
    with open(DICT, 'r') as file:
        webster_cv = []
        #compute cv map of each word
        for word in file:
            webster_cv.append(cvmap(word))
        #get frequency of each word
        webster_freq = wordfreq(webster_cv)
    #search webster cvs for word
    if cvword in webster_freq.keys():
        return webster_freq.get(cvword) #return freq
    else:
        return 0

def trigramfreq(word):
    """
    FUNCTION DESCRIPTION
    Searches for common two and three consecutive letter combinations in a word
    e.g. 'ing', 'the', 'er', 'st'

    INPUTS
    word, string, an english word

    OUTPUTS
    freq, int, number of common combinations found in word
    """
    trigrams = "./trigrams_freq"
    """
    #code used to create file
    alpherbet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    #compute every two and three letter combination of alpherbet
    trigram = set()
    for first_letter in alpherbet:
        for second_letter in alpherbet:
            for third_letter in alpherbet:
                trigram.add(first_letter+second_letter+third_letter)
    #also add diagrams
    for first_letter in alpherbet:
        for second_letter in alpherbet:
            trigram.add(first_letter+second_letter)
    #convert to dictionary with 0 values
    trigrams = dict.fromkeys(trigram, 0)
    #search webster dictionary for each combination and compute frequency of occuranceß
    with open(DICT, 'r') as readfile:
        with open("trigrams_freq", 'w') as writefile:
            len = 0
            for word in readfile:
                len += 1
            readfile.seek(0)
            count = 0
            for word in readfile:
                count += 1
                print("{} of {}".format(count, len))
                for gram in trigrams.keys():
                    if gram in word:
                        trigrams[gram] = trigrams.get(gram) + 1
            #save freq of each trigram in the dictionary as file for later use
            for key, value in trigrams.items():
                if value > 2:
                    writefile.write('{},{}\n'.format(key, value))
    """
    #load existing file to dictionary
    with open(trigrams, 'r') as file:
        trigrams = {}
        for line in file:
            kvpair = line.split(',')
            trigrams[kvpair[0]] = int(kvpair[1])
    #serch word for each combination
    freq = 0
    for key, value in trigrams.items():
        #ignore values with less than 1000 occurances
        if value >= 1000:
            if key in word:
                freq += 1
    return freq

def filestats(word_list, delimiter):
    """
    FUNCTION DESCRIPTION
    Prints stats of a word list file

    INPUTS
    word_list, pointer, file with words in
    delimiter, string, delimiter used on lines in file

    OUTPUTS
    return 0 if scucessfully prints output on screen
    """
    file.seek(0)
    row_num = 0
    word_num = 0
    char_num = 0
    for line in file:
        char_per_line = 0
        for letter in line:
            char_per_line += 1
        char_num = char_num + char_per_line
        row_num += 1
        word_num = word_num + len(line.split(delimiter))
    stats = os.stat(file)
    print( \
    """
    {}
    \'{}\' delimiter
    {} characters
    {} words
    {} rows
    {} kilobytes
    """.format(word_list, delimiter, char_num, word_num, row_num, stats.st_size * 1000))
    return 0
