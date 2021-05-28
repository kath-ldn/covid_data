# for loading json files
import json
import seaborn as sns
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    first_vac = pd.read_csv("First_vac.csv")
    sns.set_theme(style="ticks", color_codes=True)
    sns.catplot(x="date", y="newPeopleVaccinatedFirstDoseByPublishDate",
                kind="bar",
                data=first_vac)
    plt.show()

if __name__ == '__main__':
    main()