import pyodbc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Set up the connection parameters
server = 'localhost'   # Assuming SQL Server is installed locally
database = 'HousingDB'
username = 'sa'
password = '123'

# Create the connection string
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connect to the database
conn = pyodbc.connect(conn_str)

# Execute a SQL query to fetch the housing prices
sql_query = "SELECT price FROM housing"
prices = pd.read_sql(sql_query, conn)['price']

# Close the connection
conn.close()

# Perform hypothesis testing and construct a confidence interval
population_mean = 500000
alpha = 0.05  # Significance level

# Perform one-sample t-test
t_statistic, p_value = stats.ttest_1samp(prices, population_mean)

# Calculate the sample mean and standard deviation
sample_mean = np.mean(prices)
sample_std = np.std(prices, ddof=1)  # ddof=1 for sample standard deviation

# Calculate the margin of error
critical_value = stats.t.ppf(1 - alpha/2, len(prices) - 1)  # Two-tailed test
margin_of_error = critical_value * (sample_std / np.sqrt(len(prices)))

# Calculate the confidence interval
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Plot a histogram of housing prices
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(sample_mean, color='red', linestyle='--', linewidth=2, label='Sample Mean')
plt.xlabel('Housing Price ($)')
plt.ylabel('Frequency')
plt.title('Histogram of Housing Prices')
plt.legend()

# Display the results below the graph
plt.text(0.02, -0.5, f"Sample Mean: ${sample_mean:.2f}\n"
                     f"Margin of Error: ${margin_of_error:.2f}\n"
                     f"Confidence Interval: (${confidence_interval[0]:.2f}, ${confidence_interval[1]:.2f})\n"
                     f"t-statistic: {t_statistic:.2f}\n"
                     f"p-value: {p_value:.5f}",
         fontsize=12, transform=plt.gca().transAxes)

# Show the plot
plt.tight_layout()
plt.show()
