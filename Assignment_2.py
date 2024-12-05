#NAME: MOJIBAYO SINDARA DANIEL
#MATRIC NO: RUN/IFT/22/13191

import matplotlib.pyplot as pl
import pandas as pd

data = {
    "Height_Female": [175, 158, 166, 175, 160, 165, 166, 170, 170, 172],
    "Breath_Held_Female": [22.22, 30.57, 17.47, 22.39, 26.90, 36.85, 27.33, 29.55, 13.87, 34.66],
    "Height_Male": [184, 182, 180, 191, 189, 181, 180, 170, 176, 185],
    "Breath_Held_Male": [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27, 59.09, 51.15, 58.32]
}

female_times = data["Breath_Held_Female"]
male_times = data["Breath_Held_Male"]
all_times = female_times + male_times

pl.figure(figsize=(10, 5))
pl.hist(all_times, bins=8, color='skyblue', edgecolor='black')
pl.xlabel('Breath Held Time (s)')
pl.ylabel('Frequency')
pl.title('Histogram of Breath Holding Times')
pl.show()

pl.figure(figsize=(10, 5))
pl.scatter([1]*len(female_times), female_times, color='red', label='Female')
pl.scatter([2]*len(male_times), male_times, color='blue', label='Male')
pl.xticks([1, 2], ['Female', 'Male'])
pl.ylabel('Breath Held Time (s)')
pl.title('Side-by-Side Dot Plot of Breath Holding Times')
pl.legend()
pl.show()
