import pandas as pd


class LoderData:
    def __init__(self):
        self.db=pd.read_csv(r"C:\Users\IMOE001\Desktop\Twitter\Data\tweets_dataset.csv")
    def getData(self):
        return self.db
    
