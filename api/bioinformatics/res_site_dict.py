# import csv
# from typing import Dict
#
#
# def all_res_site_dict(sites_file_path) -> Dict[str, str]:
#     """
#
#     Args:
#         sites_file_path:
#         a txt file path of Alphabetized List of Recognition Specificities
#         https://www.neb.com/tools-and-resources/selection-charts/alphabetized-list-of-recognition-specificities
#
#     Returns:
#         a dict with all restriction endonuclease
#         recognition specificities = {"Name": 'sequence'}...
#
#     """
#
#     with open(sites_file_path, 'r') as all_sites:
#         reader = csv.reader(all_sites, delimiter='	')
#         Alph_res_site_dict = {}
#         for row in reader:
#             if len(row) < 2:
#                 continue
#             Alph_res_site_dict[row[1]] = row[0]
#         for key in Alph_res_site_dict:
#             Alph_res_site_dict[key] = Alph_res_site_dict[key].replace('/', '')
#     return Alph_res_site_dict
#
# Alph_res_site_map = all_res_site_dict('../files/Alphabetized_List_of_Recognition_Specificities.txt')