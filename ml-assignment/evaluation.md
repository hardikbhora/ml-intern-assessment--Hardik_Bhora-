## Design Choices for Trigram Language Model

This model was designed to implement a clean and basic trigram (N=3) language model that satisfies all test cases and follows the instructions in the assignment.

### 1. Data Structures

I used a nested dictionary implemented using `defaultdict`:

self.trigrams = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

Structure:
w1 → w2 → {w3: count}

Advantages:
- Clean, readable structure
- Automatic initialization without key errors
- Efficient for storing trigram frequency counts

A vocabulary set (`self.vocab`) was also maintained.

### 2. Text Cleaning

A `_clean_text()` helper function performs:
- Lowercasing
- Removing all characters except alphabets, periods, and spaces
- Simple tokenization using `split()`

This ensures consistent training data.

### 3. Handling Edge Cases

The model handles:

- Empty text:
  fit("") sets self.fitted = True and generate() returns ""
  
- Short text (< 3 words):
  Stored in vocab but no trigrams are created.
  generate() returns "" as required by tests.

This behavior is necessary to pass test_empty_text and test_short_text.

### 4. Training Logic

During fit():
- Clean text
- Split into tokens
- Build trigram counts through a sliding window:

for i in range(len(words) - 2):
    trigrams[w1][w2][w3] += 1

### 5. Generation Logic

The generate() method:
1. Returns "" if model is not fitted or has no trigrams
2. Randomly selects a starting bigram
3. Samples the next word probabilistically using `random.choices`
4. Generates up to 10 words

This produces random but meaningful output.

### 6. How to Run the Code

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest tests/test_ngram.py

### 7. Notes on Task 2

Task 2 is optional, so I skipped it.
