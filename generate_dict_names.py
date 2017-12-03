from nltk.corpus import words


class GenerateDictNames(object):
    def __init__(self, min_len=4, max_len=10):
        self.min_len = min_len
        self.max_len = max_len

    def generate(self):
        word_list = words.words()
        names = []

        for word in word_list:
            word = word.lower()
            if len(word) >= self.min_len and len(word) <= self.max_len:
                names.append(word)

        return names


if __name__ == '__main__':
    names = GenerateDictNames().generate()
    for name in names:
        print(name)
    print(len(names))
