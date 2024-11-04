# MBIO691
  -Coral Cover Change Analysis Final Project 

This project analyzes coral cover change predictions over the 21st century based on 12 simulations of climate change impacts, with a dataset of environmental variables such as sea surface temperature (SST), SST seasonal, pH levels, latitude, longitude, and Photosynthetically Available Radiation (PAR). Using Python and data visualization libraries, I produced three figures that explore these relationships.

## Project Overview
Coral reefs are under threat from rising ocean temperatures and acidification. This project uses simulation data from 52,000 sites to investigate predicted changes in coral cover from 2010-2020 to 2090-2100. Analyses include:
- Mapping coral cover change over time.
- Exploring relationships between coral cover, SST, and pH changes.
- Assessing which environmental factors are most predictive of coral cover change and how they relate to themselves.

The outputs include several figures to visualize and interpret the data.

## Data Description
The dataset (coral_forecast.csv) includes simulated data for various environmental variables and coral cover predictions. These columns include:
- `coral_cover_2020`, `coral_cover_2100`: Estimated coral cover in square kilometers, averaged for 2010-2020 and 2090-2100.
- `SST_2020`, `SST_2100`: Mean sea surface temperature (in °C) for the respective years.
- `pH_2020`, `pH_2100`: Mean pH values averaged across each time period.
- `SST_seasonal`: Amplitude of seasonal SST cycle (summer-winter temperature difference).
- `PAR`: Photosynthetically Available Radiation, indicating light availability for photosynthesis.
- `longitude`, `latitude`: Geographic coordinates.
- `model`: Simulation configuration (0-11), each representing a different future climate scenario.

## Figures
1. Figure 1: Map showing the predicted average percentage change in coral cover from 2020 to 2100 across geographic locations.
2. Figure 2: Scatter plot displaying the predicted percentage change in coral cover as a function of SST and pH changes.
3. Figure 3: Correlation matrix heatmap of explanatory variables and coral cover change, highlighting relationships among variables.

## Table of Contents
- [Requirements]
- [Setup Instructions]
- [Data Processing and Analysis Steps]
- [Explanation of Figures]

## Requirements
To run this project, you'll need the following Python libraries:
- `pandas`: For data loading and manipulation.
- `matplotlib`: For plotting and creating figures.
- `seaborn`: For enhanced visualizations, particularly for the heatmap.
- `cartopy`: For map projections in Figure 1.
- Install these using:
    ```bash
    pip install pandas matplotlib seaborn cartopy

## Setup Instructions
  1. Clone or download my repository to your local machine.
  2. Ensure that the dataset coral_forecast.csv is in the same directory as the script. This file contains the environmental data, including coral cover predictions, SST, pH, and other relevant variables for 52,000 sites. Be cautious as this file is quite large. (63.5 MB)
  3. Run the script using Python: python "Final Project.py"

## Data Processing and Analysis
  1. The scripts performs loading and data processing & calculating changes.
  2. For loading and data processing:
     -data = pd.read_csv('Your/path/to/coral_forecast.csv', skiprows=[1]) --> loads the dataset coral_forecast.csv
     -data['coral_cover_2020'] = pd.to_numeric(data['coral_cover_2020'], errors='coerce')
      data['coral_cover_2100'] = pd.to_numeric(data['coral_cover_2100'], errors='coerce') --> Converts relevant columns to numeric
       format, to ensure there are no non-numeric values errors.
  4. For calculating changes:
     -data['coral_change_percent'] = ((data['coral_cover_2100'] - data['coral_cover_2020']) / data['coral_cover_2020']) * 100
         --> Calculates the change in coral cover between 202 and 2100 as a percentage.
     -data['SST_change'] = data['SST_2100'] - data['SST_2020']
      data['pH_change'] = data['pH_2100'] - data['pH_2020'] --> Calculates the changes in SST and pH between two time periods.
     -data['absolute_latitude'] = data['latitude'].abs() --> Converts latitude to its absolute value
  6. For Analysis:
  7. 
      -Figure 1: Map of Predicted Average Coral Cover Change
        	Groups data by longitude and latitude to calculate the average coral cover change across simulations.
          Plots a map using Cartopy’s Robinson projection, with points colored by the percentage change in coral cover.
	        A color bar is added to represent the range of changes (centered at 0) with a CVD friendly color map and a caption explaining the plot.
     
      -Figure 2: Scatter Plot of Coral Cover Change as a Function of SST and pH Changes
          Filters data to include only sites with a decrease in coral cover.
	        Creates a scatter plot showing coral cover change as a function of SST and pH changes, focusing on declines in coral cover.
	        Uses a color gradient to represent the extent of decline, with the color map starting at 0 to highlight negative changes.
	        Adds a caption describing the plot’s focus on relationships between SST, pH, and coral decline.
  
      -Figure 3: Correlation Matrix Heatmap of Explanatory Variables and Coral Cover Change
          Calculates Pearson correlation coefficients between coral cover change and other variables, including SST change, pH change, absolute latitude, PAR, and longitude.
	        Generates a heatmap of the correlation matrix.
	        Uses a color bar to indicate the strength and direction of correlations, with a caption explaining the correlations, particularly noting the latitude and PAR relationship.
       -Each script outputs the figures as a .png file. 

## Explanation of Figures

Figure 1: Map of Predicted Coral Cover Change
	-This figure visualizes the geographic distribution of predicted coral cover change. Colors range from red (increase) to blue (decrease).
	-Interpretation: The map shows widespread declines in tropical coral cover, particularly in regions like the Indo-Pacific and Carribean. 

Figure 2: Coral Cover Change as a Function of SST and pH
	-This scatter plot highlights the relationship between coral cover decline and changes in SST and pH.
	-Interpretation: The plot emphasizes that higher SST increases and lower pH values are often associated with declines in coral cover.

Figure 3: Correlation Matrix of Variables and Coral Cover Change
	-This heatmap displays Pearson correlation coefficients between coral cover change and various environmental variables.
	-Interpretation: PAR (Photosynthetically Available Radiation) shows the highest positive correlation with coral cover change, with a correlation coefficient of 0.59. SST Change (Sea Surface Temperature change) and SST Seasonal Cycle also have notable correlations, with coefficients of approximately -0.54 and -0.57, respectively, indicating a moderate negative relationship with coral cover change (ie higher SST greater coral decline).

     
