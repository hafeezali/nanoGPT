import nltk
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu
import os

nltk.download('punkt')

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def calculate_bleu_score(reference_list, candidate_list):
    # Tokenize the reference and candidate texts
    reference_tokens = []
    for line in reference_list:
        reference_tokens.extend(word_tokenize(line.lower()))

    candidate_tokens = []
    for line in candidate_list:
        candidate_tokens.extend(word_tokenize(line.lower()))

    # Calculate BLEU score
    bleu_score = sentence_bleu([reference_tokens], candidate_tokens)

    return bleu_score

if __name__ == "__main__":
    candidate_file = argv[1]  # Replace with your reference file path
    reference_file = "../data/" + argv[2]  # Replace with your candidate file path

    ref_lines = read_file(reference_file)
    candidate_lines = read_file(candidate_file)

    total_bleu_score = 0.0
    total_samples = 0

    for i in range(0, len(ref_lines), len(candidate_lines)):
        total_samples = total_samples + 1
        total_bleu_score = total_bleu_score + calculate_bleu_score(ref_lines[i:i+len(candidate_lines)], candidate_lines)

    bleu_score = total_bleu_score / total_samples
    print(f"BLEU Score: {bleu_score:.4f}")

