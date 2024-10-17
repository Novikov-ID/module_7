class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        symbol_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    for symbol in symbol_list:
                        if symbol in line:
                            line = line.replace(symbol, ' ')
                    line_strip = line.strip()
                    line_split = line_strip.split()
                    for line_s in line_split:
                        words.append(line_s)
                all_words[name] = words
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')


print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
