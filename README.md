# DIY Project: Small Data Collection System
The purpose of the project is to develop a data collection system. Run it to gather data, and then visualize the data in a graphical manner.

## Data Collection Policies
1. I must collect my own data. I can use an API offered by a website, web application, or web services to collect my data.
2. I may not use data already collected and available in data sets located on websites such as Kaggle.com, Google Research, etc. There are no exceptions to this policy.

# Hurricane & Gas Prices in Florida
I planned out a system that would use Python scripts to collect data using an API, create new data sets, and plot that data onto .csv files. This concept would be centered around
hurricanes that impacted Florida and how they would impact total gas prices before arriving to after leaving. I would use an API from the U.S. Energy Information Administration.

## Project Goals
1. Gather data on the total gas prices in Florida during Hurricanes.
2. Figure out how those prices are possibly impacted by hurricanes that hit Florida.
3. Use Python scripts to help gather data and achieve the goals above.

## Tools Used
1. Visual Studio Code
2. Python
  - requests module
  - Pandas Library
  - MATLAB Library
3. Energy Information Administration's APIv2
4. www.weather.gov - For the information on the hurricanes.

## How Does It Work?
- Fetch U.S. EIA data through an EIA API key and save to a .csv file.
- Analyze the data from the CSV file to plot a graph.
- Use a collection of 5 CSV files to plot a bar graph for the average gasoline prices 2 weeks before and after, and during the hurricanes.

# Findings & Results
Regardless of the state of gas prices before a hurricane, the gas prices tend to drop during or not long after the hurricane is passing. However, other factors not accounted
for in this project such as the state of the economy, entervention by the state and federal government, outages, and stalled crude oil production still have to be considered
on why this tends to be the result.
