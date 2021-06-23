"""
--------------------------------------------------------------------------------
Description: this function is looking for restriction sites on plasmid

Written by [Beining Ouyang] [bouyang@bu.edu], [Jun.14.2021]
[PROJECT LICENCSE HERE] N/A
--------------------------------------------------------------------------------
"""
import os
from typing import (
    List,
)

# create a dic for res. sites
restriction_site_map = {
    "NotI": 'GCGGCCGC',
    "XhoI": 'CTCGAG',
}



def find_site(sequence: str) -> List[int]:
    """
    Args:
        sequence: str of sequence
        re_site: restriction site

    Returns: return the index of the restriction site

    """
    sites_index = []

    for re_site in restriction_site_map:
        for i in range(len(sequence) - len(restriction_site_map[re_site]) + 1):
            if sequence[i: (i + len(restriction_site_map[re_site]))] \
                    == restriction_site_map[re_site]:
                sites_index.append(i)
        print(f'{repr(sequence)=}')
        print(f'{repr(restriction_site_map[re_site])=}')
    return sites_index


if __name__ == '__main__':
     current_location = os.path.abspath(__file__)
     #fasta_seq = os.path.join(Path(current_location).parent.parent.absolute(), 'files', 'pCI_neo_sequence.fasta')
     #res_site = os.path.join(Path(current_location).parent.parent.absolute(), 'files', 'XhoI.txt')
     a = "CTCGAGsdsaaaaweeqeeqweeCTCGAGsdaasdsdsd "
     print(find_site(a))
