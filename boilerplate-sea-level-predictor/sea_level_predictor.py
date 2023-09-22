import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    line1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    df_range = range(1880, 2051)
    plt.plot(df_range, line1.slope * df_range + line1.intercept)

    # Create second line of best fit
    df_2000up = df[df["Year"] >= 2000]
    line2 = linregress(df_2000up["Year"], df_2000up["CSIRO Adjusted Sea Level"])
    df_2000up_range = range(2000, 2051)
    plt.plot(df_2000up_range, line2.slope * df_2000up_range + line2.intercept)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
