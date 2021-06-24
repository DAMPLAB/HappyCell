"""
--------------------------------------------------------------------------------
Description: this function is looking for restriction sites on plasmid

Written by [Beining Ouyang] [bouyang@bu.edu], [Jun.14.2021]
[PROJECT LICENCSE HERE] N/A
--------------------------------------------------------------------------------
"""

# create a dic for res. sites
res_site_map = {
    "NotI": 'GCGGCCGC',
    "XhoI": 'CTCGAG',
}


def find_site(sequence: str) -> dict[str, int]:
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

#  modular testing
#  if __name__ == '__main__':
#     a = "CTCGAGsdsaaaaweeqeeqweeCTCGAGsdaasdsdsd "
#     print(find_site(a))
