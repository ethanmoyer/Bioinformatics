import numpy as np

# Given a list of elements and an element, the function returns all of the positions at which the element appears in the list.
def get_index_positions(list_of_elems, element):
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = list_of_elems.index(element, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

# let i be the rows
# let j be the columns

# returns max score and pointer
def calc_score(grid, i, j):
	match_mismatch = (match if seq1[i - 1] == seq0[j - 1] else mismatch)
	past_score_values = np.array([grid[i - 1][j - 1], grid[i - 1][j], grid[i][j - 1]])
	past_score_values = [e + match_mismatch for e in past_score_values] + [0]
	past_score_pointers = [[i - 1, j - 1], [i - 1, j], [i, j - 1], [0, 0]]

	max_score_value = max(past_score_values)
	max_score_indices = get_index_positions(past_score_values, max_score_value)
	max_score_points = [past_score_pointers[i] for i in max_score_indices]
	return max_score_value, max_score_points

def traceback(grid, pointer):

	align_seq0 = ''
	align_seq1 = ''

	x_rel = 1
	y_rel = 1

	while pointer != [0, 0]:

		x = pointer[0]
		y = pointer[1]

		align_seq0 = (seq0[y - 1] if x_rel == 1 else '-') + align_seq0
		align_seq1 = (seq1[x - 1] if y_rel == 1 else '-') + align_seq1
		next_pointers = grid_pointers[x - 1][y - 1]

		if len(next_pointers) == 1:
			pointer = next_pointers[0]
			x_rel = x - pointer[0]
			y_rel = y - pointer[1]
			continue

		pointer_scores = []
		for next_pointer in next_pointers:
			x_next = next_pointer[0]
			y_next = next_pointer[1]
			pointer_scores.append(grid[x_next][y_next])

		next_pointer_indices = get_index_positions(pointer_scores, max(pointer_scores))
		next_pointers = [next_pointers[i] for i in next_pointer_indices]

		pointer = next_pointers[0]
		x_rel = x - pointer[0]
		y_rel = y - pointer[1]

	return align_seq0, align_seq1

if __name__ == '__main__':

	match = 1
	mismatch = -1

	seq0 = 'TACGGGCCCGCTAC'
	seq1 = 'TAGCCCTATCGGTCA'

	grid = np.array([[0 for i in range(len(seq0) + 1)] for j in range(len(seq1) + 1)])
	grid_pointers = [[ [0, 0] for i in range(len(seq0))] for j in range(len(seq1))]


	for i in range(1, len(grid)):
		for j in range(1, len(grid[0])):
			grid[i][j], grid_pointers[i - 1][j - 1] = calc_score(grid, i, j)

	highest_score_pointers = np.argwhere(grid == np.max(grid)).tolist()

	for pointer in highest_score_pointers:
		align_seq0, align_seq1 = traceback(grid, pointer)
		print(align_seq0)
		print(align_seq1)
		print()

	i = 0



#	   	 0	 1   2   3   4	 5	 6	 7 	 8	 9	 10	 11	 12  13	 14	
#			 T   A   C   G   G   G   C   C   C   G   C   T   A   C
'''		 	 
array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],	  0
       [ 0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0],	T 1
       [ 0,  0,  2,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  1],	A 2
       [ 0,  0,  1,  1,  2,  3,  4,  3,  2,  1,  2,  1,  0,  1,  1],	G 3
       [ 0,  0,  0,  2,  1,  2,  3,  5,  6,  7,  6,  7,  6,  5,  6],	C 4
       [ 0,  0,  0,  3,  2,  1,  2,  6,  7,  8,  7,  8,  7,  6,  7],	C 5
       [ 0,  0,  0,  4,  3,  2,  1,  7,  8,  9,  8,  9,  8,  7,  8],	C 6
       [ 0,  1,  0,  3,  3,  2,  1,  6,  7,  8,  8,  8, 10,  9,  8],	T 7
       [ 0,  0,  2,  2,  2,  2,  1,  5,  6,  7,  7,  7,  9, 11, 10],	A 8
       [ 0,  1,  1,  1,  1,  1,  1,  4,  5,  6,  6,  6, 10, 10, 10],	T 9
       [ 0,  0,  0,  2,  1,  0,  0,  5,  6,  7,  6,  7,  9,  9, 11],	C 10
       [ 0,  0,  0,  1,  3,  4,  5,  4,  5,  6,  8,  7,  8,  8, 10],	G 11
       [ 0,  0,  0,  0,  4,  5,  6,  5,  4,  5,  9,  8,  7,  7,  9],	G 12
       [ 0,  1,  0,  0,  3,  4,  5,  5,  4,  4,  8,  8,  9,  8,  8],	T 13
       [ 0,  0,  0,  1,  2,  3,  4,  6,  7,  8,  7,  9,  8,  8,  9],	C 14
       [ 0,  0,  1,  0,  1,  2,  3,  5,  6,  7,  7,  8,  8,  9,  8]]) 	A 15
'''


