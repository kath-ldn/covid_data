# Imports required libraries
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from datetime import datetime

# Constants to hold API urls
FIRST_VAC_API = requests.get(str("https://coronavirus.data.gov.uk/api/v1/data?filters=areaType=overview&structure=%7B"
                                 "%22areaType%22:%22areaType%22,%22areaName%22:%22areaName%22,"
                                 "%22areaCode%22:%22areaCode%22,%22date%22:%22date%22,"
                                 "%22newPeopleVaccinatedFirstDoseByPublishDate%22"
                                 ":%22newPeopleVaccinatedFirstDoseByPublishDate%22,"
                                 "%22cumPeopleVaccinatedFirstDoseByPublishDate%22"
                                 ":%22cumPeopleVaccinatedFirstDoseByPublishDate%22%7D&format=json"))
SECOND_VAC_API = requests.get(str("https://coronavirus.data.gov.uk/api/v1/data?filters=areaType=overview&structure"
                                  "=%7B%22areaType%22:%22areaType%22,%22areaName%22:%22areaName%22,"
                                  "%22areaCode%22:%22areaCode%22,%22date%22:%22date%22,"
                                  "%22newPeopleVaccinatedSecondDoseByPublishDate%22"
                                  ":%22newPeopleVaccinatedSecondDoseByPublishDate%22,"
                                  "%22cumPeopleVaccinatedSecondDoseByPublishDate%22"
                                  ":%22cumPeopleVaccinatedSecondDoseByPublishDate%22%7D&format=json"))


# Main function gets data then draws a stacked bar chart
def main():
    vac_dates, first_vac_num, second_vac_num = get_data()
    draw_chart(vac_dates, first_vac_num, second_vac_num)


# Gets data from API and returns it as three lists - dates, numbers of first doses and numbers of second doses
def get_data():
    first_vac = format_api_data((FIRST_VAC_API.json()), "First")
    second_vac = format_api_data((SECOND_VAC_API.json()), "Second")
    vac_dates = list(first_vac.keys())
    first_vac_num = list(first_vac.values())
    second_vac_num = list(second_vac.values())
    return vac_dates, first_vac_num, second_vac_num


# Draws chart using matplotlib
def draw_chart(vac_dates, first_vac_num, second_vac_num):
    # sets width of bars
    width = 0.6
    # creates chart fig/axes using mpl, then adds data and labels chart
    fig, axs = plt.subplots()
    axs.bar(vac_dates, first_vac_num, width, label="First Dose")
    axs.bar(vac_dates, second_vac_num, width, bottom=first_vac_num, label="Second Dose")
    axs.set_ylabel("Doses (in 1000s)")
    axs.set_title("Number of People Vaccinated Against COVID19 In The UK")
    axs.legend()
    # Formats date ticks along x axis in concise/readable way using mpl ConciseDateFormatter
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    axs.xaxis.set_major_locator(locator)
    axs.xaxis.set_major_formatter(formatter)
    # Shows chart
    plt.show()


def change_date_type(str_date):
    date_obj = datetime.strptime(str_date, '%Y-%m-%d')
    date = date_obj.date()
    return date


def format_api_data(file, vac_num):
    new_file = {}
    for item in file["data"]:
        str_date = item["date"]
        date = change_date_type(str_date)
        if item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"] is not None:
            new_file[date] = int(item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"]) / 1000
        elif item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"] is None:
            new_file[date] = int(0)
    return new_file


if __name__ == '__main__':
    main()