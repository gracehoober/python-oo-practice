class WordFinder:
    """Word Finder: finds random words from a dictionary."""


    def __init__(self, filepath):
        """Create a word finder instance by reading a provided file of words."""

        (self.words_list, count) = self.construct_wordslist_and_count(filepath)

        print(f"{count} words read")

    # @classmethod
    def construct_wordslist_and_count(self, filepath):
        words_list = set()

        with open(filepath, "r") as file:
            num_words = 0
            for line in file:
                words_list.add("".join(line.split("\n")))
                num_words += 1

        return (words_list, num_words)


