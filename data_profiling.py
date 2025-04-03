import pandas as pd
from ydata_profiling import ProfileReport

# Load the dataset
df = pd.read_csv('data.csv')
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("data_profiling.html")
