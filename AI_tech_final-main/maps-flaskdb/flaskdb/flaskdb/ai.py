import sys
import random
import math
import copy

class GA():
    points = []

    POPULATION_SIZE = 10    # 集団の個体数
    GENERATION = 10         # 世代数
    MUTATE = 0.1            # 突然変異の確率
    SELECT_RATE = 0.5       # 選択割合

    def __init__(self, POPULATION_SIZE=10, GENERATION=10, MUTATE=0.1, SELECT_RATE=0.5):
        self.POPULATION_SIZE = 10
        self.GENERATION = 10
        self.MUTATE = 0.1
        self.SELECT_RATE = 0.5

    def calc_distance(self, points, route):
        distance = 0
        for i in range(len(points)):
            (x0, y0) = points[route[i]]
            if i == len(points) - 1:
                (x1, y1) = points[route[0]]    
            else:
                (x1, y1) = points[route[i + 1]]
            #distance = distance + math.sqrt((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1))
            distance = distance + self.gis_distance(x0, y0, x1, y1)
        return distance

    def gis_distance(self, lat1, lng1, lat2, lng2):
        R = 6378.137
        x1 = R * math.cos(math.pi * lat1 / 180) * math.cos(math.pi * lng1 / 180)
        y1 = R * math.cos(math.pi * lat1 / 180) * math.sin(math.pi * lng1 / 180)
        z1 = R * math.sin(math.pi * lat1 / 180)
        x2 = R * math.cos(math.pi * lat2 / 180) * math.cos(math.pi * lng2 / 180)
        y2 = R * math.cos(math.pi * lat2 / 180) * math.sin(math.pi * lng2 / 180)
        z2 = R * math.sin(math.pi * lat2 / 180)
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        return 2 * R * math.asin( d / 2 / R )

    def sort_fitness(self, points, population):
        fp = []
        for individual in population:
            fitness = self.calc_distance(points, individual)
            fp.append((fitness, individual))
        fp.sort()

        sorted_population = []    
        
        for fitness, individual in fp:
            sorted_population.append(individual)
            
        return sorted_population

    def selection(self, points, population):
        sorted_population = self.sort_fitness(points, population)
        n = int(self.POPULATION_SIZE * self.SELECT_RATE)    
        
        return sorted_population[0:n]

    def crossover(self, ind1, ind2):
        r1 = random.randint(0, len(self.points) - 1)
        r2 = random.randint(r1 + 1, len(self.points))

        flag = [0] * len(self.points)
        ind = [-1] * len(self.points)
        
        for i in range(r1, r2):
            city = ind2[i]
            ind[i] = city
            flag[city] = 1
        
        for i in list(range(0, r1)) + list(range(r2, len(self.points))):
            city = ind1[i]
            if flag[city] == 0:
                ind[i] = city
                flag[city] = 1
                
        for i in range(0, len(self.points)):
            if ind[i] == -1:
                for j in range(0, len(self.points)):
                    city = ind1[j]
                    if flag[city] == 0:
                        ind[i] = city
                        flag[city] = 1
                        break
        return ind

    def mutation(self, ind1):
        ind2 = copy.deepcopy(ind1)
        if random.random() < self.MUTATE:
            city1 = random.randint(0, len(self.points) - 1)
            city2 = random.randint(0, len(self.points) - 1)
            if city1 > city2:
                city1, city2 = city2, city1
            ind2[city1:city2+1] = reversed(ind1[city1:city2+1])
        return ind2

    def compute(self, spot_list):
        self.points.clear()
        for spot in spot_list:
            self.points.append((spot.latitude, spot.longitude))

        population = []
        for i in range(self.POPULATION_SIZE):
            individual = list(range(len(self.points)))

            random.shuffle(individual)
            population.append(individual)

        print(population)
        
        for generation in range(self.GENERATION):
            print(u"tsp_ga (" + str(generation + 1) + u"generation)")
            
            population = self.selection(self.points, population)
            
            n = self.POPULATION_SIZE - len(population)    
            for i in range(n):
                r1 = random.randint(0, len(population) - 1)
                r2 = random.randint(0, len(population) - 1)
                individual = self.crossover(population[r1], population[r2])
        
                individual = self.mutation(individual)
        
                population.append(individual)
        
            self.sort_fitness(self.points, population)
            
            for ind in range(self.POPULATION_SIZE):
                route = population[ind]
                dist = self.calc_distance(self.points, route)
                
                print(route, dist)
                
                for i in range(len(self.points)):
                    (x0, y0) = self.points[route[i]]
                    if i == len(self.points) - 1:
                        (x1, y1) = self.points[route[0]]
                    else:
                        (x1, y1) = self.points[route[i+1]]

        return route, dist
