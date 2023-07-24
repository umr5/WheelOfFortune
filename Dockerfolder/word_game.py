import random

class WordGame:

    def __init__(self):
        self.active = True
        self.phrase = []
        self.letter_guess = []
        self.guessed_phrase = []
        file = open('phrases.txt', 'r')
        self.data = file.readlines()

    def guess_word(self, letter):
         for i in range(len(self.phrase)):
             if self.phrase[i] == letter:
                self.guessed_phrase[i] = letter
         return self.guessed_phrase



    def get_phrase(self):
        index = random.randint(0,205)
        self.phrase = self.data[index].lower().replace('\n', '')
        for i in self.phrase:
            self.guessed_phrase.append(i)
        for x in range(len(self.guessed_phrase)):
            if self.guessed_phrase[x] != ' ':
                self.guessed_phrase[x] = '_'
        return self.guessed_phrase

    def return_phrase(self):
        if self.guessed_phrase.__contains__('_'):
            return self.guessed_phrase
        else:
            return 'You Win!'

    def delete_phrase(self):
        self.phrase = []
        self.guessed_phrase = []
