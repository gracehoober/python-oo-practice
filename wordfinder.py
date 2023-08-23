from random import randint

class WordFinder:
    """Word Finder: finds random words from a dictionary."""


    def __init__(self, filepath):
        """Create a word finder instance by reading a provided file of words."""

        self.words_list = self.construct_wordslist_and_count(filepath)

        print(f"{len(self.words_list)} words read")

    # @classmethod
    def construct_wordslist_and_count(self, filepath): # TODO: Change method name to be concise
        """Reads a file of words returns a list of words and count of words"""
        # words_list = set()

        file = open(filepath, "r")
        words_list = [line.strip() for line in file]

        # with open(filepath, "r") as file:
        #     for line in file:
        #         # words_list.add("".join(line.split("\n")))
        #         words_list.append("".join(line.split("\n"))) # Note: strip() is another option that avoids having to join, specifically removes whitespace

        return words_list


    def random(self):
        """Returns a random word from the words list"""
        # removed = self.words_list.pop()
        # self.words_list.add(removed)

        # Note: choice() allows to select random item from a sequence
        randomIndex = randint(0, len(self.words_list) - 1)
        return self.words_list[randomIndex]


        # return removed

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

        # TODO: List comprehension here to be more pythonic
        new_words_list = []

        for word in self.words_list:
            if not (not word or word[0] == "#"):
                new_words_list.append(word)


        self.words_list = new_words_list

        #TODO: REPR for both classes