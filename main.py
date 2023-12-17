import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
anime = pd.read_csv("anime.csv")

print(anime)
print(f"anime.ndim = {anime.ndim}")
print(anime.columns)
print(anime["Episodes"].unique())
print(anime.sort_values(by='Episodes'))