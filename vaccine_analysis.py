# for loading json files
import json
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#to do - customising/formatting - smaller label size
#inc manipulate data to make more attractive. divide y / 1000 and add doses in 1000
#change date - 21 May and add 2021 in x label - use a date formatter
#rationalise - repeat a lot e.g. pop and reverse

def main():
    first_vac = get_vaccine_data("First")
    second_vac = get_vaccine_data(("Second"))
    first_keys = list(first_vac.keys())
    second_keys = list(first_vac.keys())
    first_keys.reverse()
    first_keys.pop(0)
    second_keys.reverse()
    second_keys.pop(0)
    if first_keys == second_keys:
        first_values = list(first_vac.values())
        second_values = list(second_vac.values())
        first_values.reverse()
        first_values.pop(0)
        second_values.reverse()
        second_values.pop(0)
        width = 0.35
        fig, ax = plt.subplots()
        ax.bar(first_keys, first_values, width, label="First Dose")
        ax.bar(first_keys, second_values, width, bottom=first_values, label="Second Dose")
        ax.set_ylabel("Doses")
        ax.set_title("COVID19 Vaccines given in the UK")
        plt.xticks(rotation=80)
        ax.legend()
        plt.show()

    else:
        print("Error: dates across files do not match.")

def get_vaccine_data(vac_num):
    file = json.load(open(vac_num + '-vac.json'))
    new_file = {}
    for item in file["data"]:
        if item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"] is not None:
            new_file[item["date"]] = int(item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"])
        elif item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"] is None:
            new_file[item["date"]] = int(0)
    return new_file

if __name__ == '__main__':
    main()