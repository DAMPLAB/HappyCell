import csv

# read pCIneo_res_sites and creat a dict of restriction sites
with open('../files/pCINeo_res_sites.txt', 'r') as pCI:
        reader = csv.reader(pCI, delimiter=' ')
        res_site_dict = {}
        for row in reader:
            res_site_dict[row[0]] = row[1]
        for key in res_site_dict:
             res_site_dict[key] = res_site_dict[key].replace('|', '')
             if '\t' in res_site_dict[key]:
                res_site_dict[key] = (res_site_dict[key][:res_site_dict[key].index('\t')]).upper()

#print(res_site_dict)


with open('../files/Alphabetized_List_of_Recognition_Specificities.txt', 'r') as Alph:
    reader = csv.reader(Alph, delimiter='	')
    Alph_res_site_dict = {}
    for row in reader:
        if len(row)<2:
            continue
        Alph_res_site_dict[row[1]] = row[0]
    for key in Alph_res_site_dict:
        Alph_res_site_dict[key] = Alph_res_site_dict[key].replace('/', '')

#print(Alph_res_site_dict)
