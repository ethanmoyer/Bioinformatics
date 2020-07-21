protein_integer_mass = {'G': 57, 'A': 71, 'S': 87,'P': 97, 'V': 99, 
						'T': 101, 'C': 103, 'I': 113, 'L': 133, 'N': 114, 
						'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
						'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

inv_protein_integer_mass = {v: k for k, v in protein_integer_mass.items()}

integer_mass = list(inv_protein_integer_mass.keys())
proteins = list(inv_protein_integer_mass.values())

tyro_b1 = 'VKLFPWFNQY'

spectrum = [0, 97, 97, 99, 101, 103, 196, 198, 198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 298, 400, 400, 497]

canidate_proteins = [inv_protein_integer_mass[e] for e in integer_mass if e in spectrum]

while len(canidates) > 1:
	canidate_proteins = [e + protein for e in canidate_proteins for protein in proteins]

	canidate_integer_mass = {}
	for protein in canidate_proteins:
		for aa in protein:
			if protein not in canidate_integer_mass:
				canidate_integer_mass[protein] = protein_integer_mass[aa]
			else:
				canidate_integer_mass[protein] += protein_integer_mass[aa]

	inv_canidate_integer_mass = {v: k for k, v in canidate_integer_mass.items()}

	integer_mass = list(inv_canidate_integer_mass.keys())
	proteins = list(inv_canidate_integer_mass.values())

	canidate_proteins = [inv_canidate_integer_mass[e] for e in integer_mass if e in spectrum]