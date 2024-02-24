import csv
import math
# import numpy as np
# import pandas as pd
import scipy.stats as st
# import matplotlib.pyplot as plt

# Define the column index for age
age_column = 2

# Define the total population of the dataset
population = 1000

# Calculate sum of any column you want; just put in the parameter the name of the column
def sumOfCol(column_index):
    with open("../data/dataset.csv", 'r') as fin:
        headerline = next(fin)
        total = 0
        for row in csv.reader(fin):
            total += int(row[column_index])
    return total

# Calculate the mean of the population
def mean(column_index, pop):
    return sumOfCol(column_index) / pop

# Calculate the variance of the population
def variance(column_index, pop):
    mean_val = mean(column_index, pop)
    with open("../data/dataset.csv", 'r') as fin:
        headerline = next(fin)
        va = 0
        for row in csv.reader(fin):
            va += (int(row[column_index]) - mean_val) ** 2
    return va / (pop - 1)

def standardDeviation(column_index, pop):
    variance_value = variance(column_index, pop)
    return math.sqrt(variance_value)

# Calculate one half of Z Score value, due to right Z Score value = (-left Z Score value)
def zScoreInHalf(CI_value):
    prop = (1 - CI_value) / 2
    zScore = st.norm.ppf(prop)
    return abs(zScore)


# Calculate the Confidenece Interval
# This CI only calculate with the sample of 1000. If u w
def confidenceInterval(column_index, pop, ci_value):
    leftScore = mean(column_index, pop) - standardDeviation(column_index, pop) * zScoreInHalf(ci_value)
    rightScore = mean(column_index, pop) + standardDeviation(column_index, pop) * zScoreInHalf(ci_value)

    return f"{leftScore} <= μ <= {rightScore}"

print("Means of Population = ", mean(age_column, population))
print("Variance of Population = ", variance(age_column, population))
print("Standard Deviation of Population = ", standardDeviation(age_column, population))
print("Z Score with 95% CI = ", zScoreInHalf(0.95))
print("95% Confidence Interval of mean population: ", confidenceInterval(age_column, population, 0.95))