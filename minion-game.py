import unittest
import sys

VOWELS = set(['A', 'E', 'I', 'O', 'U'])

def is_vowel(char):
    return char in VOWELS

def calculate_score(word, vowel_start=True):
    score = 0
    seen_words = set([])
    for i, char in enumerate(word):
        good_to_start_here = (
            vowel_start and is_vowel(char) 
            or (not vowel_start and not is_vowel(char)))
        if(good_to_start_here):
            words_starting_at_char = gen_words_starting_at_char(word, i)
            for subword in words_starting_at_char:
                if subword in seen_words:
                    continue
                else:
                    seen_words.add(subword)
                    score += calc_score_from_subword(word, subword)
    return score

def gen_words_starting_at_char(word, i):
    for j in range(i+1, len(word) + 1):
        yield word[i:j]

def calc_score_from_subword(word, subword):
    score = 0
    subword_len = len(subword)
    for i, char in enumerate(word):
        score += int(word[i:(i + len(subword))] == subword)
    return score

def read_word():
    return sys.stdin.read().strip()


class TestMinionGame(unittest.TestCase):
    
    def test_gen_words(self):
        self.assertEqual(
            list(gen_words_starting_at_char('MATT', 0)),
            ['M', 'MA', 'MAT', 'MATT']
        )
        self.assertEqual(
            list(gen_words_starting_at_char('MATT', 1)),
            ['A', 'AT', 'ATT']
        )

    def test_calc_score_from_subword(self):
        self.assertEqual(
            calc_score_from_subword('BANANA', 'B'), 1)
        self.assertEqual(
            calc_score_from_subword('BANANA', 'A'), 3)
        self.assertEqual(
            calc_score_from_subword('BANANA', 'AN'), 2)
        self.assertEqual(
            calc_score_from_subword('BANANA', 'NA'), 2)
        self.assertEqual(
            calc_score_from_subword('ABCABCABC', 'ABC'), 3)
        self.assertEqual(
            calc_score_from_subword('ABCABCABC', 'BCA'), 2)

    def test_calculate_score(self):
        self.assertEqual(
            calculate_score('BANANA', vowel_start=False), 12)
        self.assertEqual(
            calculate_score('BANANA', vowel_start=True), 9)
            
if __name__ == '__main__':
    word = read_word() 
    stuart_score = calculate_score(word, vowel_start=False)
    kevin_score = calculate_score(word, vowel_start=True)
    if stuart_score > kevin_score:
        print("Stuart {0}".format(str(stuart_score)))
    elif kevin_score > stuart_score:
        print("Kevin {0}".format(str(kevin_score)))
    else:
        print("Draw")
