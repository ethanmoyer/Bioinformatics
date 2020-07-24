import copy

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


# Given a dictionary and a value, the function returns the keys at which this value appears. This is most useful for when different keys map to the same value and inverting the dictionary would change its length.
def get_keys_with_value(dict_, value):
	keys = list(dict_.keys())
	values = list(dict_.values())
	return [keys[e] for e in get_index_positions(values, value)]


# Given a protein represented as a string, the function returns the total mass of that protein according to an integer mass dictionary.
def sum_integer_mass(protein):
	mass = 0
	for e in protein:
		mass += protein_integer_mass_dict[e]
	return mass


if __name__ == '__main__':
	# Integer mass dictionary of all of the amino acids commonly found in a protein.
	protein_integer_mass_dict = {'G': 57, 'A': 71, 'S': 87,'P': 97, 'V': 99, 
							'T': 101, 'C': 103, 'I': 113, 'L': 133, 'N': 114, 
							'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
							'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

	# Spectrum of circular protein
	spectrum = [0, 97, 97, 99, 101, 103, 196, 198, 198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 398, 400, 400, 497]

	# Obtain the first bases of the protein sequence according to the spectrum above.
	canidate_proteins = [get_keys_with_value(protein_integer_mass_dict, e) for e in spectrum]

	# Remove empty lists and unlist the single amino acids
	canidate_proteins = list(set([protein for proteins_ in canidate_proteins for protein in proteins_]))

	# Display potential starting amino acids of the protein
	print(canidate_proteins)

	# List of all amino acids that are added on the current peptides during every iteration of the search.
	aa = list(protein_integer_mass_dict.keys())

	# Continue while there are more than one candidate protein
	while len(canidate_proteins) > 1:

		# Branch step. Add all of the current candidates with every amino acid
		canidate_proteins = [e + protein for e in canidate_proteins for protein in aa]

		# Find all non-proper substrings of the canidate proteins
		canidate_proteins_split = [[protein[i: j] for i in range(len(protein)) for j in range(i + 1, len(protein) + 1)] for protein in canidate_proteins]

		# New list for consistent candidates 
		canidate_proteins_ = []

		# Loop through all of the protein splits
		for i, canidate_protein_split in enumerate(canidate_proteins_split):

			# Copy spectrum and successively remove from the copy to find inconsistent peptides
			spectrum_ = copy.deepcopy(spectrum)

			# Loop through each split in the peptide
			for peptide_split in canidate_protein_split:

				# Find the mass of the split and remove it from the copy of spectrum if it exists. Otherwise, break.
				peptide_mass = sum_integer_mass(peptide_split)
				if peptide_mass in spectrum_:
					spectrum_.remove(peptide_mass)
				else:
					break
			# If loop finishes for all peptide slits, add to new candidate list for next round. Bound step.
			else:
				canidate_proteins_.append(canidate_proteins[i])
		# Print list if there are new candidate proteins
		if canidate_proteins_ != []:
			print(canidate_proteins_)
		canidate_proteins = canidate_proteins_


