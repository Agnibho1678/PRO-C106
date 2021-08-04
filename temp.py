import plotly.express as px
import csv

with open("C:/PythonFiles/C106/ice_cream.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Temperature", y="Cold drink sales")
    fig.show()
