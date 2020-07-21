import pandas as pd
covid = pd.read_csv("covid19_belgium_cases_agesex_region_temperature.csv",encoding="ISO-8859-1")
covid=covid.dropna()
covid.to_csv('covid19.csv', index=False)