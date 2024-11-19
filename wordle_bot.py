import random

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


if __name__ == "__main__":
    with open("./src/5LetterWords", "r") as f:
        words = f.readlines()
    words = {w.strip() for w in words if w[0] != "5"}
    print(f"Words: {len(words)}")

    most_vowels = get_most_vowels(words)
    first_sgg = random.sample(most_vowels, k=5)
    print(f"First suggestions: {first_sgg}")
    print("Remember, the word with most vowels are 'audio'!")

    nextline = input("Input: ")
    word, anno = nextline.split()
    anno = int(anno)
