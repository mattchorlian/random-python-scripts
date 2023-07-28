
from nltk.corpus import words
import enchant

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
accepted = ['c', 'i', 'y', 't', 'd', 'a', 'r']
forbidden = [letter for letter in alphabet if letter not in accepted]

def check_word(word):
    for letter in forbidden:
        if letter in word or letter.upper() in word:
            return False
    return True

def spellingbee(accepted):
    d = enchant.Dict("en_US")
    result = []
    word_dict = words.words()
    trimmed_dict = [word for word in word_dict if accepted[0] in word]
    for word in trimmed_dict:
        if check_word(word):
            result.append(word)
    #filter(check_word, trimmed_dict)
    for i in range(4, 12):
        list_i = []
        list_i = [word for word in result if len(word) == i and word[0].upper() != word[0] and d.check(word)]
        print('\n')
        print(list_i)
    
spellingbee(accepted)
