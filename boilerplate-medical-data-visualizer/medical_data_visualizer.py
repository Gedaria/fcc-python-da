import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")


# Add 'overweight' column
def bmi_compute(row):
    height, weight = row["height"], row["weight"]
    bmi = weight / (height / 100) ** 2
    if bmi > 25:
        return 1
    else:
        return 0


df["overweight"] = df.apply(bmi_compute, axis=1)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalize_data(value):
    if value <= 1:
        return 0
    else:
        return 1


df["cholesterol"] = df["cholesterol"].apply(normalize_data)
df["gluc"] = df["gluc"].apply(normalize_data)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"],
    )
    fig = sns.catplot(
        data=df_cat, x="variable", col="cardio", hue="value", kind="count"
    )

    # Do not modify the next two lines
    fig.savefig("catplot.png")
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_filtered = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] < df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] < df["weight"].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_filtered.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    plt.figure()

    # Draw the heatmap with 'sns.heatmap()'
    fig = sns.heatmap(corr, square=True, annot=True, center=0, fmt=".1f", mask=mask)

    # Do not modify the next two lines
    fig.savefig("heatmap.png")
    return fig
