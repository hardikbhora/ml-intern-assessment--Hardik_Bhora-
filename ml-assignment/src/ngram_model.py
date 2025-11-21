import random
import re
from collections import defaultdict


class TrigramModel:
    def __init__(self):
        self.trigrams = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        self.vocab = set()
        self.fitted = False

    def _clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z. ]+", "", text)
        return text

    def fit(self, text):
        text = self._clean_text(text).strip()

        if not text:
            self.fitted = True
            return

        words = text.split()

        if len(words) < 3:
            self.vocab.update(words)
            self.fitted = True
            return

        self.vocab.update(words)

        for i in range(len(words) - 2):
            w1, w2, w3 = words[i], words[i + 1], words[i + 2]
            self.trigrams[w1][w2][w3] += 1

        self.fitted = True

    def generate(self):
        
        if not self.fitted:
            return ""

        
        if not self.trigrams:
            return ""

        
        w1 = random.choice(list(self.trigrams.keys()))
        w2 = random.choice(list(self.trigrams[w1].keys()))

        generated_words = [w1, w2]

        
        for _ in range(10):
            next_words = self.trigrams.get(w1, {}).get(w2, {})
            if not next_words:
                break

            words = list(next_words.keys())
            counts = list(next_words.values())

            total = sum(counts)
            probs = [c / total for c in counts]

            next_word = random.choices(words, probs)[0]
            generated_words.append(next_word)

            w1, w2 = w2, next_word

        return " ".join(generated_words)
