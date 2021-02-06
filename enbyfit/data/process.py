import pandas as pd


DF = pd.read_csv('food.csv')


class Query:
    def __init__(self, query):
        self.query = query.upper()

        ids = []

        for id, data in enumerate(DF['Category']):
            if data == self.query:
                ids.append(id)

        print(DF.loc[ids])




if __name__ == '__main__':
    query = Query('cheese')
