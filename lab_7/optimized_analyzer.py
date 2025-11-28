import random
import string
import re
import time
import collections


def generate_random_word_optimized():
    length = random.randint(3, 10)
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def generate_sentence_optimized(word_list):
    length = random.randint(5, 20)
    words = random.choices(word_list, k=length)
    sentence = ' '.join(words)

    if random.random() < 0.3:
        sentence += random.choice([".", "!", "?"])

    return sentence


def generate_dataset_optimized(count=50000):
    words = [generate_random_word_optimized() for _ in range(3000)]
    sentences = [generate_sentence_optimized(words) for _ in range(count)]
    return sentences


def clean_text_optimized(text):
    text = re.sub(r'[^a-z\s]', '', text.lower())
    return text


def split_into_words_optimized(text):
    return text.split()


def count_words_optimized(sentences):
    word_counts = collections.Counter()

    for sentence in sentences:
        cleaned = clean_text_optimized(sentence)
        words = split_into_words_optimized(cleaned)
        word_counts.update(words)

    return word_counts


def heavy_analysis_optimized():
    print("Generating dataset (OPTIMIZED)...")
    start = time.time()

    dataset = generate_dataset_optimized(60000)

    print("Dataset ready.")
    print("Cleaning + counting...")

    t2 = time.time()

    counts = count_words_optimized(dataset)

    t3 = time.time()

    top10 = counts.most_common(10)

    print("Top10:", top10)
    print("Total unique words:", len(counts))
    print(f"Generation time: {t2 - start:.3f}")
    print(f"Count time: {t3 - t2:.3f}")
    print(f"Total time: {t3 - start:.3f}")


if __name__ == "__main__":
    heavy_analysis_optimized()
