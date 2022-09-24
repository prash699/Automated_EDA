import sweetviz as sv
import  pandas

df = pandas.read_csv(r'C:\Users\Prashant\Desktop\Visadataset.csv')

report =sv.analyze(df)
report.show_html('sweetviz_output.html')