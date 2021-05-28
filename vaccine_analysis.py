# for loading json files
import json
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    get_vaccine_data("First")
    get_vaccine_data("Second")

# think about using github large dataset? user can input their country or random
# or overlay some other data
# doesn't start from zero as uk vac programme started on 08 december and started publishing in jan (publish date)
# source : https://coronavirus.data.gov.uk/details/vaccinations

def get_vaccine_data(vac_num):
    file = json.load(open(vac_num + '-vac.json'))
    for item in file["data"]:
        if item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"] is not None:
            print(str(item["date"]) + str(" vaccinated -> ") + str(item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"]) + str(" total -> ") + str(item["cumPeopleVaccinated" + vac_num + "DoseByPublishDate"]))
        elif item["newPeopleVaccinated" + vac_num + "DoseByPublishDate"] is None:
            print(str(item["date"]) + str(" vaccinated -> ") + str("0") + str(" total -> ") + str(item["cumPeopleVaccinated" + vac_num + "DoseByPublishDate"]))

if __name__ == '__main__':
    main()