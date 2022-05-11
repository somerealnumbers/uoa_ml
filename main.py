import pandas as pd
from aitools import understand


def ai(data):
    """ this does ai """

    insight = understand(data)

    return insight

# read data
df = pd.read_csv("data.csv")

# see insight
print(ai(df))
