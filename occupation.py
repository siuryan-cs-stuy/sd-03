import random

FILENAME = 'occupations.csv'
NUM_ITERATIONS = 1000000

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
    random_num = random.random()*100
    for key in occ_dict:
        count += occ_dict[key]
        if random_num < count:
            return key

def print_test_random(num):
    counter = {}
    occupations = generate_occupations()
    for key in occupations:
        counter[key] = 0

    for i in range(0,num):
        counter[random_occupation(occupations)] += 1

    for key in counter:
        #print key + ': ' + str(counter[key])
        print key + ': ' + str(round(percent_error(occupations[key]*NUM_ITERATIONS/100, counter[key]), 2)) + '%'

def percent_error(actual, measured):
    return abs((actual-measured)/actual)*100

# To test randomness of random selection
#print 'Percent error of each occupations for ' + str(NUM_ITERATIONS) + ' ITERATIONS'
#print_test_random(NUM_ITERATIONS)

# To print a random occupation
print random_occupation(generate_occupations())
