# Code in Place Final Project: COVID19 Data Analysis

## About

This is my final project for the Stanford Code In Place Python course! I am exploring data science because this isn't 
something I hadn't previously done as much of. I had mainly been working with JavaScript/the front end prior to this course.

This program analyses how many first and second dose COVID19 vaccines have been given. This could be expanded to other
countries/global vaccines, with the right data.

### Demo

![Screenshot of Bar Chart showing COVID19 data](./screenshot-17-Jun.png?raw=true)

### Built with

* Python
* MatPlotLib

## Prerequisites & Installation

* the latest version of python (3.9)
* MatPlotLib (and dependency packages)
* I used a Conda environment, but this is optional

## Usage

Load the project in your IDE(I used PyCharm) and run to see the data.

## Licence

Program distributed under the [MIT](https://choosealicense.com/licenses/mit/) licence.

All data is property of the UK government and available at https://coronavirus.data.gov.uk/details/vaccinations.

## Contact
Kath Turner - @kath_ldn - katharineturner3@gmail.com

### Known Issues

* The data doesn't start from zero because although the UK vaccination programme started on 08 December 2020,
  publication of the data started in January 2021. The data shows the number of vaccines by publication date,
  not by date they are given. Therefore it may not precisely reflect numbers given on each day.
* I have not tested how the program would run if data was incomplete, and the dates on each did not match each other.
  This would likely require additional code to work.

## Acknowledgements

* Miniconda
* MatPlotLib
* UK Government for the data


