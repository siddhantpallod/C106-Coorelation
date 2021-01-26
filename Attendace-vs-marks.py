import plotly.express as px
import csv
import numpy as np

def getData(dataPath):
    icecream = []
    coldrinks = []

    with open(dataPath) as f:
        df = csv.DictReader(f)
        for i in df:
            icecream.append(float(i['Days Present']))
            coldrinks.append(float(i['Marks In Percentage']))

        return {'x': icecream, 'y': coldrinks}

def findCo(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print(correlation[0,1])

def main():
    dataPath = 'Attendance.csv'
    dataSource = getData(dataPath)
    findCo(dataSource)

main()