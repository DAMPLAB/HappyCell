"""
--------------------------------------------------------------------------------
Description: this function is looking for restriction sites on plasmid

Written by [Beining Ouyang] [bouyang@bu.edu], [Jun.14.2021]
[PROJECT LICENCSE HERE] N/A
--------------------------------------------------------------------------------
"""
#  from res_site_dict import Alph_res_site_dict, pCI_res_site_dict
from typing import (
    ByteString,
    Dict,
)

# create a dic for res. sites
res_site_map = {
  "NotI": 'GCGGCCGC',
  "XhoI": 'CTCGAG',
}

def format_fasta_file(sequence_file):
    """

    Args:
        sequence_file:

    Returns:

    """
    input_text = sequence_file.decode('UTF-8')
    # input_text was in byte, we decode it here
    genomic_code = input_text.split("\n")[1:]
    sequence_name = input_text.split("\n")[0].replace(">", "").split(',')[0]
    genomic_code = "".join(genomic_code)
    removal_list = [", ", "'", "[", "]"]
    for entry in removal_list:
        genomic_code = genomic_code.replace(entry, '')
    return sequence_name, input_text

def find_site(sequence: str) -> Dict[str, int]:
    """
    Args:
        sequence: str of sequence
    Returns: return a dict: key: str, name of the res. sites., value:
    index of the restriction sites
    """
    sites_index_map = {}
    for re_site in res_site_map:
        for i in range(len(sequence) - len(res_site_map[re_site]) + 1):
            if sequence[i: (i + len(res_site_map[re_site]))] == res_site_map[re_site]:
                sites_index_map[re_site] = i
    return sites_index_map


def calculate_length_of_plasmid(sequence: str) -> int:
    """

    Args:
        sequence:

    Returns:

    """
    return len(sequence)


if __name__ == "__main__":
    string = "TCAATATTGGCCATTAGCCATATTATTCATTGGTTATATAGCATAAATCAATATTGG" \
             "CTATTGGCCATTGCATACGTTGTATCTATATCATAATATGTACATTTATATTGGCTCAT" \
             "GTCCAATATGACCGCCATGTTGGCATTGATTATTGACTAGTTATTAATAGTAATCAATTA" \
             "CGGGGTCATTAGTTCATAGCCCATATATGGAGTTCCGCGTTACATAACTTACGGTAAATGGCC" \
             "CGCCTGGCTGACCGCCCAACGACCCCCGCCCATTGACGTCAATAATGACGTATGTTCCCATAGT" \
             "AACGCCAATAGGGACTTTCCATTGACGTCAATGGGTGGAGTATTTACNGCGGCCGC"
    print(find_site(string))
