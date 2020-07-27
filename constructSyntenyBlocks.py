import numpy as np

def get_reverse_compliment(seq):
	nucleotides = 'AGCT'
	return ''.join([nucleotides[3 - nucleotides.index(nuc)] for nuc in seq])


def get_kmer_list(seq, k):
	return [seq[i:i + k] for i in range(len(seq) - k + 1)]


def create_mker_grid(seq0, seq1, k):

	kmer_list0 = get_kmer_list(seq0, k)
	seq0_rc = get_reverse_compliment(seq0)
	kmer_list0_rc = get_kmer_list(seq0_rc, k)

	kmer_list1 = get_kmer_list(seq1, k)
	seq1_rc = get_reverse_compliment(seq1)
	kmer_list1_rc = get_kmer_list(seq1_rc, k)

	grid = np.array([[1 if kmer1 == kmer0 or kmer0 == kmer_list1_rc[::-1][i][::-1] else 0 for i, kmer1 in enumerate(kmer_list1[::-1])] for kmer0 in kmer_list0])

	return grid

def distance(p_i, p_j):
	return np.sqrt((p_i[0] - p_j[0])**2 + (p_i[1] - p_j[1])**2)


def get_synteny_blocks(grid, max_distance=2, min_size=3):
	
	grid_coords = np.where(grid == 1)
	x_coords = grid_coords[0]
	y_coords = grid_coords[1]

	n = len(x_coords)

	synteny_blocks_coords = []
	for c, coords_i in enumerate(zip(x_coords[:n - 1], y_coords[:n - 1])):
		for coords_j in zip(x_coords[c + 1:], y_coords[c + 1:]):
			x_i = coords_i[0]
			y_i = coords_i[1]

			x_j = coords_j[0]
			y_j = coords_j[1]

			if distance((x_i, y_i), (x_j, y_j)) <= max_distance:
				synteny_blocks_coords.append([coords_i, coords_j])

	# Merge the blocks
	synteny_blocks = []
	n = len(synteny_blocks_coords)
	for b, synteny_block_i in enumerate(synteny_blocks_coords[:n - 1]):
		synteny_block_max = max(synteny_block_i)
		for synteny_block_j in synteny_blocks_coords[b + 1:]:
			print(synteny_block_max)
			print(synteny_block_j)
			if synteny_block_max == min(synteny_block_j):
				synteny_block_max = max(synteny_block_j)

		synteny_blocks.append([min(synteny_block_i), synteny_block_max])
		print(synteny_blocks)
		quit()

	return [synteny_block for synteny_block in synteny_blocks if distance(min(synteny_block), max(synteny_block)) >= min_size]


if __name__ == '__main__':
	seq0 = 'AGCAGGTTATCTACCTGT'
	seq1 = 'AGCAGGAGATAAACCTGT'

	grid = create_mker_grid(seq0, seq1, 3)

	synteny_blockss = get_synteny_blocks(grid)


