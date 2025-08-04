import pandas as pd
from DB import LoderData

class Analysis:
    def __init__(self):
        self.data=LoderData()
        self.db=self.data.getData()
    
    def AmountTweets1(self):                 #מחשבת כמה ציוצים אנטישמים
        self.count=self.db[self.db["Biased"]==1]["Biased"].count()
        return self.count
    
    def AmountTweets0(self):                 # מחשבת כמה ציוצים לא אנטישמים
        self.count=self.db[self.db["Biased"]==0]["Biased"].count()
        return self.count
    
    def AllTweets(self):                     # מחשבת את כמות כל הציוצים
        self.alltweets=self.db["Biased"].count()
        return self.alltweets
    
    def Averagelen1(self):                   # מחשבת את הממוצע של המילים באנטישמים
        self.lencount=self.AmountTweets1()
        self.db=self.db.copy()
        self.db["lenge"]=self.db["Text"].str.split().apply(len)
        return self.db["lenge"][self.db["Biased"]==1].sum()/self.lencount
    
    def Averagelen0(self):                   # מחשבת את הממוצע של המילים הלא אנטישמים
        self.lencount=self.AmountTweets0()
        self.db=self.db.copy()
        self.db["lenge"]=self.db["Text"].str.split().apply(len)
        return self.db["lenge"][self.db["Biased"]==0].sum()/self.lencount
    
    def Averagelen(self):                   # מחשבת את הממוצע של המילים כולם
        self.lencount=self.AllTweets()
        self.db=self.db.copy()
        self.db["lenge"]=self.db["Text"].str.split().apply(len)
        return self.db["lenge"].sum()/self.lencount
        
    def ThreeTweets1(self):                 # מחזירה את שלוש הציוצים הכי ארוכים אינטישמים
        self.db=self.db.copy()
        self.db["lenge"]=self.db["Text"].apply(len)
        self.db1=self.db[self.db["Biased"]==1]
        self.db1=self.db1.sort_values(by=['lenge'])
        return self.db1.tail(3)
    
    
    def ThreeTweets0(self):                  # מחזירה את הציוצים הכי ארוכים לא אנטישמים
        self.db=self.db.copy()
        self.db["lenge"]=self.db["Text"].apply(len)
        self.db0=self.db[self.db["Biased"]==0]
        self.db0=self.db0.sort_values(by=['lenge'])
        return self.db0.tail(3)
    
    
    def ThreeTweets(self):                  # מחזירה את שלוש הציוצים הכי ארוכים בהכל
        self.db=self.db.copy()
        self.db["lenge"]=self.db["Text"].apply(len)
        self.db=self.db.sort_values(by=['lenge'])
        return self.db.tail(3)
        

    def TenWord(self):                    # מחזיר את עשר המילים הכי נפוצות
        full_data = ''.join(self.db['Text'].tolist()).lower().split()
        word_counter = pd.Series(full_data).value_counts()
        return {"total": word_counter.head(10).index.to_list()}

        
    
        



        