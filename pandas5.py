import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Arun", "Priya", "Kavin"],
    "Mark": [90, 95, 85]
}

df = pd.DataFrame(data)

plt.bar(df["Name"], df["Mark"])

plt.xlabel("Students")
plt.ylabel("Marks")

plt.title("Student Performance")

plt.show()

