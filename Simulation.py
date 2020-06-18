import pandas as pd,math,random,numpy as np
import csv

#Debug variables
common_repeats_results = [] #List of common repeats
lone_repeats_results = [] #List of lone repeats

#Experimental variables
experiment_count = 10000 #Number of experimental iterations
digits = 3
total_digit_sums = 9 * digits

#Table variables
column_names = [["Common Repeats", "Lone Repeats","Outcome Count", "Outcome Probability"]] #List of column names
results = []

#Winning outcome variables
win_cond_1 = 0 #Both outputs divisible by 5
win_cond_2 = 0 #Both equal to 0
win_cond_3 = 0 #Consecutive values
win_cond_4 = 0 #Both even then both prime

conditions = [win_cond_1,win_cond_2,win_cond_3, win_cond_4]

def checkPrime(x):
    if x >= 2:
        for y in range(2,x):
            if not (x % y):
                return False
    else:
	    return False
    return True

def checkWin(x,y):
    global conditions
    #Condition 1 - both outputs are divisible by 5
    if x != 0 and x % 5 == 0 and y != 0 and y % 5 == 0:
        conditions[0] += 1
    #Condition 2 - both outputs are equal to 0
    if x == 0 and y == 0:
        conditions[1] += 1
    #Condition 3 - outputs are consecutive (e.g. [5,6])
    if y - x == 1:
        conditions[2] += 1
    #Condition 3 - one set of outputs are both even, next two are both prime
    if len(results) > 1 and results[-1][0] % 2 == 0 and results[-1][1] % 2 == 0:
        if checkPrime(x) and checkPrime(y):
            conditions[3] += 1

#Generates random list of numbers to be used for the number count
num_count = np.random.randint(728, size=experiment_count)

#Main loop, generates results
for i in range(experiment_count):

    #Calculates common repeats by dividing by 27 then rounding down, then calculates the remainder, giving the number of lone repeats
    common_repeats = math.floor(num_count[i] / total_digit_sums)
    lone_repeats = num_count[i] % total_digit_sums

    #Adds results to appropriate lists for debug purposes
    common_repeats_results.append(common_repeats)
    lone_repeats_results.append(lone_repeats)

    #Checks for winning conditions
    checkWin(common_repeats,lone_repeats)

    #Pairs common- and lone- repeats for tabling
    results.append([common_repeats,lone_repeats,None,None])

#Prints number of experiments (FOR DEBUG, FINDING MAX EXPERIMENTS)
print("Finished generating with *",str(len(common_repeats_results)),"* results.","\n...")

#Combines condition results and condition probability
for i in range(len(conditions)):
    results[i][2] = conditions[i]
    results[i][3] = conditions[i] / experiment_count * 100
    print("Condition",str(i+1), "=", str(results[i][2]),"|",str(results[i][3]) + "%")
#Combines pairings and column names
result_table = np.concatenate((column_names,results))

with open('Experiment.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(result_table)
csvFile.close()

print("Finished writing to csv file.")

# print ("DATAFRAME/TABLE OF RESULTS:\n",results_dataframe,"\n...")

#Writes dataframe to excel
# results_dataframe.to_excel("Experimental Results Table.xlsx")
# print("Finished writing to excel")

# This program is based on the pigeonhole theorem, which says that if there are "n" slots/types/options, and there are n+1 objects, then there are two objects in at least one of the "n" slots. It applies this theory to digital sums (the sum of the individual digits of a number). There are 27 possible digital sums (excluding repeats) in a three digit number (because 9+9+9), where each digit can be anything between 1 and 9. Because there are 27 possible digital sums, given a set of 28 three digit numbers, at least two of those numbers will share the same digital sum. If there are 54 numbers, then every digital sum could be repeated twice. This program returns the amount of times *every* digital sum could be repeated, as well as the number of digital sums that could be repeated more than the others. These are referred to as common- and lone- repeats in the program. For example, given 91 three digit numbers, there are 3 common-repeats and 10 lone-repeats, because 91 = 27 * 3 + 10.