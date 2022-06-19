import json

from flask import Flask, request

from collections import defaultdict
from random import choice, shuffle, randrange


DICTIONARY = open("./sowpods")

app = Flask(__name__)


""" Prepare the data """


def cleanData(data):
    words = {}  # length: [words, ...]
    for word in DICTIONARY:
        word = word.replace('\n', '')
        if len(word) not in words:
            words[len(word)] = [word]
        else:
            words[len(word)].append(word)
    return words


words = cleanData(DICTIONARY)


""" Front page of the website """


@app.route("/")
def index():
    return "hello world!!!"


""" Find all the anagrams of a word endpoint """


@app.route("/anagrams")
def anagrams():
    prompt = request.args.get("prompt")
    if prompt is None or len(prompt) <= 0:
        return "Please add a valid prompt in anagrams. Example: /anagrams?prompt=pots", 400
    return json.dumps({"result": find_anagrams(prompt.upper())})


""" Find all the anagrams of a word """


def find_anagrams(prompt):
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


""" Generate a puzzle based on a diffculty of 0 - 2 """


@app.route("/generatePuzzle")
def generatePuzzle():
    diff = request.args.get("difficulty")
    if diff is None or len(diff) <= 0:
        return "Please add a valid diff in generatePuzzle. Example: /generatePuzzle?difficulty=1. difficulty is between 0 - 2", 400
    diff = int(diff)
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
    else:
        return "Please add a valid diff in generatePuzzle. Example: /generatePuzzle?difficulty=1. difficulty is between 0 - 2", 400
    randomWord = choice(words[randomList])
    randomWordList = list(randomWord)
    shuffle(randomWordList)
    randomWordNew = "".join(randomWordList)
    return json.dumps({"result": randomWordNew})


""" Verify a puzzle equates to a guess """


@app.route("/verify")
def verify():
    puzzle = request.args.get("puzzle")
    if puzzle is None or len(puzzle) <= 0:
        return "Please add a valid puzzle in verify. Example: /verify?puzzle=lleho&guess=hello.", 400
    guess = request.args.get("guess")
    if guess is None or len(guess) <= 0:
        return "Please add a valid guess in verify. Example: /verify?puzzle=lleho&guess=hello.", 400
    puzzle = list(puzzle)
    for char in guess:
        if char not in puzzle:
            return json.dumps({"result": False})
        else:
            puzzle.remove(char)
    return json.dumps({"result": len(puzzle) == 0})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
