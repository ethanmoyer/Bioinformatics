# Assembling read pairs

from random import choice

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


#def walk_sequence(sequence, read_list, read_pairs_edges):



#sequence = create_random_sequence(15)
original_sequence = 'AGCTGTCGACTTGTG'
k = 6

overlap = 3

read_list = get_kmer_list(original_sequence, k)

read_pairs = get_read_pairs(read_list, overlap)

read_pairs_edges = get_read_pairs_edges(read_pairs)

i = 0

sequence = read_list[0][:3]

search = read_pairs_edges[0][1]

#while sequence != original_sequence
for i, read in enumerate(read_pairs_edges[:len(read_list) - overlap]):
	print(search)
	print(read[0])
	if search == read[0]:
		print(i)
		print(read_list[i])
		sequence += read_list[i]
		search = read_pairs_edges[i][1]