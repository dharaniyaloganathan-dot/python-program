import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Kavin"],
    "Mark": [90, 95, 85]
}

df = pd.DataFrame(data)

print(df[df["Mark"] > 90])

