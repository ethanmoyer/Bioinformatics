import numpy as np

def get_reverse_compliment(seq):
	nucleotides = 'AGCT'
	return ''.join([nucleotides[3 - nucleotides.index(nuc)] for nuc in seq])


def get_kmer_list(seq, k):
	return [seq[i:i + k] for i in range(len(seq) - k + 1)]


def get_synteny_blocks(seq0, seq1):

	kmer_list0 = get_kmer_list(seq0, 3)
	seq0_rc = get_reverse_compliment(seq0)
	kmer_list0_rc = get_kmer_list(seq0_rc, 3)

	kmer_list1 = get_kmer_list(seq1, 3)
	seq1_rc = get_reverse_compliment(seq1)
	kmer_list1_rc = get_kmer_list(seq1_rc, 3)

	grid = np.array([[1 if kmer1 == kmer0 or kmer1 == kmer_list0_rc[::-1][i][::-1] else 0 for i, kmer1 in enumerate(kmer_list1[::-1])] for kmer0 in kmer_list0])

	grid_rc = np.array([[1 if kmer1 == kmer0 else 0 for kmer1 in kmer_list1_rc] for kmer0 in kmer_list0_rc])

if __name__ == '__main__':
	seq0 = 'AGCAGGTTATCTACCTGT'
	seq1 = 'AGCAGGAGATAAACCTGT'

	synteny_blocks = get_synteny_blocks(seq0, seq1)