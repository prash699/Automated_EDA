from pandas_profiling import ProfileReport
import pandas

df = pandas.read_csv(r'C:\Users\Prashant\Desktop\Visadataset.csv')

profile = ProfileReport(df,explorative=True)

profile.to_file('pandas-profiling_output.html')