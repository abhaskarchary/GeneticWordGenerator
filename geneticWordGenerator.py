import random
import math

population_size = 100
mutation_rate = 0.01
start_gen = 0

class population:


    def __init__(self, user):
        self.generation = start_gen
        self.user = user
        self.size = population_size
        self.dna = []
        self.mutation_rate = mutation_rate
        print("generation",self.generation)
        print()
        for i in range(self.size):
            self.dna.append(dna(user))
            print(self.dna[i].gene,self.dna[i].fitness)
        print()
        print()

    def generated(self):
        for i in range(self.size):
            if self.dna[i].gene == self.user:
                return True
        return False

    def reproduce(self):
        pool = []
        self.generation+=1
        print("generation",self.generation)
        print()
        for i in range(self.size):
            for _ in range(math.floor(self.dna[i].fitness*100)):
                pool.append(self.dna[i].gene)

        
        for i in range(self.size):
            parent1 = pool[random.randint(0,len(pool)-1)]
            parent2 = pool[random.randint(0,len(pool)-1)]
            self.dna[i].alter_dna(self.cross_over(parent1,parent2))
            self.mutate(self.dna[i])
            print(self.dna[i].gene, self.dna[i].fitness)

        print()
        print()

        
    def cross_over(self, a, b):
        mid = random.randint(1,len(a)-1)
        new_dna = ""
        for i in range(len(a)):
            if i < mid:
                new_dna = new_dna + a[i]
            else:
                new_dna = new_dna + b[i]
        return new_dna

    def mutate(self,dna):
        new_gene = ""
        #print(len(dna.gene))
        for i in range(len(dna.gene)):
            if random.random() <= self.mutation_rate:
                new_gene = new_gene + dna.genes()
            else:
                new_gene = new_gene + dna.gene[i]

        dna.gene = new_gene
        
                

class dna:


    def __init__(self, user):
        self.size = len(user)
        self.user = user
        self.gene = ""
        for i in range(self.size):
            self.gene = self.gene+ self.genes()

        self.fitness = self.fitness_function()/float(len(user))

    def genes(self):
        outcomes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
        return outcomes[random.randint(0,len(outcomes)-1)]

    def fitness_function(self):
        score = 0
        for i in range(len(self.user)):
            if self.user[i] == self.gene[i]:
                score+=1
        return score

    def alter_dna(self,new_gene):
        self.gene = new_gene
        self.fitness = self.fitness_function()/float(len(user))
            

user = input("Enter the phrase to be genetically generated:")

pop = population(user)

while not pop.generated():
    pop.reproduce()

