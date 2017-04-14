import random
import math

population_size = 100
mutation_rate = 0.01
start_gen = 0

class population:


    def __init__(self, user):
        self.generation = start_gen
        self.size = population_size
        self.dna = []
        for i in range(self.size):
            self.dna.append(dna(user))
            print(self.dna[i].gene)

    def generated(self):
        for i in range(self.size):
            if self.dna[i].gene == self.user:
                return True
        return False

    def reproduce(self):
        pool = []
        self.dna = []
        self.generation+=1
        for i in range(self.size):
            for _ in range(math.floor(self.dna[i].fitness)):
                pool.append(self.dna[i].gene)
            parent1 = pool[random.randint(0,len(pool)-1)]
            parent2 = pool[random.randint(0,len(pool)-1)]
            self.dna.append(cross_over(parent1,parent2))

    def cross_over(self, a, b):
        mid = random.randint(1,len(a)-1)
        new_dna = ""
        for i in range(len(a)):
            if i < mid

class dna:


    def __init__(self, user):
        self.size = len(user)
        self.gene = ""
        for i in range(self.size):
            self.gene = self.gene+ self.genes()

        self.fitness = self.fitness_function(user)/float(len(user))

    def genes(self):
        outcomes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
        return outcomes[random.randint(0,len(outcomes)-1)]

    def finess_function(self, user):
        score = 0
        for i in range(user):
            if i == self.gene[i]:
                score+=1
        return score
            

user = input("Enter the phrase to be genetically generated:")

pop = population(user)

while not pop.generated():
    pop.reproduce()

