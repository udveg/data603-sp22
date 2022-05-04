# Chicago crime dataset analysis 
This Notebook contains Chicago crime data analysis for the last ten years (2011-2021) <br>
The dataset was collected from the ‘city of chicago’ official website which has many public datasets.<br>

## Dataset Description
For this particular project I have used three datasets ,the first dataset is the actual crime dataset which contains information about the crime that is time, location, category and primary type. The second dataframe is about the districts in chicago which contains district name and chicago district number which I will further use for getting an comprehensive idea about the crimes in chicago based on different districts. The dataset consists of 22 columns and 7.5 Million rows (dataset size 1.78GB). The dataset has information about the reported crimes from 2001 in the city of chicago except for the murders. The third dataset is about the community area names and their respective codes. Further I will discuss how I used these datasets for analysis. 

* The dataset about the crime and IUCR can be found in the Chicago's official [website.](https://data.cityofchicago.org/Public-Safety/Crimes-One-year-prior-to-present/x2n5-8w5q)
* The dataset which had information about disricts was also from the same portal. 

<p align="center">
<img width="760" height="450" src="https://user-images.githubusercontent.com/89949851/166584816-d4de5cb1-e21a-4233-ae02-d91e825e7fb9.jpeg">
</p>

--- 

<br>

The aim of the project is to find out the crimes that occurred more often, the crime rate trend across the years, and during which month and hour of the day the crime rate was highest. Using the second dataset, I want to get the district name and join the two dataframes so that we can evaluate the crimes based on district. Initally, the dataset had many null values and even the schema was not properly defined, so I had to perform EDA before I did any transformation on the data. Spark doesn't have any built-in libraries for plotting, so I will use matplotlib to plot and I will also use SQL functions to work with the dataframe.

---

### How to run the notebook:
To run the notebook, we must have SQL functions, matplotlib, and other basic libraries installed, as mentioned in the notebook. The whole code needs to be run step by step from the beginning, and the environment should have all the two datasets attached.  

## Step-1 (Exploring and Cleaning Data) 
For the exploration, I started with defining the schema and then dropping all the columns which were unecessary, the dataset consisted of 22 columns and 7.4 million rows, but for this particular analysis I considered only last ten years data so I have trimmed the data according to year. Moreover, the data had many null values which had to be removed. To begin the process of cleaning my data in preparation for analysis, I wanted to check to see whether I had any nulls. I began by determining which columns had null values. Several did, including the following: Location Description, District, Community Area, X and Y coordinates, and both Latitude and Longitude. I removed them and also there where certain records which looked non relatable for example some crimes where described as "NON-CRIMINAL" I removed all of them using 'filter' function. These are some of the columns that are used in analyzing. <br>

<b>Date</b>           -      Date on which crime occured. <br>
<b>Primary Type</b>   -      Primary type of crime. <br>
<b>IUCR</b>           -      Four digit Illinois Uniform Crime Reporting (IUCR) codes <br>
<b>Description</b>    -      Short description of the type of crime <br>
<b>Location description</b> - Description of where crime occured<br>
<b>District</b>       -     District code where crime occured <br>
<b>Community</b>      -     Community area code where crime occured <br>
<b>Longitude & Latitude</b>     -     Exact coordinates of crime occurance<br>
<b>FBI Code</b>      -    numeric code indicating FBI crime categorization<br>
<b>Year</b>          -    Year of crime <br>
<b>Arrest</b>         -     Indicates whether arrest was made or not<br>

<img width="1060" alt="Screen Shot 2022-05-03 at 10 10 59 PM" src="https://user-images.githubusercontent.com/89949851/166614641-160a6352-bfaf-44ae-8ed3-86bd070c8cec.png">



---

## Step-2 (Checking relevant data for analyzing)
For further process firstly I removed all the crime types that are not relevant or not significant crimes then merged the similar looking crimes; the  crime type that had multiple records which had similar meaning for example:-

<img width="1078" alt="Screen Shot 2022-05-03 at 10 07 14 PM" src="https://user-images.githubusercontent.com/89949851/166614510-816cf6a9-8ae2-48f0-ae93-beef13c7e327.png">

<br>

To be able to analyze by date, I wanted to change the date column to DateTimeIndex. 

```
dataset = dataset.withColumn('datetime', to_timestamp('Date', 'MM/dd/yyyy hh:mm:ss a'))
```

<br>

## Step-3 (Analysis)

After thoroughly examining the entire dataset, I determined that I wanted to examine the relationship between various variables and the arrest rate. Although this was a boolean variable, I thought it could be interesting to investigate how factors such as primary type, domestic status, community region, and year affected the arrest rate. Additionally, I wanted to determine which year, month, and hour had the greatest crime rate; the relationship between arrested and non-arrested crimes; and the community area and district with the highest crime rate.

<br>

### 3.1 Visualizing Primary Type

To begin, I narrowed my dataframe into a few columns I was interested to look into. Primary type and count then plotted the dataset based on crime rate. For plotting I have used matplotlib and before actually plotting the dataset I had to transform it into pandas dataframe which allowed me to plot. <br>
For most of the plotting I have used the code as shown below:-

```
df = df.toPandas()
dcount.plot(kind='bar', x='columnname', y='columnname', colormap='twilight_shifted')
plt.title("Title", fontdict = {'fontsize': 20,  'color': '#000000'})
plt.show()
```

Before plotting I had to group the dataframe on primary type and calculate the count so that I could plot it, this allowed me to determine the top 10 crimes in Chicago.

<p align="center">
<img width="541" alt="Screen Shot 2022-05-03 at 10 56 22 PM" src="https://user-images.githubusercontent.com/89949851/166617652-2c7ca1eb-1b67-4954-b7e8-d769563d18a1.png">
</p>

I wanted to verify that the outcome was accurate, so I searched for publications about crime in Chicago and discovered that other articles contained the same facts. This is one of the articles that details the most serious crimes in Chicago. [Link](https://www.chicagocriminaldefenselawyer.net/chicago-criminal-lawyer/what-are-the-most-common-crimes-committed-in-chicago)

<br>

### 3.2 Crime Trend across the years


