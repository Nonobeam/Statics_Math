import pandas as pd
from scipy import stats


df = pd.read_csv("data/lung_cancer.csv")
relevant_years = df.loc[:, '2000':'2019']
countries = ['Vietnam', 'Indonesia', 'China', 'Thailand', 'India']

filtered_df = df[df['country'].isin(countries)]


mean = relevant_years.mean(axis=1)
std_dev = relevant_years.std(axis=1)


n = len(relevant_years.columns)
z_score = stats.norm.ppf(0.975)


margin_of_error = z_score * (std_dev / (n ** 0.5))


lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error


results_df = pd.DataFrame({
    'Country': df['country'],
    'Mean': mean,
    'Lower Bound': lower_bound,
    'Upper Bound': upper_bound
})


selected_results = results_df[results_df['Country'].isin(countries)]
print(selected_results)