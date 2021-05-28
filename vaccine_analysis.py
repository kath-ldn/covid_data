# for loading json files
import json
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    first_vac = get_vaccine_data("First")
    keys = first_vac.keys()
    values = first_vac.values()
    print(keys, values)
    plt.bar(keys, values)
    plt.title = "First Vaccine Doses"
    plt.xlabel = "Date"
    plt.xticks(rotation=80)
    plt.ylabel = "Vaccines"
    plt.show()

    """
    first_vaccine = pd.read_json("First-vac.json")
    sns.relplot(first_vaccine, x="1", y="2", hue="data", kind="line")
    """

def get_vaccine_data(vac_num):
    file = json.load(open(vac_num + '-vac.json'))
    new_file = {}
    for item in file["data"]:
        if item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"] is not None:
            new_file[item["date"]] = int(item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"])
            # print(str(item["date"]) + str(" vaccinated -> ") + str(item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"]) + str(" total -> ") + str(item["cumPeopleVaccinated" + vac_num + "DoseByPublishDate"]))
        elif item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"] is None:
            new_file[item["date"]] = int(0)
            # print(str(item["date"]) + str(" vaccinated -> ") + str("0") + str(" total -> ") + str(item["cumPeopleVaccinated" + vac_num + "DoseByPublishDate"]))
    return new_file

if __name__ == '__main__':
    main()