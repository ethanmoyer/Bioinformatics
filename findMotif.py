from random import choice, random
import numpy as np

# Given length n, the function returns a random sequence n bp long.
def create_random_sequence(n):
	seq = ''
	for i in range(n):
	    seq += choice(nuc_list)
	return seq


# Given a sequence, motif, and the number of mismatches, the function returns a sequence with the motif (with given number of mismatches) randomly inserted in it.
def insert_random_motif(seq, motif, mismatches):
	i = int(random() * (len(seq) - len(motif)))
	if mismatches:
		for j in range(mismatches):
			k = int(random() * len(motif))
			motif = motif[:k] + create_random_sequence(1) + motif[k:]
	return seq[:i] + motif + seq[i:]


# Given a sequence and k, the function returns a random k-mer from the sequence,
def select_random_motif(seq, k):
	i = int(random() * (len(seq) - k))
	return seq[i:i + k]


# Given a list of motifs, the function returns the counts of each nucleotide (rows) across the length of the k-mers (columns).
def get_nuc_counts(motif_list):
	count_list = [[0] * len(motif_list[0]) for i in range(4)]
	for i in range(len(motif_list)):
		for j in range(len(nuc_list)):
			count_list[j][i] = [motif_list[k][i] for k in range(4)].count(nuc_list[j])
	return count_list


# Given a matrix of nucleotide counts across each position in a k-mer, the function returns a frequency matrix using Lapace's theorem: P(x = 1 | x1, x2, ..., xn = 1) = (s + 1) / (n + 2).
def get_nuc_frequency_laplace(nuc_counts):
	nuc_counts = (np.array(nuc_counts) + 1) / 8
	return nuc_counts.tolist()


# Given a sequence and length k, the function returns a list of the k-mers in the sequence.
def get_kmer_list(seq, k):
	return [seq[i:i + k] for i in range(len(seq) - k)]


# Given a matrix of nucleotide frequencies across each position in a k-mer and a list of k-mers, this function returns the probability of seeing each k-mer.
def get_kmer_probabilities(nuc_freq, kmers):
	probabilities = []
	for kmer in kmers:
		probability = 1
		for i in range(len(kmer)):
			probability *= nuc_freq[nuc_list.index(kmer[i])][i]
		probabilities.append(probability)
	return probabilities


# Given a list of sequences and k (motif length), the function randomly shuffles sequences according to gibbs sampler algorithm and returns the list of motifs that it deems to be the most prevalent of size k.
def gibbs_sampler(seq_list, k):
	motif_list = [select_random_motif(seq, k) for seq in seq_list]

	for i in range(1000):

		remove_i = int(random() * len(seq_list))

		del motif_list[remove_i]

		nuc_counts = get_nuc_counts(motif_list)
		nuc_frequency = get_nuc_frequency_laplace(nuc_counts)

		kmers = get_kmer_list(seq_list[remove_i], len(nuc_frequency[0]))

		kmer_probabilities = get_kmer_probabilities(nuc_frequency, kmers)

		index_max = kmer_probabilities.index(max(kmer_probabilities))

		new_motif = kmers[index_max]

		motif_list.insert(remove_i, new_motif)

	return motif_list


# Given two strings, the function returns the hamming distance between the two.
def hamdist(str0, str1):
        diffs = 0
        for ch1, ch2 in zip(str0, str1):
                if ch1 != ch2:
                        diffs += 1
        return diffs


if __name__ == '__main__':

	nuc_list = ['A', 'T', 'C', 'G']

	n = 10
	seq_list = [create_random_sequence(n) for i in range(5)]

	k = 4
	motif = create_random_sequence(4)

	seq_list = [insert_random_motif(seq, motif, 0) for seq in seq_list]

	motif_list = gibbs_sampler(seq_list, k)

	print(f'Motif: {motif}')
	print(f'Found motifs: {motif_list}')

	hamming_distance = [hamdist(motif, e) for e in motif_list]

	print(f'Hamming distances for all found motifs compared to actual motif: {hamming_distance}')
