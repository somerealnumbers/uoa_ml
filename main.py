import pandas as pd
from aitools import understand, get_connection
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
p = result.plot()

# conn
db = get_connection()

# write to database
df.write(db)

p.save("./fig.png")
