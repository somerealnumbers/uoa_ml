import pandas as pd
from aitools import understand
from datetime import datetime


def ai(data):
    """ this does ai """

    insight = understand(data)

    return insight

# read data
df = pd.read_csv("data.csv")

# time stamp
df["TimeStamp"] = datetime.now()

# see insight
result = ai(df)

# plot the insight
result.plot()
