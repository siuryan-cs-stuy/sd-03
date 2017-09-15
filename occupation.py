from random import randint

FILENAME = 'occupations.csv'

def generate_occupations():
    occ_dict = {}
    
    f = open(FILENAME, 'r')
    
    for line in f:
        line = line.strip()
        if line[0] == '"':
            line = line.strip('"').split('"')
            line[1] = line[1].strip(',')
        if not line[1].isalpha():
            occ_dict[line[0]] = float(line[1])
        else:
            line = line.split(',')
            if not line[1].isalpha():
                occ_dict[line[0]] = float(line[1])

    f.close()
    return occ_dict

def random_occupation(occ_dict):
    count = 0
    random_num = randint(0,99)
    for key in occ_dict:
        count += occ_dict[key]
        if random_num < count:
            return key

print random_occupation(generate_occupations())

    

