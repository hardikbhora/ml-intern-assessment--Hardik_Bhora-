# Trigram Language Model – Instructions

## 1. Install dependencies
Run inside the project folder:
pip install -r requirements.txt

## 2. Run tests
pytest tests/test_ngram.py

## 3. Project Structure
ml-assignment/
├── src/
│   └── ngram_model.py
├── tests/
│   └── test_ngram.py
├── evaluation.md
└── data/

## 4. What the model does
- Cleans input text
- Builds trigram counts
- Uses probabilistic sampling to generate text
- Handles empty/short inputs
- Passes the provided tests

## 5. Example usage
from src.ngram_model import TrigramModel
model = TrigramModel()
model.fit("I am a test sentence.")
print(model.generate())
