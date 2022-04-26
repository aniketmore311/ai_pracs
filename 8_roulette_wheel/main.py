import random


class RouletteWheel:
    def __init__(self):
        self.fitness_vector = []
        self.cummulative_boundry = []
        self.fractions = []

    def set_fitness_vector(self, fitness_vector):
        self.fitness_vector = fitness_vector
        self.fractions = list()
        totalsum = 0
        current_boundry = 0
        for fitness in fitness_vector:
            totalsum += fitness
        for fitness in fitness_vector:
            current_boundry += fitness/totalsum
            self.cummulative_boundry.append(current_boundry)
            self.fractions.append(fitness / totalsum)
        # print(self.fractions)
        # print(self.cummulative_boundry)

    def spin(self):
        num = random.random()
        index = 0;
        while self.cummulative_boundry[index] < num:
            index += 1
        return self.fitness_vector[index]


def main():
    values = input().split(",")
    fitness_vector = list()
    for value in values:
        fitness_vector.append(int(value))
    rw = RouletteWheel()
    rw.set_fitness_vector(fitness_vector)
    freq = dict()
    for i in range(100):
        winner = rw.spin()
        if winner not in freq:
            freq[winner] = 0
        old_freq = freq[winner]
        freq[winner] = old_freq+1
    for key in freq:
        print(f"{key} won {freq[key]} times")

main()

