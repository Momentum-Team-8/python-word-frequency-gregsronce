from os import remove, replace


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

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

# Make the words_to_count a smaller range to experiment and work with.

# Use the count method to count the number of words in the list with specified value?


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as the_hill_we_climb:
        text = the_hill_we_climb.read().lower()
        # print(repr(text[0:-1]))  
        punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
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
        # print(words_to_count)
        smaller_chunk = words_to_count[0:14]
        print(smaller_chunk)
        # for word in smaller_chunk:
        #     print(word, smaller_chunk.count(word))


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
