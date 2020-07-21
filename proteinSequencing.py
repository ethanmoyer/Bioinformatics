import copy

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

def get_keys_with_value(dict_, element):
	keys = list(dict_.keys())
	values = list(dict_.values())
	return [keys[e] for e in get_index_positions(values, element)]


protein_integer_mass_dict = {'G': 57, 'A': 71, 'S': 87,'P': 97, 'V': 99, 
						'T': 101, 'C': 103, 'I': 113, 'L': 133, 'N': 114, 
						'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
						'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

get_keys_with_value(protein_integer_mass_dict, 128)

tyro_b1 = 'VKLFPWFNQY'

spectrum = [0, 97, 97, 99, 101, 103, 196, 198, 198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 298, 400, 400, 497]

canidate_proteins = [get_keys_with_value(protein_integer_mass_dict, e) for e in spectrum]

canidate_proteins = list(set([protein for proteins_ in canidate_proteins for protein in proteins_]))

proteins = list(protein_integer_mass_dict.keys())
integer_mass = list(protein_integer_mass_dict.values())

while len(canidate_proteins) > 1:
	canidate_proteins = [e + protein for e in canidate_proteins for protein in proteins]

	canidate_integer_mass_dict = {}
	for protein in canidate_proteins:
		for aa in protein:
			if protein not in canidate_integer_mass_dict:
				canidate_integer_mass_dict[protein] = protein_integer_mass_dict[aa]
			else:
				canidate_integer_mass_dict[protein] += protein_integer_mass_dict[aa]

	canidate_names = list(canidate_integer_mass_dict.keys())
	canidate_integer_mass = list(canidate_integer_mass_dict.values())

	canidate_proteins = [get_keys_with_value(canidate_integer_mass_dict, e) for e in spectrum]

	canidate_proteins = list(set([protein for proteins_ in canidate_proteins for protein in proteins_]))

	canidate_proteins_split = [[protein[i: j] for i in range(len(protein)) for j in range(i + 1, len(protein) + 1)] for protein in canidate_proteins]

	canidate_proteins_ = []

	for i, canidate_protein_split in enumerate(canidate_proteins_split):
		spectrum_ = copy.deepcopy(spectrum)
		for peptide_split in canidate_protein_split:
			# Don't longer proteins!
			if len(peptide_split) > 1:
				continue
			peptide_mass = protein_integer_mass_dict[peptide_split]
			if peptide_mass in spectrum_:
				spectrum_.remove(peptide_mass)
			else:
				break
		else:
			canidate_proteins_.append(canidate_proteins[i])

	canidate_proteins = canidate_proteins_



