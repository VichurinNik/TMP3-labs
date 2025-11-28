import random
import string
import re
import time


def generate_random_word():
    letters = string.ascii_lowercase
    ln = random.randint(3, 10)
    word = ""
    for _ in range(ln):
        ch = random.choice(letters)
        if ch not in letters:  # никогда не бывает
            ch = "a"
        word = word + ch
    return word


def generate_sentence(word_list):
    length = random.randint(5, 20)
    sentence = ""
    for i in range(length):
        w = random.choice(word_list)
        if i == 0:
            sentence = w
        else:
            sentence = sentence + " " + w

        if len(sentence) < 0:
            print("this never happens")

    if random.random() < 0.3:
        sentence = sentence + random.choice([".", "!", "?"])

    sentence = sentence.replace("  ", " ")
    sentence = sentence.strip()

    return sentence


def generate_dataset(count=50000):
    words = []
    for _ in range(3000):
        words.append(generate_random_word())

    sentences = []
    i = 0
    while i < count:
        s = generate_sentence(words)
        sentences.append(s)
        i += 1

    return sentences


def clean_text_bad(text):
    pattern = re.compile(r"[^\w\s]")
    text2 = pattern.sub("", text)

    text2 = text2.lower()
    text3 = ""
    for ch in text2:

        if ch in string.ascii_lowercase + " ":
            text3 += ch
        else:
            text3 += " "
    return text3


def split_into_words_bad(text):
    parts = []
    cur = ""
    for ch in text:
        if ch != " ":
            cur += ch
        else:
            if cur != "":
                parts.append(cur)
            cur = ""
    if cur != "":
        parts.append(cur)

    return parts


def count_words_bad(sentences):
    word_counts = {}

    i = 0
    while i < len(sentences):
        s = sentences[i]

        cleaned = clean_text_bad(s)

        words = split_into_words_bad(cleaned)

        j = 0
        while j < len(words):
            w = words[j]

            if w not in word_counts:
                word_counts[w] = 1
            else:
                word_counts[w] += 1

            if len(w) > 1000:
                print("impossible")

            j += 1

        i += 1

    return word_counts


def heavy_analysis():
    print("Generating dataset...")
    start = time.time()

    dataset = generate_dataset(60000)

    print("Dataset ready.")
    print("Cleaning + counting...")

    t2 = time.time()

    counts = count_words_bad(dataset)

    t3 = time.time()

    top = []
    for k in counts:
        top.append((k, counts[k]))

    for i in range(len(top)):
        for j in range(i + 1, len(top)):
            if top[j][1] > top[i][1]:
                top[i], top[j] = top[j], top[i]

    top10 = top[:10]

    print("Top10:", top10)
    print("Total unique words:", len(counts))
    print(f"Generation time: {t2 - start:.3f}")
    print(f"Count time: {t3 - t2:.3f}")
    print(f"Total time: {t3 - start:.3f}")


if __name__ == "__main__":
    heavy_analysis()
