import pandas as pd
from DB import LoderData

class clearData:
    def __init__(self):
        self.data=LoderData()
        self.db=self.data.getData()
    def RelevantColumns(self):           # עמודות רלוונטיות
        self.db=self.db.copy()
        self.db=self.db[["Biased","Text"]]
        return self.db

    def RemovingMarks(self):             # מנקה סימנ פיסוק       
        for c in ['.', ',', '!', '?', ';', ':', '"', "'", '(', ')', '-', '_']:
            self.db['Text'] = self.db['Text'].str.replace(c, '')
        return self.db
    def lowerCase(self):                  # ממיר לאותיות קטנות
        self.db['Text'] = self.db['Text'].str.lower()
        return self.db

    def NotClassified(self):               # מסיר לא מסווגים
        self.db=self.db[self.db["Biased"].isin([0,1])]
        return self.db



