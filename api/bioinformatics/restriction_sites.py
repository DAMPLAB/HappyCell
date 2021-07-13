"""
--------------------------------------------------------------------------------
Description: this function is looking for restriction sites on plasmid

Written by [Beining Ouyang] [bouyang@bu.edu], [Jun.14.2021]
[PROJECT LICENCSE HERE] N/A
--------------------------------------------------------------------------------
"""
import csv, os
from typing import (
    ByteString,
    Dict,
)

# create a dic for res. sites, we used some common restriction enzyme here
Alph_res_site_map = {
    "ApaI": 'GGGCCC',
    "BamHI": 'GGATCC',
    "BglII": 'AGATCT',
    "EcoRI": 'GAATTC',
    "HindIII": 'AAGCTT',
    "KpnI":	'GGTACC',
    "NcoI":	'CCATGG',
    "NdeI":	'CATATG',
    "NheI":	'GCTAGC',
    "NotI":	'GCGGCCGC',
    "SacI": 'GAGCTC',
    "SalI":	'GTCGAC',
    "SphI":	'GCATGC',
    "XbaI":	'TCTAGA',
    "XhoI":	'CTCGAG',
}




def format_fasta_file(sequence_file):
    """

    Args:
        sequence_file: a fasta file from frontend in byte, with sequence and unwanted headers,
        spaces,white line
    Returns:
        we decode here, get rid of headers, spaces, symbols, white lines
        return name of the this sequence and clean format of the sequence

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
    for re_site in Alph_res_site_map:
        for i in range(len(sequence) - len(Alph_res_site_map[re_site]) + 1):
            if sequence[i: (i + len(Alph_res_site_map[re_site]))] == Alph_res_site_map[re_site]:
                sites_index_map[re_site] = i
    return sites_index_map


def calculate_length_of_plasmid(sequence: str) -> int:
    """

    Args:
        sequence: sequence after format_fasta_file,
        clean sequence without headers
    Returns: length of the sequence

    """
    return len(sequence)


def all_res_site_dict(sites_file_path) -> Dict[str, str]:
    """

    Args:
        sites_file_path:
        a txt file path of Alphabetized List of Recognition Specificities
        https://www.neb.com/tools-and-resources/selection-charts/alphabetized-list-of-recognition-specificities

    Returns:
        a dict with all restriction endonuclease
        recognition specificities = {"Name": 'sequence'}...

    """
    with open(sites_file_path, 'r') as all_sites:
        reader = csv.reader(all_sites, delimiter='	')
        Alph_res_site_dict = {}
        for row in reader:
            if len(row) < 2:
                continue
            Alph_res_site_dict[row[1]] = row[0]
        for key in Alph_res_site_dict:
            Alph_res_site_dict[key] = Alph_res_site_dict[key].replace('/', '')
        # TODO: should not get rid of "/" it is useful information
    return Alph_res_site_dict


# cwd = os.getcwd()
# file_root = os.path.join(os.getcwd(), 'files')
# all_sites_fp = os.path.join(file_root, 'Alphabetized_List_of_Recognition_Specificities.txt')
# Alph_res_site_map = all_res_site_dict(all_sites_fp)



