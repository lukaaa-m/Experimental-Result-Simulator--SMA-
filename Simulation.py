import pandas as pd,math,random,numpy as np

#Debug variables
common_repeats_results = [] #List of common repeats
lone_repeats_results = [] #List of lone repeats

#Experimental variables
experiment_count = 10 #Number of experimental iterations
digits = 3
total_digit_sums = 9 * digits

#Table variables
column_names = [["Common Repeats", "Lone Repeats"]] #List of column names
result_pairs = []

#Generates random list of numbers to be used for the number count
num_count = np.random.randint(728, size=experiment_count)

#Main loop, generates results
for i in range(experiment_count):

    #Calculates common repeats by finding lowest common factor then rounding down, then calculates the remainder, giving the number of lone repeats
    common_repeats = math.floor(num_count[i] / total_digit_sums)
    lone_repeats = num_count[i] % total_digit_sums

    #Adds results to appropriate lists for debug purposes
    common_repeats_results.append(common_repeats)
    lone_repeats_results.append(lone_repeats)

    #Pairs common- and lone- repeats for tabling
    result_pairs.append([common_repeats,lone_repeats])

#Prints number of experiments (FOR DEBUG, FINDING MAX EXPERIMENTS)
print("Finished generating with *",str(len(common_repeats_results)),"* results.","\n...")

#Combines pairings and column names
result_table = np.concatenate((column_names,result_pairs))

#Compiles results into dataframe to be written to Excel spreadsheet
results_dataframe = pd.DataFrame(data=result_table[1:,0:], index = None, columns=result_table[0,0:])

print ("DATAFRAME/TABLE OF RESULTS:\n",results_dataframe,"\n...")

#Writes dataframe to excel
results_dataframe.to_excel("Experimental Results Table.xlsx")
print("Finished writing to excel")

# This program is based on the pigeonhole theorem, which says that if there are "n" slots/types/options, and there are n+1 objects, then there are two objects in at least one of the "n" slots. It applies this theory to digital sums (the sum of the individual digits of a number). There are 27 possible digital sums (excluding repeats) in a three digit number, where the digit can be anything between 1 and 9 (because 9+9+9). Because there are 27 possible digital sums, given a set of 28 three digit numbers, at least two of those numbers will share the same digital sum. If there are 54 numbers, then every digital sum could be repeated twice. This program returns the amount of times *every* digital sum could be repeated, as well as the number of digital sums that could be repeated more than the others. These are referred to as common- and lone- repeats in the program. For example, given 91 three digit numbers, there are 3 common-repeats and 10 lone-repeats, because 91 = 27 * 3 + 10.