#!/usr/bin/env python
import random


class Islander(object):
    weight = 1

    def __str__(self):
        return "Mystery Islander"

    def __repr__(self):
        return str(self)

    def __int__(self):
        return self.weight

    def __radd__(self, other):
            return other + self.weight

class OddIslander(Islander):
    def __init__(self):
        self.weight = random.choice([0, 2])



class Game(object):
    '''
    Becuase holts' problem was annoying me, 
    here's a python implementation of it.

    You have tweleve people on an island.
    All weigh exactly the same apart from one of them, who 
    is slightly heavier or lighter than ther others.

    Using a see-saw and three comparisions (< or >) find out which.

    '''
    def __init__(self):
        self.population = [Islander() for x in range(0,11)]
        self.odd_one_out = OddIslander()
        self.population.append(self.odd_one_out)
        random.shuffle(self.population)

    def run_tests_for_weight(self):
        left = self.population[:6]
        right = self.population[6:]
        first_result = sum(left)<sum(right)
        left = self.population[0:3] + self.population[6:9]
        right = self.population[3:6] + self.population[9:12]
        second_result = sum(left)<sum(right)
        if(first_result==second_result):
            equal_group = self.population[3:6] + self.population[6:9]
            unequal_group = self.population[0:3] + self.population[9:12]
        else:
            unequal_group = self.population[3:6] + self.population[6:9]
            equal_group = self.population[0:3] + self.population[9:12]
        if(sum(equal_group) > sum(unequal_group)):
            return "Lighter"
        else:
            return "Heavier"

    def run_quick_search(self):
        left = self.population[:6]
        right = self.population[6:]
        if(sum(left)>sum(right)):
            heavier = left
        else:
            heavier = right
        left = heavier[0:3]
        right = heavier[3:6]
        if(sum(left)>sum(right) or sum(left)<sum(right)):
            return "Heavier"
        else:
            return "Lighter"

    def get_odd_one(self):
        if self.odd_one_out.weight > 1:
            return "Heavier"
        else:
            return "Lighter"


    def print_proof(self):
        print("\n\nProof!\n")
        if self.odd_one_out.weight > 1 :
            print("Odd one out is heavier")
            return
        print("Odd one out is lighter")


def main():
    game = Game()
    for i in range(0,100):
        game = Game()
        if not (game.run_tests_for_weight()==game.get_odd_one()):
            print("INCORRECT")
            return
        if not (game.run_quick_search()==game.get_odd_one()):
            print("INCORRECT")
            return
    


if __name__ == '__main__':
    main()
