import nltk
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu
import os

nltk.download('punkt')

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_bleu_score(reference_file, candidate_file):
    reference_text = read_file(reference_file)
    candidate_text = read_file(candidate_file)

    # Tokenize the reference and candidate texts
    reference_tokens = word_tokenize(reference_text.lower())
    candidate_tokens = word_tokenize(candidate_text.lower())

    # Calculate BLEU score
    bleu_score = sentence_bleu([reference_tokens], candidate_tokens)

    return bleu_score

if __name__ == "__main__":
    reference_file = "2l12h/sample.txt"  # Replace with your reference file path
    candidate_file = "../data/shakespeare_char/input.txt"  # Replace with your candidate file path

    if not os.path.exists(reference_file) or not os.path.exists(candidate_file):
        print("Reference or candidate file not found.")
    else:
        bleu_score = calculate_bleu_score(reference_file, candidate_file)
        print(f"BLEU Score: {bleu_score:.4f}")
