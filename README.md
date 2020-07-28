# Bioinformatics

## Origin

These bioinformatics scripts are projects guided by and extended off of the lecture videos from bioinformaticsalgorithms.org. I really enjoy learning about bioinformatics, so I figured I would work on the projects and research topics, and then I could post them in this repository. 

## Mini-projects

### Lecture 1 - findOriC.py

Given a prokaryotic genome, the script locates the origin of replication region (OriC) using characteristics about the GC content throughout the genome. It then is able to find and return the most relevant 9-mer repeats (DnaA box) within that region.

### Lecture 2 - findMotif.py

This script displays the power of Gibbs Sampler, a randomized algorithm to finding motifs in a sequence. Motifs can either be inserted or discovered from random sequences.

### Lecture 3 - read-pairs.py

Given a sequence, the script fragments it into k-mer read pairs and aligns them using a Eulerian path algorithm. 

### Lecture 4 - proteinSequencing.py

Given a spectrum of peptide weights, the script reconstructs the unknown protein, assuming a perfect spectrum

### Lecture 5 - localAlignment.py

Given two sequences, the script returns the most optimal alignment of them using a custom scoring matrix. 

### Lecture 6 - constructSyntenyBlocks.py

Given two sequences, the script identifies synteny blocks of k-mers and returns their coordinates with respect to the k-mer list.

### Lecture 7 - neighborjoining.py

Given a distance matrix, the script applies the neighbor joining algorithm to construct an accurate biological tree.