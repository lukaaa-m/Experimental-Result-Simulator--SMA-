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