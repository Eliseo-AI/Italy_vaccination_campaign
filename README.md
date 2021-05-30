Italy Vaccination Campaign
================
Table of Content
================
  * [Description](#description)
  * [Installation guide](#installation-guide)
  * [Files](#files)
  * [Dataset](#dataset)
  * [Results](#results)
  * [Credits](#credits)
  * [Licensing](#licensing)

## Description
This is a project developed at the [CRI](https://cri-paris.org/en) Université de Paris in the second semester of the Master of Digital Science, within the [Challenge Hub](https://master.cri-paris.org/en/challenge-hub) program.
The project is an analysis of the vaccination campaign against covid-19 in Italy that began in 2020, it is using three different types of vaccines, which need two doses to be effective, also have different times between the first dose and the second, likewise, their availability and quantities are different.
The age groups are eight, the first is made up of young people between 16 and 19 years old, the following groups are for ten years up to 89 years and the last one is ninety years or more.

## Installation guide

If you use conda, you can install: 

   * conda install pandas
   * conda install seaborn
   * conda install numpy

If you use pip, you can install: 

   * pip install pandas
   * pip install seaborn
   * pip install numpy
    
## Files

For this project, one downloaded file was used in the direction given above, 

*Italian vaccine campaign Date (December 27, 2020 to may 25, 2021) https://www.kaggle.com/arthurio/italian-vaccination

## Dataset

the file contains information by groups of vaccinated people grouped by date and company supplier of the vaccine, It does not have individual registers that allow for groupal analysis, for example combining gender and age.

shape (31643, 22)

* Administration date: date of the vaccine administration
* Vaccine supplier: Pfizer, Astrazeneca and Moderna
* Region: abbreviation of the Italian region
* Age range: age group
* Number of males: number of vaccinated males
* Number of females: number of vaccinated females
* Number of healthcare workers: number of vaccinated healthcare workers
* Number of non-healthcare workers: number of vaccinated non-healthcare workers
* Care home patients: number of vaccinated care home patients
* Number of 60-69 people: number of vaccinated people aged 60-69
* Number of 70-79 people: number of vaccinated people aged 70-79
* Number of over 80: number of vaccinated people aged 80+
* Armed forces: number of vaccinated military personnel
* School staff: number of the vaccinated school staff
* Vulnerable subjects: number of vaccinated vulnerable subjects
* Others: number of vaccinated people from other categories
* First dose: number of administered first vaccine doses
* Second dose: number of administered second vaccine doses
* NUTS1 code: European code for major socio-economic regions
* NUTS2 code: European code for basic regions for the application of regional policies
* ISTAT code: region code by Italian National Institute of Statistics
* Region name: full name of Italian regions

## Results
The graphs presented were divided into the first three by the types of vaccines and the following will be comparative in the doses.
![Pfizer](Images/pfizer.png)
- the italian government started the vaccination campaign with Pfizer in December without major differences in age groups. In February, it prioritized the group from 80 to 89 years old with a clear difference. In the evaluated period and without making a difference between the first and second doses, the total of the pfizer vaccine reached a peak of 120,000 doses in one day.

![Astrazeneca](images/astrazeneca.png)
- The italian government began AstraZeneca campaign with very few doses in January and in February, with greater availability, a prioritization of four groups of people began between 20 and 29 years old, between 30 and 39 years old, between 40 and 49 years old, and finally between 50 and 59 years old, until the middle of March, then it prioritized the group of 70 to 79 years. In the evaluated period and without making a difference between the first and second doses, the total of the AstraZeneca vaccine reached a peak of about 50,000 doses in one day.

![Moderna](images/moderna.png)
- the government began Moderna AstraZeneca in January with few doses, since February they prioritized the group of 80 to 89 years and in the middle of March also prioritize the group of 70 to 79 years. In the evaluated period and without making a difference between the first and second doses, the total of the Modern vaccine reaching a peak of about 14,000 doses in one day, this is the vaccine with the least availability and therefore the least application within the population.

![janssen](images/janssen.png)
- the government began Moderna AstraZeneca in January with few doses, since February they prioritized the group of 80 to 89 years and in the middle of March also prioritize the group of 70 to 79 years. In the evaluated period and without making a difference between the first and second doses, the total of the Modern vaccine reaching a peak of about 14,000 doses in one day, this is the vaccine with the least availability and therefore the least application within the population.

<img src="images/first-dose.png" width="750" >
<img src="images/second-dose.png" width="750" >
- In these two graphs you can see the comparison between the two doses of the vaccines, in the case of pfizer the shortage is seen and therefore the decision is made between half of January and the first week of February not to apply more first due to a period in which the second dose is given priority, the case of AstraZeneca shows that it has a period of interruption in the month of March due to the doubts that arose with the vaccine and the application of second doses showing the difference in the times with Regarding the other vaccines, the third is the modern vaccine, this sample that in the second week of March they begin to have greater availability and their application increases both in the first dose and in the second dose at the same time.
  
<img src="images/females.png" width="750" >
<img src="images/males.png" width="750" >  
  
## Discussion


## Credits
The analysis of the dataset was carried out by Eliseo B.
the file is in jupiternotebook format ".pynb"

## Licensing
 MIT License, Eliseo Baquero 2021
