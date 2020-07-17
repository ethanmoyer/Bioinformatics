from Bio import SeqIO

import matplotlib.pyplot as plt
import numpy as np

from random import random

# Determines if seq0 and seq1 are similar with at most t changes. 
def atmosttdifferences(seq0, seq1, t):
	count = 0
	for i in range(len(seq0)):
		if seq0[i] != seq1[i]:
			if count == t:
				return False
			else:
				count += 1
	return True


# Parses through the records and returns the sequence
def getFasta(fasta = "data/sequence.fasta"):
	records = []
	for record in SeqIO.parse(fasta, "fasta"):
		 records.append(record)
	return records


def findDnaA(sequence):
	gminusc = []
	gtotal = 0
	ctotal = 0

	# C rapidly mutates into T through deamination, which rates rise 100-fold when DNA is single stranded. 
	# - Forward half strand lives as ssDNA, decreasing C
	# - Reverse half strand lives as dsDNA, decreasing G
	for i in range(len(sequence)):
		if sequence[i] == 'G':
			gtotal += 1
		elif sequence[i] == 'C':
			ctotal += 1
		gminusc.append(gtotal - ctotal)

	# Plot G minus C vs position along the genome to find the transition from decreasing to increasing.
	plt.plot(gminusc)
	plt.title('OriC Detection Graph')
	plt.ylabel('G minus C')
	plt.xlabel('Position along the geome')	
	plt.show()

	# Find minimum index and isolate the sequence that's 500 bp long centered at that index
	min_idx = gminusc.index(min(gminusc))
	seq = sequence[min_idx - 250:min_idx + 250]

	# k = length of k-mers
	k = 9
	# t = most allowed mismatches in a k-mer
	t = 0

	# Fragments that are similar with t mismatches
	fragments = [[1 if atmosttdifferences(seq[i:i + k].seq, seq[j:j + k].seq, t) and i > j else 0 for i in range(len(seq) - k)] for j in range(len(seq) - k)]

	occurances = sum(np.array(fragments))

	# repeat positions and repeat sequences are returned by the function
	repeat_pos = np.where(occurances == 1)
	repeat_seq = [seq[i:i + k].seq for i in repeat_pos[0]]

	return repeat_seq, repeat_pos

if __name__ == '__main__':

	records = getFasta()
	sequence = records[0]
	repeat_seq, repeat_pos = findDnaA(sequence)

