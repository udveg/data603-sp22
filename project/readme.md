# Chicago crime dataset analysis 
The Notebook contains Chicago crime data analysis for the last ten years (2011-2021) <br>
The dataset was collected from the ‘city of chicago’ official website which has many public datasets.<br>
This particular readme file provides an overview of the project and how I conducted my analysis.

## Dataset Description
For this particular project I have used three datasets ,the first dataset is the actual crime dataset which contains information about the crime that is time, location, category and primary type. The second dataframe is about the districts in chicago which contains district name and chicago district number which I will further use for getting an comprehensive idea about the crimes in chicago based on different districts. The dataset consists of 22 columns and 7.5 Million rows (dataset size 1.78GB). The dataset has information about the reported crimes from 2001 in the city of chicago except for the murders. The third dataset is about the community area names and their respective codes. Further I will discuss how I used these datasets for analysis. 

* The dataset about the crime and IUCR can be found in the Chicago's official [website.](https://data.cityofchicago.org/Public-Safety/Crimes-One-year-prior-to-present/x2n5-8w5q)
* The dataset which had information about disricts was also from the same [portal.](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6)
* The dataset about the districts was also from the same [website.](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Neighborhoods/bbvz-uum9) 

<p align="center">
<img width="760" height="450" src="https://user-images.githubusercontent.com/89949851/166584816-d4de5cb1-e21a-4233-ae02-d91e825e7fb9.jpeg">
</p>

--- 

<br>

The aim of the project is to find out the crimes that occurred more often, the crime rate trend across the years, and during which month and hour of the day the crime rate was highest. Using the second dataset, I want to get the district name and join the two dataframes so that we can evaluate the crimes based on district. Initally, the dataset had many null values and even the schema was not properly defined, so I had to perform EDA before I did any transformation on the data. Spark doesn't have any built-in libraries for plotting, so I will use matplotlib to plot and I will also use SQL functions to work with the dataframe.

---
<br>

## About this Repository
The repository contains an ipynb file containing the analytic code, a pdf file including the presentation slides, and the second and third datasets containing information about Chicago's districts and community areas. However, the primary dataset was extremely huge, so I have attached a md file containing a link to the third dataset. Finally, the readme file contains all project-related instructions and information.  

### How to run the notebook:
To run the notebook, we must have SQL functions, matplotlib, and other basic libraries installed, as mentioned in the notebook. The whole code needs to be run step by step from the beginning, and the environment should have all the three datasets attached. <br>
The first dataset is a large file so it may take lot of space and also time to read the file. 

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

To ascertain the trend throughout time I conducted groupby on the year column and estimated the number of offenses committed in each year. I then sorted the results by year and presented them in a time-series graph to enhance the comprehension. <br>

The code for grouping and calculating the count :- 
```
df = dataset.groupBy(['Year'])\
                     .count()\
                     .orderBy(['Year', 'count'], ascending=[True, False])

```

<img width="450" alt="Screen Shot 2022-05-03 at 11 09 21 PM" src="https://user-images.githubusercontent.com/89949851/166618413-a7c8881a-6e45-4101-9bcd-c55e8ef80880.png">

From this graph we can understand that the crime rate is plummeting across the years which is pretty good. <br>

### 3.3 Crime trend across months
I wanted to check during which month of the year the crime rate was high for this I had to extract month from date&time column. For this first I extracted month from converted time column using SQL command then used groupby to group them based on months and then counted before plotting. 

```
month_df = dataset.select("datetime", month(col("datetime")).alias("month"), )
```
<img width="471" alt="Screen Shot 2022-05-04 at 1 05 00 AM" src="https://user-images.githubusercontent.com/89949851/166625576-a81a8244-d98b-4347-838e-05dc7b8e612b.png">

We can observe that during June, July, and August, the highest crime rates are recorded. That is usually in summer. This may seem strange, but according to various [articles](https://www.vox.com/2014/6/17/5818432/lock-your-doors-crime-is-worst-in-the-summer), the crime rate peaks during the summer, and the same is true for the state of Illinois.

### 3.4 Crime trend during a day

It is same as analyzing crime across month but here I wanted to check how crime rate varied across different hours of the day. I followed the similar steps, that is using SQL to extract hour and then using groupby and sorthing them before plotting. 

<img width="443" alt="Screen Shot 2022-05-04 at 1 17 56 AM" src="https://user-images.githubusercontent.com/89949851/166626520-44bdf7f5-b98d-4197-974b-07457bcb88c5.png">

<br>

## Step-4 (Joining different datasets for analysis) 

As the dataset had lot of codes which were not comprehensive , I have used other two datasets for joining the original dataset. The columns I used for joining was District and community, initially the dataset had only respective codes by combining them I extracted respective names. For joining the dataframes I have used inner join -

```
district_df = df.join(district,df.District == district.DISTRICT,"inner")
```

<img width="500" alt="Screen Shot 2022-05-04 at 1 04 15 PM" src="https://user-images.githubusercontent.com/89949851/166741125-9ab9bf5b-20ef-4705-b210-393cdb0d282f.png">

I repeated the previous procedures, grouping them and plotting them with matplotlib. According to the graph, the Harrison district had the most offenses, followed by Chicago Lawn and Greesham, which are all located inside Area 4 on the Chicago map. This explains why area 4 is one of the crime hotspots.

 
 <br>
 
 ### 4.1 Comparison between arrested and non-arrested crimes
 
To comapre the relation between arrested and non-arrested crimes, firstly I filtered the crimes based on label that is whether in a crime arrest was made or not then I counted count for each of them and plotted it in single graph for comparison. <br>
In addition, in this section I have attempted to determine the type of crime for which the greatest number of arrests were made so that we can determine which types of crimes were deemed serious, as well as the average rate of arrests made relative to non-arrested crimes in order to determine the trend over the years.

<br>

## Step-5 (Location-based Anlaysis)

Here, I attempted to extract insights from the second and third datasets by applying them to districts and community areas. I plotted the crimes using bar graphs for both districts and community areas, and I utilized scatter plots for crimes that occurred frequently, which provided a clear picture of the crimes.

![Screen Shot 2022-05-12 at 7 43 52 PM](https://user-images.githubusercontent.com/89949851/168184752-3de771e1-a2ba-4843-9acb-9c8c0f5cb51f.png)

I wanted to demonstrate how the scatter plot was utilized to illustrate the crime. Using this, I was able to obtain numerous information, such as the locations where various crimes occurred and the crime rates in various regions.

## Conclusion

I was able to find the relation crime trend across months and hours of the day. The city's overall crime rate, especially the violent crime rate, is higher than the US average. Chicago was responsible for nearly half of 2016's increase in homicides in the US, though the nation's crime rates remain near historic lows. Following are major finding of this analysis:
<br>

* Theft, Battery are by far the most frequent crimes in Chicago. Criminal Damage and Narcotics are falling into the third and fourth column in number. Assault, Burglary, Deceptive Practice, Motor Vehicle Theft and Robbery are next in the line in terms of frequency.
* According to the results the number of crimes are in decline from 2010 to 2015. In 2015, total number of crimes seemed to have its lowest value. However, there was increase in the crimes . 
* During June, July, and August, the highest crime rates are recorded that is usually in summer. It is true for most of the places that crime rate increases during summer. The crime rate appears to have peaked in the summer and remained at its maximum level from June to August, while it was lower in the winter, reaching its lowest point in February. The monthly pattern was steady throughout the entire year.
* The crime rate is higher in certain District in the Southern part of Chicago. More specifically, District Harrison, Greesham, and Chicago Lawn have the highest crime rate.
* The arrest has remained relatively constant for a longer period of time in different years with the exception of 2016 which the trend was relatively decreasing after May. The results also showed that the number of arrests has its lowest value in 2020 and its highest value in 2012.
* The most arrests belongs to Narcotics, Battery, Theft, Criminal Trespass, and Assault, respectively.
* The ratio of Arrest has peaked in 2014 following a sharp drop between 2014 and 2016. The ratio of the arrests has its lowest value in 2016.
* The Area 4 is on the south side of the city. The possible reason for the crime rate being too high may be the proximity of Riverdale to the freeway and the streets. Sadly, the economic conditions in the region are also quite poor, with most people making less than $8,000 a year.
* Crimes such as homicide and sexual assault are more prevalent in the core of Area 4 and its surrounding suburbs, whereas the number of thefts increases as we approach the city limits.
* Austin has the highest crime rate in Chicago's 15th district's neighborhood areas, of which Area 4 is a portion. Located on the West Side of the city, it is the third largest community area in terms of people and the second largest in terms of land area.

If our data analytics can provide us with all of this information about the security status of the city of Chicago, I believe that a larger data analytics project will provide significantly more valuable information that can be used as a powerful resource for taking prudent actions to improve the security status of our cities.

