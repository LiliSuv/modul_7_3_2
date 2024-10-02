class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = [*file_names]

    def get_all_words(self):
        all_word = {}
        all_words = {}
        for file_name in self.file_names:
            with open (file_name, mode='r', encoding='utf-8') as file:
                a = file.read ()
                word = ''
                for wor in a:
                    word += wor.lower ()
                puncs = ',', '.', '=', '!', '?', ';', ':', ' - '
                for punc in puncs:
                    if punc in word:
                        word = word.replace (punc, ' ')
                        continue
                word = word.split ()
                all_word[file_name] = word
                all_words.update (all_word)
        return all_words

    def find(self, word):
        find = {}
        finds = {}
        for key, value in self.get_all_words ().items ():

            if word.lower () in value:
                find[key] = value.index (word.lower ()) + 1
                finds.update(find)
            else:
                find[key] = None
                finds.update (find)
        return finds

    def count(self, word):
        counts = {}
        for value, key in self.get_all_words ().items ():
            words = key.count (word.lower ())
            counts[value] = words
        return counts

finder2 = WordsFinder ('test_file.txt', 'test_file_1.txt')
print (finder2.get_all_words ())
print (finder2.find ('TEXT'))
print (finder2.count ('teXT'))
print (finder2.find ('поРа'))
print (finder2.count ('Очей'))
