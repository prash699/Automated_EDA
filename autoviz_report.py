from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()

filename = r'C:\Users\Prashant\Desktop\Visadataset.csv'

report = AV.AutoViz(filename,sep=",",chart_format="html")

