# Assembling read pairs

from random import choice, shuffle

nuc_list = ['A', 'T', 'C', 'G']

def create_random_sequence(n):
	seq = ''
	for i in range(n):
	    seq += choice(nuc_list)
	return seq

def get_kmer_list(seq, k):
	return [seq[i:i + k] for i in range(len(seq) - k + 1)]


def get_read_pairs(read_list, overlap=3):
	return [[read[:overlap], read[len(read) - overlap:]] for read in read_list]


def get_read_pairs_edges(read_pairs):
	edge_len = len(read_pairs[0][0])
	node_len = edge_len - 1
	return [[[read[:node_len], read[edge_len - node_len:]] for read in pair] for pair in read_pairs]


def shuffle_reads(read_list, read_pairs_edges):
	read_list_and_pairs_edges = list(zip(read_list, read_pairs_edges))
	shuffle(read_list_and_pairs_edges)
	read_list, read_pairs_edges = zip(*read_list_and_pairs_edges)
	return list(read_list), read_pairs_edges


def align_reads(original_sequence, read_pairs_edges, read_list, overlap):
	sequence = read_list[0]

	search = read_pairs_edges[0][1]

	read_list, read_pairs_edges = shuffle_reads(read_list, read_pairs_edges)

	#while sequence != original_sequence
	for j in range(len(read_list)):
		for i, read in enumerate(read_pairs_edges[:len(read_list)]):
			print('search:', search)
			print('read:', read)
			if search == read[0]:
				print('added:', read_list[i][overlap:])
				sequence += read_list[i][overlap:]
				search = read_pairs_edges[i][1]
				if len(sequence) == len(original_sequence):
					return sequence

	return sequence


if __name__ == '__main__':
	original_sequence = create_random_sequence(18)
	#original_sequence = 'AGCTGTCGACTTGTG'
	k = 6
	overlap = 3

	read_list = get_kmer_list(original_sequence, k)

	read_pairs = get_read_pairs(read_list, overlap)

	read_pairs_edges = get_read_pairs_edges(read_pairs)

	sequence = align_reads(original_sequence, read_pairs_edges, read_list, overlap)

	print('Original sequence\t', original_sequence)
	print('Aligned sequence\t', sequence)
