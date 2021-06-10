import string


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


# start by opening the file, read the file, turn file to all lower-case.

# Removing Punctuation- 1. Make a new string that stores the the punctuation marks. 
# 2. Make an empty string that will store words without punctuation.
# 3. Make a for in loop that will loop over each word of the text.
# 4. If statement checks if the word is present in punctuation string or not.
# 5. If it is not present, the word will be added to the new string.

# Split the string into a list so that each word can be counted and stop words can be removed.

# Removing Stop_words: 1. Create an empty array that will hold the appended text.
# 2. Make a for in loop that will loop over each word of list_of_words.
# 3. If statement checks if the word is present in the array STOP_WORDS or not.
# 4. If it is not present, the word will be appended to the new array words_to_count.

# Next steps: 1. Create new dictionary.
# 2. Loop over words in words_to_count and add them to a dictionary with an initial count of one. 
# Then, increase their value by one every time the word occurs.

# Sort the dictionary:  
# Loop over sorted, which takes the iterable object (dict) and will sort it based on 
# the order of the results when the key function is called. In this case, using the get method on the dict as the key's argument.
# Then, reverse=True will order the results in descending order.
# I also tried using the anonymous function lambda to sort the dictionary by its values (on line 61).


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        text = file.read().lower()
        # print(repr(text[0:-1]))
        new_text_string = ""
        for word in text:
            if word not in punctuation:
                new_text_string += word
        # print(new_text_string)
        list_of_words = new_text_string.split()
        # print(list_of_words)
        words_to_count = []
        for word in list_of_words:
            if word not in STOP_WORDS:
                words_to_count.append(word)
        dict = {}
        for word in words_to_count:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        print(sorted(dict.items(), key=lambda seq: seq[1], reverse=True))
        # for word in sorted(dict, key=dict.get, reverse=True):
        #     print(word, dict[word])


# Calling function, adding argument from function to the command line.
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
