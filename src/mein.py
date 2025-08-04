import pandas as pd
from DataClear import clearData
from DataAnalysis import Analysis


class mein:
    def __init__(self):
        self.db=clearData()
        self.data=self.db.RelevantColumns()
        self.data=self.db.RemovingMarks()
        self.data=self.db.lowerCase()
        self.data=self.db.NotClassified()
        self.data.to_csv(r"C:\Users\IMOE001\Desktop\Twitter\results\tweets_dataset_cleaned.csv")


data=mein()