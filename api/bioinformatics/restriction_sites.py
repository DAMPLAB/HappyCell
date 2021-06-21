"""
--------------------------------------------------------------------------------
Description: this function is looking for restriction sites on plasmid

Written by [Beining Ouyang] [bouyang@bu.edu], [Jun.14.2021]
[PROJECT LICENCSE HERE] N/A
--------------------------------------------------------------------------------
"""
import os
from pathlib import Path
from typing import (
    List,
)


def find_site(sequence: str, re_site: str) -> List[int]:
    """

    Args:
        sequence:
        re_site:

    Returns:

    """
    sites_index = []
    if not re_site:
        return 0
    else:
        for i in range(len(sequence) - len(re_site) + 1):
            if sequence[i: (i + len(re_site))] == re_site:
                sites_index.append(i)
        return sites_index


def load_file(filepath: str) -> str:
    """
        return a str of genome

    Args:
        filepath:

    Returns:

    """
    if not os.path.isfile(filepath):
        raise TypeError(f'{filepath} does not exist.')
    genome = open(filepath).read().replace("\n", "")
    return genome


def get_restriction_sites(
        genome_fp: str,
        restriction_fp: str,
) -> List[int]:
    """

    Args:
        genome_fp: path of the mRNA file??
        restriction_fp: path of the restriction sites files

    Returns: Load data, search, and return index of each restriction site as dictionary

    """

    if not os.path.isfile(genome_fp) or not os.path.isfile(restriction_fp):
        raise TypeError("file does not exist")
    a = load_file(genome_fp)
    b = load_file(restriction_fp)
    return find_site(a, b)


# if __name__ == '__main__':
#     current_location = os.path.abspath(__file__)
#     fasta_seq = os.path.join(Path(current_location).parent.parent.absolute(), 'files', 'pCI_neo_sequence.fasta')
#     res_site = os.path.join(Path(current_location).parent.parent.absolute(), 'files', 'XhoI.txt')
#     # a = "files/pCI_neo_sequence.fasta"
#     # b = "files/XhoI.txt"
#     print(get_restriction_sites(fasta_seq, res_site))
