import pandas as pd

class CheckPath:
    def check(self):
        df = pd.read_csv('../file/All2.csv')
        res = df['path'].iloc[-1]
        return res