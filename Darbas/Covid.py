import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")

# -----------------------------------------------------------------------
# datasetas didelis [104116 rows x 60 columns] todel, atsirenku tik man aktualia info i nauja df "newdf":
# -----------------------------------------------------------------------
# newdf = df[['continent', 'location', 'date', 'total_cases', 'new_cases', 'new_cases_smoothed', 'total_deaths',
#             'new_deaths', 'total_cases_per_million', 'new_cases_per_million',
#             'total_deaths_per_million', 'new_deaths_per_million',
#             'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'new_vaccinations',
#             'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
#             'people_fully_vaccinated_per_hundred', 'population', 'median_age', 'gdp_per_capita',
#             'extreme_poverty', 'female_smokers', 'male_smokers', 'handwashing_facilities',
#             'life_expectancy', 'human_development_index']]

# -----------------------------------------------------------------------
# issifiltruoju tik viso pasaulio agreguotus duomenis)
# -----------------------------------------------------------------------
df.set_index('location', inplace=True)
world_stat = df.loc[['World'], ['date', 'total_cases', 'new_cases','new_cases_smoothed', 'people_vaccinated',
                                'people_fully_vaccinated', 'population', 'median_age', 'gdp_per_capita',
                                'total_deaths', 'extreme_poverty', 'female_smokers', 'male_smokers', 'handwashing_facilities',
                                'life_expectancy', 'human_development_index']]

start_date = world_stat.iloc[world_stat['new_cases'].argmin(),0]
start_cases = world_stat.iloc[world_stat['new_cases'].argmin(),1]
last = world_stat.date.tail(1).iloc[0]

print(f"\nCOVID STATISTICS\n\nConsiders all countries` data starting {start_date}, " \
          f"when the first {start_cases} cases were registered, until {last}.\n")

peak_date = df.iloc[df['new_cases'].argmax(), 2]
peak_newcases = df.iloc[df['new_cases'].argmax(), 4]

print(f"{'-'*150}\nCovid-19 peak: {peak_date} - new cases per day at {int(peak_newcases/1000)} thousands.\n")

world_stat['date'] = pd.to_datetime(world_stat['date'])
plt.rcParams.update({'font.size':8})
plt.plot(world_stat.date, ((world_stat.new_cases)/1000), c="c", label = "line 1")
plt.plot(world_stat.date, ((world_stat.new_cases_smoothed)/1000), c="r", label = "line 2")
plt.title('Covid-19 dynamics')
plt.xlabel('Data')
plt.xticks(rotation=45)
plt.ylabel('New cases in (thousands)')
plt.show()



