import plotly.express as px
import csv
import numpy as np

def getData(dataPath):
    icecream = []
    coldrinks = []

    with open(dataPath) as f:
        df = csv.DictReader(f)
        for i in df:
            icecream.append(float(i['Size of TV']))
            coldrinks.append(float(i['\tAverage time spent watching TV in a week (hours)']))

        return {'x': icecream, 'y': coldrinks}

def findCo(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print(correlation[0,1])

def main():
    dataPath = 'tv.csv'
    dataSource = getData(dataPath)
    findCo(dataSource)

main()