from os import remove, replace


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# start by opening the file, read the file


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as the_hill_we_climb:
        text = the_hill_we_climb.read().lower()
        # print(repr(text[0:-1]))  
        text = text.split()
        new_text = text[0:12]
        print(new_text)
        for word in new_text:
            print(word, new_text.count(word))
        
        # trying to figure out removing stop-words
        bad = STOP_WORDS[0]
        for bad in STOP_WORDS:
            # print(bad)
            if bad in new_text:
                new_text.remove(bad)
            print(new_text)


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
