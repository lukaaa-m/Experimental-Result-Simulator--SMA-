import pandas as pd #Excel writing and reading package

experiment_count = 1000000 #Number of experimental iterations
experiment_results = [] #List of all experimental results

#Starts with random input, enforces game rules to give final output
for i in range(experiment_count):
    #Do game rule stuff
    result = 0 #Final output after game rule enforcement
    experiment_results.append(result)

#Compiles results into dataframe to be written to Excel spreadsheet
results_dataframe = pd.DataFrame(data=experiment_results, index=None,                               columns="Results", dtype=None, copy=False)

#Write dataframe to excel