import random
import string

VOWELS = {"u", "e", "o", "a", "i"}


def get_most_vowels(words: set[str]) -> list[str]:
    vowel_counts = []
    for w in words:
        vowel_count = set()
        for char in w:
            if char in VOWELS:
                vowel_count.add(char)
        vowel_counts.append((w, len(vowel_count)))

    vowel_counts.sort(key=lambda x: x[1], reverse=True)

    return [x[0] for x in vowel_counts if x[1] == vowel_counts[1][1]]


def get_score(word: str, wrong: dict, wrong_pos: dict, correct: dict) -> int:
    wrong_pos_count = {}
    score = 0

    for i, c in enumerate(word):
        if c in wrong:
            score -= 10
            continue

        if c in correct and i in correct[c]:
            score += 25
            continue

        if c in wrong_pos and i not in wrong_pos[c]:
            # count wrong pos and compare
            if c not in wrong_pos_count:
                wrong_pos_count[c] = 1
            else:
                wrong_pos_count[c] += 1

            c_count = wrong_pos_count[c]
            if c_count <= len(wrong_pos[c]):
                score += 10
            continue

    return score

def get_highest_score_words(words: list[str], wrong: dict, wrong_pos: dict, correct: dict) -> list[str]:
    scores = []
    for word in words:
        score = get_score(word, wrong, wrong_pos, correct)
        scores.append((word, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    res = [x for x in scores if x[1] == scores[0][1]]
    print(res[:10], wrong, wrong_pos, correct)
    return [x[0] for x in res]

def get_word_occurence(words: list, occurences: dict[str, int]) -> dict[str, int]:
    scores = {}
    for w in words:
        score = 0
        letters = set(list(w))
        for c in letters:
            score += occurences[c]
        
        scores[w] = score
    
    return scores


def get_letter_occurence(words: list) -> dict:
    occurences = {}
    for c in string.ascii_lowercase:
        occurences[c] = 0

    for w in words:
        letters = set(list(w))
        for c in letters:
            occurences[c] += 1
    return occurences


if __name__ == "__main__":
    with open("./src/5LetterWords", "r") as f:
        words = f.readlines()
    words = [w.strip() for w in words]

    print(f"Words: {len(words)}")

    letter_occurences = get_letter_occurence(words)
    word_occurence_scores = get_word_occurence(words, letter_occurences)

    scores = list(word_occurence_scores.items())
    scores.sort(key=lambda x: x[1], reverse=True)
    highest_occs = [x for x in scores if x[1] == scores[0][1]]
    first_sgg = random.sample(highest_occs, k=min(5, len(highest_occs)))
    print(f"First suggestions: {first_sgg}")

    wrong = set()
    wrong_pos: dict[str, set] = {}
    correct: dict[str, set] = {}
    while True:
        nextline = input("Input: ")
        word, anno = nextline.split()

        for i in range(5):
            letter_score = int(anno[i])
            letter = word[i]

            if letter_score == 0:
                wrong.add(letter)
            elif letter_score == 1:
                if letter in wrong_pos:
                    wrong_pos[letter].add(i)
                else:
                    wrong_pos[letter] = set([i])
            elif letter_score == 2:
                if letter in correct:
                    correct[letter].add(i)
                else:
                    correct[letter] = set([i])

        words = get_highest_score_words(words, wrong, wrong_pos, correct)
        # print(words)
        
