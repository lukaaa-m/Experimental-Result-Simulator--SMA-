import math, random as rand, numpy as np

experiment_iterations = 10000000
results = []

win_cond_1 = 0
win_cond_2 = 0
win_cond_3 = 0
win_cond_4 = 0
win_cond_5 = 0
win_cond_6 = 0

conditions = [win_cond_1,win_cond_2,win_cond_3,win_cond_4,win_cond_5,win_cond_6]

second_draw_set = [x for x in range(0,24)]
second_draw_set.append(25)

primes = [2,3,5,7,11,13,17,19,23]
def checkPrime(x):
    if x in primes:
        return True
    else:
        return False


def checkConditions(x,y):
    global conditions
    global second_draw_set
    #Condition 1: both draws are divisible by 5
    if x != 0 and x % 5 == 0 and y != 0 and y % 5 == 0:
        conditions[0] += 1
        return

    #Condition 2: draws are 0 and 26
    if abs(x-y) == 26:
        conditions[1] += 1
        return

    #Condition 3: draws are consecutive
    if y-x == 1:
        conditions[2] += 1
        return

    #Condition 4: two even draws, then 2 prime draws
    if not (abs(x-y) == 26) and (x % 2 == 0 and y % 2 == 0):
        second_draw_1 = second_draw_set[rand.randint(0,24)]
        second_draw_2 = second_draw_set[rand.randint(0,24)]
        while second_draw_2 == second_draw_1:
            second_draw_2 = second_draw_set[rand.randint(0,24)]

        if checkPrime(second_draw_1) and checkPrime(second_draw_2):
            conditions[3] += 1
            return

    #Condition 5: one draw is even and other is odd
    if (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
        conditions[4] += 1
        return
        
    #Condition 6: both are odd
    if x != 0 and x % 2 == 1 and y % 2 == 1:
        conditions[5] += 1
        return


    
    
def genResult():
    global results
    #Generates random draws
    draw_1 = rand.randint(0,26)
    draw_2 = rand.randint(0,26)
    #Precludes draws
    while draw_2 == draw_1:
        draw_2 = rand.randint(0,26)

    #Adds results to 2D array
    results.append([draw_1,draw_2])
    #Checks for winning conditions
    checkConditions(draw_1,draw_2)

#Iterates experiment
for i in range(experiment_iterations):
    genResult()

j = 1
for i in conditions:
    print("Condition", j,"=", i,"|", i /experiment_iterations * 100)
    j += 1