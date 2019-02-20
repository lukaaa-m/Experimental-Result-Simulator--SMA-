import pandas as pd,math,random

experiment_count = 5 #Number of experimental iterations
common_repeats_results = [] #List of common repeats
lone_repeats_results = [] #List of maximum lone repeats
digits = 3
total_digit_sums = 9 * digits

#Starts with random input, enforces game rules to give final output
for i in range(experiment_count):
    num_count = random.randint(1,161)

    common_repeats = math.floor(num_count / total_digit_sums)
    lone_repeats = num_count % total_digit_sums

    common_repeats_results.append(common_repeats)
    lone_repeats_results.append(lone_repeats)

    print("Numbers =", num_count)
    print (common_repeats_results[i], ":", lone_repeats_results[i])


#Compiles results into two-column dataframe to be written to Excel spreadsheet
########

#Write dataframe to excel
########


# This program is based on the pigeonhole theorem, which says that if there are "n" slots/types/options, and there are n+1 objects, then there are two objects in at least one of the "n" slots. It applies this theory to digital sums (the sum of the individual digits of a number). There are 27 possible digital sums (excluding repeats) in a three digit number, where the digit can be anything between 1 and 9 (because 9+9+9). Because there are 27 possible digital sums, given a set of 28 three digit numbers, at least two of those numbers will share the same digital sum. If there are 54 numbers, then every digital sum could be repeated twice. This program returns the amount of times *every* digital sum could be repeated, as well as the number of digital sums that could be repeated more than the others. These are referred to as common- and lone- repeats in the program. For example, given 91 three digit numbers, there are 3 common-repeats and 10 lone-repeats, because 91 = 27 * 3 + 10.