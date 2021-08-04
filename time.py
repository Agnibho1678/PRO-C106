import csv
import numpy as np

def getDataSource(data_path):
    size_of_tv = []
    average_time_spent = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            average_time_spent.append(float(row["\tAverage time spent watching TV in a week"]))
        
    return{"x": size_of_tv, "y": average_time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of TV and average time spent watching TV :",correlation[0,1])

def setup():
    data_path = "C:/PythonFiles/C106/television.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()