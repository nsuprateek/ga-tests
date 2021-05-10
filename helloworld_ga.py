import random
from string import printable

answer = "Hello World!!"
population = []
SIZE = 10

def calcFitness(word):
    fitness = 0
    for i in range(len(word)):
        fitness += (ord(answer[i]) - ord(word[i])) ** 2
    return fitness

for i in range(SIZE):
    dna = [random.choice(printable) for j in range(len(answer))]
    fitness = calcFitness(dna)
    candidate = {'dna': dna, 'fitness': fitness}
    population.append(candidate)

def gimmeBaby(mom, dad):
    MUTATION_RATE = 1
    child_dna = mom['dna'][:]

    start = random.randint(0, len(dad['dna']) - 1)
    stop = random.randint(0, len(dad['dna']) - 1)
    if start > stop:
        stop, start = start, stop

    child_dna[start:stop] = dad['dna'][start:stop]

    pos = random.randint(0, len(child_dna) - 1)
    child_dna[pos] = chr(ord(child_dna[pos]) + random.randint(-1, 1)*MUTATION_RATE)
    child_fitness = calcFitness(child_dna)
    return {'dna': child_dna, 'fitness': child_fitness}


def chooseParent():
    rand = random.random() * random.random() * (SIZE - 1)
    rand = int(rand)
    return population[rand]


gen = 0

while True:
    population.sort(key=lambda candidate: candidate['fitness'])

    if population[-1]['fitness'] == 0:
    # if gen >= 5000:
        break


    gen += 1

    print('\nGENERATION - %d' % gen)
    for string in population:
        print('Fitness: %d -- %s' % (string['fitness'], ''.join(string['dna'])))
    # print('Gen - %d Best: %s' %(gen, ''.join(population[0]['dna'])))
    mom = chooseParent()
    dad = chooseParent()

    child = gimmeBaby(mom, dad)
    if child['fitness'] < population[-1]['fitness']:
        population[-1] = child
