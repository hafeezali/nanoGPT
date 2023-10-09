from bleu import file_bleu
import sys

hyp_file = sys.argv[2]

ref_file = sys.argv[1]

hyp = []
with open(hyp_file) as hf:
	hyp = hf.read().split('\n')

ref = []
with open(ref_file) as rf:
	ref = rf.read().split('\n')

hl = len(hyp)
bleu_score = 0
bleu_n = 0

for i in range(0, len(ref), hl):
	if i+hl < len(ref):
		bleu_n = bleu_n + 1
		bleu_score = bleu_score + list_bleu(ref[i:i+hl], hyp)

print(bleu_score/bleu_n)