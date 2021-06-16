# for loading json files
import json
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
from datetime import datetime

#To do: rationalise - repeat a lot e.g. pop and reverse

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
        fig, axs = plt.subplots(constrained_layout=True)
        axs.bar(first_keys, first_values, width, label="First Dose")
        axs.bar(first_keys, second_values, width, bottom=first_values, label="Second Dose")
        axs.set_ylabel("Doses (in 1000s)")
        axs.set_title("COVID19 Vaccines given in the UK")
        axs.legend()
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator)
        axs.xaxis.set_major_locator(locator)
        axs.xaxis.set_major_formatter(formatter)
        plt.show()

    else:
        print("Error: dates across files do not match.")


def format_date(str_date):
    date_obj = datetime.strptime(str_date, '%Y-%m-%d')
    date = date_obj.date()
    return date


def get_vaccine_data(vac_num):
    file = json.load(open(vac_num + '-vac.json'))
    new_file = {}
    for item in file["data"]:
        str_date = item["date"]
        date = format_date(str_date)
        if item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"] is not None:
            new_file[date] = int(item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"]) / 1000
        elif item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"] is None:
            new_file[date] = int(0)
    return new_file


if __name__ == '__main__':
    main()