import pandas as pd

details = {

    'Name':['a','b','c','d'],
    'Age':[24,25,26,27],
}

df = pd.DataFrame.from_dict(details)
print(df[:2])