from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.
        >>> wf = WordFinder("words.txt")

        >>> wf.random() in ["# Veggies", "kale", "parsnips", " ", "# Fruits", "apple", "mango"]

    """

    def __init__(self, filepath):
        """Create a word finder instance by reading a provided file of words."""

        self.words_list = self.construct_wordslist(filepath)

        print(f"{len(self.words_list)} words read")

    def __repr__(self):
        return f"number of items in words_list= {len(self.words_list)}"

    def construct_wordslist(self, filepath):
        """Reads a file of words returns a list of words"""


        file = open(filepath, "r")
        words_list = [line.strip() for line in file]

        return words_list


    def random(self):
        """Returns a random word from the words list"""

        return choice(self.words_list)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary, but excludes comments (#) and blank lines."""

    def __init__(self, filepath):
        """Create a special word finder instance by reading a provided file of words."""
        super().__init__(filepath)
        self.remove_invalid_words()

    def remove_invalid_words(self):
        """
        Process the words list further to remove blank spaces and comments starting with '#'.
        Called when instance of class is created.
        """

        self.words_list = [word for word in self.words_list if not (not word or word[0] == "#")]

        # for word in self.words_list:
        #     if not (not word or word[0] == "#"):
        #         new_words_list.append(word)


        # self.words_list = new_words_list

        #TODO: REPR for both classes