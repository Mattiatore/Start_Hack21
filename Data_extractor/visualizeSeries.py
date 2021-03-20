import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import datetime
from matplotlib import pyplot



#print basic chart
def printChart():
    series = pd.read_csv('/Users/emanuele.cesari/Desktop/Start_Hack21/Data_extractor/66305.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
    series.plot()
    pyplot.show()

printChart()