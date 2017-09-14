from random import randint

FILENAME = 'occupations.csv'

def generate_occupations():
    occ_dict = {}
    
    f = open(FILENAME, 'r')
    
    for line in f:
        line = line.strip()
        if line[0] == '"':
            occupation = line.strip('"').split('"')
            occupation[1] = occupation[1].strip(',')
        if not occupation[1].isalpha():
            occ_dict[occupation[0]] = float(occupation[1])
        else:
            line = line.split(',')
            if not line[1].isalpha():
                occ_dict[line[0]] = float(line[1])

    f.close()
    return occ_dict

def random_occupation(occ_dict):
    random_num = randint(0,99)

    

