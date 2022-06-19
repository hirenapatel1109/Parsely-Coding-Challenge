import json

from flask import Flask, request

from collections import defaultdict
from random import choice, shuffle, randrange


DICTIONARY = open("./sowpods")

app = Flask(__name__)


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


@app.route("/")
def index():
    return "hello world!!!"


@app.route("/anagrams")
def anagrams():
    prompt = request.args.get("prompt")
    if prompt is None or len(prompt) <= 0:
        return "Please add a valid prompt in anagrams. Example: /anagrams?prompt=pots", 400
    return json.dumps({"result": find_anagrams(prompt.upper())})


def find_anagrams(prompt):
    # call your solver entrypoint here, and return the result from this
    # function.
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
