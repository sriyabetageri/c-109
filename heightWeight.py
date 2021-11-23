import pandas as pd
import statistics
import csv

df = pd.read_csv("height-weight.csv")
heightList = df["Height(Inches)"].to_list()

weightList = df["Weight(Pounds)"].to_list()