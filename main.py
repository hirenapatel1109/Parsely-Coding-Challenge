"""
1. generate puzzles of varying difficulty
  difficulty: more letters = more difficult
2. verify that the answers provided for a puzzle are correct
  0: <= 5 characters
  1: 5 - 14 characters
  2: 14 + characters
  can be 1 at a time, return True or Flase
3. generate unsolvable puzzles that look like solvable ones
  randomization of characters
  3 <= letters <= 20

the puzzle “dgo” has the solutions “dog” and “god”
"""
from collections import defaultdict
from random import choice, shuffle, randrange


DICTIONARY = open("./sowpods")


def generatePuzzle(diff: int, words):
    if diff < 0 or diff > 2:
        return "ERROR: Please use 0-2 difficulty"
    randomList = None
    wordLens = list(words.keys())
    if diff == 0:
        randomList = choice(wordLens[:len(words) // 3])
    elif diff == 1:
        randomList = choice(wordLens[len(words) // 3:len(words) * 2 // 3])
    elif diff == 2:
        randomList = choice(wordLens[2 * len(words) // 3:])
    randomWord = choice(words[randomList])
    randomWordList = list(randomWord)
    shuffle(randomWordList)
    randomWordNew = "".join(randomWordList)
    # print(randomWord, randomWordNew)
    return randomWordNew


def cleanData(data):
    words = {}  # length: [words, ...]
    for word in DICTIONARY:
        word = word.replace('\n', '')
        if len(word) not in words:
            words[len(word)] = [word]
        else:
            words[len(word)].append(word)
    return words


def verify(puzzle, guess):
    puzzle = list(puzzle)
    for char in guess:
        if char not in puzzle:
            return False
        else:
            puzzle.remove(char)
    return len(puzzle) == 0

    # def find_anagrams(prompt):


def find_anagrams(prompt, words):
    potentialWords = words[len(prompt)]
    sortedPrompt = ''.join(sorted(prompt))
    print(prompt, sortedPrompt)
    answer = []
    for word in potentialWords:
        sortedWord = ''.join(sorted(word))
        if sortedWord == sortedPrompt:
            answer.append(word)
    print(answer)
    return answer


if __name__ == "__main__":
    words = cleanData(DICTIONARY)
    print(generatePuzzle(0, words))
    print(generatePuzzle(0, words))
    print(generatePuzzle(1, words))
    print(generatePuzzle(1, words))
    print(generatePuzzle(2, words))
    print(generatePuzzle(2, words))
    print(generatePuzzle(2, words))
    print(verify("SPRAYS", "ARPSSY"))
    print(verify("SPRAYS", "ARPSSYS"))
    print(verify("SPRAYS", "A"))
    print(verify("SPRAYS", ""))
    print(verify("", "ARPSSY"))
    print(verify("R", "ARPSSY"))
    print(verify("S", "SSSSSS"))
    print(verify("SSSS", "S"))
    print(verify("SSSS", "SSSS"))
    print("____")
    print(find_anagrams("SASRPY", words))
