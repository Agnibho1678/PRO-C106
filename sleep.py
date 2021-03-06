import plotly.express as px
import csv

with open("C:/PythonFiles/C106/coffee.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Coffee in ml", y="sleep in hours", color = "week")
    fig.show()

