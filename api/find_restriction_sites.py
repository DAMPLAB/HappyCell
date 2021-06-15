"""
--------------------------------------------------------------------------------
Description: this function is looking for restriction sites on plasmid

Written by [Beining Ouyang] [bouyang@bu.edu], [Jun.14.2021]
[PROJECT LICENCSE HERE] N/A
--------------------------------------------------------------------------------
"""
import os

def find_site(sequence, re_site):
    """
    :type sequence: str
    :type re_site: str
    """
    sites_index = []
    if len(re_site) == 0:
        return 0
    else:
        for i in range(len(sequence) - len(re_site) + 1):
            if sequence[i:(i + len(re_site))] == re_site:
                sites_index.append(i)
        return sites_index

def load_genome(filepath):
    """
    return a str of genome
    """
    if not os.path.isfile(filepath):
        raise TypeError(filepath + " does not exist")
    genome = open(filepath).read().replace('\n','')
    return genome

def load_sites(filepath):
#Load sites from list of filenames and return list of strings
    if not os.path.isfile(filepath):
        raise TypeError(filepath + " does not exist")
    site = open(filepath).read().replace('\n','')
    return site

def get_restriction_sites(genome_fp, restriction_fp):
    # Load data, search, and return indices of each restriction site as dictionary
    if not os.path.isfile(genome_fp) or not os.path.isfile(restriction_fp):
        raise TypeError("file does not exist")
    a = load_genome(genome_fp)
    b = load_sites(restriction_fp)
    return (find_site(a,b))


a="files/pCI_neo_sequence.fasta"
b="files/XhoI.txt"
print(get_restriction_sites(a,b))

