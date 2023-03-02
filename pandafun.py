import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
        "Suite Number": [356, 667, 133],

    }
)

df[(df["Age"] >= 35)]

print(df[(df["Age"] >= 35)])


#df["Age"]
#print(df["Age"])

#print(df)

#print(df["Age"].max())

