import itertools
import enchant

# Helper function for turning list of strings into a string
# Args: word is a list containing letters
# Returns: a string of letters in the list, in order

def wordify(word):
    res = ""
    for w in word:
        res = res + w
    return res


# This function does a series of things:
# 1. Creates a list containing all > 3 letter combinations of the original letters
# 2 Using each combination in the above list, create cartesian products of lengths 3 - 8 to check as words
# 3. Return filtered list of checked words
# Args: letters is a 7 letter long list, and special is the letter that must be included (letters[0])

def spellingbee(letters):
    d = enchant.Dict("en_US")
    special = letters[0]

    four_letter_words = []
    five_letter_words = []
    six_letter_words = []
    seven_letter_words = []
    eight_letter_words = []

    combs3 = list(itertools.combinations(letters, 3))
    combs4 = list(itertools.combinations(letters, 4))
    combs5 = list(itertools.combinations(letters, 5))
    combs6 = list(itertools.combinations(letters, 6))

    filtered_combs3 = [[word[0], word[1], word[2]] for word in combs3 if special in word]
    filtered_combs4 = [[word[0], word[1], word[2], word[3]] for word in combs4 if special in word]
    filtered_combs5 = [[word[0], word[1], word[2], word[3], word[4]] for word in combs5 if special in word]
    filtered_combs6 = [[word[0], word[1], word[2], word[3], word[4], word[5]] for word in combs6 if special in word]

    final_list = list(itertools.chain(filtered_combs3, filtered_combs4, filtered_combs5, filtered_combs6))
    final_list.append(letters)
    for combination in final_list:
        print("SEARCHING FOR WORDS WITH COMBINATION: ")
        print(combination)

        if len(combination) <= 4:
            fours = itertools.product(combination, repeat=4)
            filtered_fours = [wordify(word) for word in fours if special in word and d.check(wordify(word))]
            four_letter_words.append(filtered_fours)

        if len(combination) <= 5:
            fives = itertools.product(combination, repeat=5)
            filtered_fives = [wordify(word) for word in fives if special in word and d.check(wordify(word))]
            five_letter_words.append(filtered_fives)

        if len(combination) <= 6:
            sixes = itertools.product(combination, repeat=6)
            filtered_sixes = [wordify(word) for word in sixes if special in word and d.check(wordify(word))]
            six_letter_words.append(filtered_sixes)

        sevens = itertools.product(combination, repeat=7)
        filtered_sevens = [wordify(word) for word in sevens if special in word and d.check(wordify(word))]
        seven_letter_words.append(filtered_sevens)

        eights = itertools.product(combination, repeat=8)
        filtered_eights = [wordify(word) for word in eights if special in word and d.check(wordify(word))]
        eight_letter_words.append(filtered_eights)


    four_letter_words_final = [*set([element for sublist in four_letter_words for element in sublist])]
    five_letter_words_final = [*set([element for sublist in five_letter_words for element in sublist])]
    six_letter_words_final = [*set([element for sublist in six_letter_words for element in sublist])]
    seven_letter_words_final = [*set([element for sublist in seven_letter_words for element in sublist])]
    eight_letter_words_final = [*set([element for sublist in eight_letter_words for element in sublist])]

    print("FOURS")
    print(four_letter_words_final)
    print("FIVES")
    print(five_letter_words_final)
    print("SIXES")
    print(six_letter_words_final)
    print("SEVENS")
    print(seven_letter_words_final)
    print("EIGHTS")
    print(eight_letter_words_final)



spellingbee(['a', 'f', 't', 'e', 'i', 'c', 'b'])