import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import cartopy.crs as ccrs

# Load the dataset
data = pd.read_csv('/Users/emilyrutkowski/Documents/MBIO691Project/coral_forecast.csv', skiprows=[1])

# Group data by site
# Sites are characterised by a unique (lon, lat) combination. To group sites together, 
# we can firstly create a new column with the combined longitude and latitude.
data['lon_lat'] = list(zip(data.longitude, data.latitude))

# We can now perform groupby operations, e.g. computing mean values across all models
data = data.groupby('lon_lat').mean().drop(columns='model')

# Display a summary
data

# Calculate percentage change in coral cover
data['coral_change_percent'] = (
    (data['coral_cover_2100'] - data['coral_cover_2020']) / data['coral_cover_2020']
) * 100

#View calculation of coral percent change
print(data.head())

# Check for NaN values
print(data[['longitude', 'latitude', 'coral_change_percent']].isna().sum())

# Calculate the average percentage change across simulations
average_change = data.groupby(['longitude', 'latitude'])['coral_change_percent'].mean().reset_index()

print(average_change['coral_change_percent'].describe())

# Cap the coral_change_percent values at 200%
average_change['coral_change_percent'] = average_change['coral_change_percent'].clip(upper=200)

#Plot 

import matplotlib.ticker as mticker

# Create the figure and map
plt.figure(figsize=(20, 20))
ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines()

# Plot the data
sc = ax.scatter(
    average_change['longitude'], average_change['latitude'], 
    c=average_change['coral_change_percent'], cmap='RdYlGn', 
    s=30, transform=ccrs.PlateCarree(), alpha=0.5
)

# Color bar with adjusted size and title positioning
cbar = plt.colorbar(sc, fraction=0.01, pad=0.05)
cbar.set_label("Average Coral Cover Change (%)", fontsize=8, labelpad=20, fontweight='bold', rotation=270, loc='center')

# Set specific intervals for latitude and longitude ticks
gl = ax.gridlines(draw_labels=True, linestyle=":", color="lightgray")
gl.top_labels = False
gl.right_labels = False
gl.xlabel_style = {'size': 12}
gl.ylabel_style = {'size': 12}
gl.xlocator = mticker.FixedLocator([-180, -90, 0, 90, 180])
gl.ylocator = mticker.FixedLocator([-40, -20, 0, 20, 40])

# Set main title
plt.title("Predicted Average Percentage Change in Coral Cover (2020-2100)", fontsize=9, pad=15, fontweight='bold')

# Define the caption with "Figure 1." in bold
caption_text = (r"$\bf{Figure\ 1.}$ Predicted average percentage change in coral cover from 2020 to 2100, based on simulations across approximately 52,000 sites. Each point represents the average "
                "coral cover change at a given location, with colors ranging from green (increase in coral cover) "
                "to red (decrease in coral cover). The projection provides a global view, showing the widespread "
                "decline in tropical coral cover, particularly in the Indo-Pacific and Caribbean regions. This figure aims to illustrate the "
                "geographical variability and expected impact on coral reefs over the century.")

# Add the caption with a box around it and bring it closer to the map
plt.figtext(0.5, 0.3, caption_text, wrap=True, ha='center', fontsize=8, va='top', 
            bbox=dict(facecolor='whitesmoke', edgecolor='gray', boxstyle='round,pad=0.5'))

# Save and show the plot
plt.savefig('/Users/emilyrutkowski/Documents/MBIO691Project/average_coral_cover_change_final_map_with_boxed_caption.png', dpi=300, bbox_inches='tight')
plt.show()

#---Moving on to figure 2---

data['coral_cover_2020'] = pd.to_numeric(data['coral_cover_2020'], errors='coerce')
data['coral_cover_2100'] = pd.to_numeric(data['coral_cover_2100'], errors='coerce')

# Calculate coral cover change percentage, SST change, and pH change
data['coral_change_percent'] = ((data['coral_cover_2100'] - data['coral_cover_2020']) / data['coral_cover_2020']) * 100
data['SST_change'] = data['SST_2100'] - data['SST_2020']
data['pH_change'] = data['pH_2100'] - data['pH_2020']

# Cap coral cover change to a reasonable max for clarity (e.g., 200%)
data['coral_change_percent'] = data['coral_change_percent'].clip(upper=200)

# Scatter plot
plt.figure(figsize=(10, 8))
sc = plt.scatter(
    data['SST_change'], data['pH_change'], 
    c=data['coral_change_percent'], cmap='coolwarm', alpha=0.6, s=20
)
cbar = plt.colorbar(sc, label="Coral Cover Change (%)")
cbar.ax.set_ylabel("Coral Cover Change (%)", rotation=270, labelpad=15, fontsize=10, fontweight='bold')
cbar.ax.tick_params(labelsize=10)  # Increase tick label font size

# Add labels
plt.xlabel("SST Change (°C)", fontsize=10, fontweight='bold')
plt.ylabel("Predicted pH Change (units)", fontsize=10, fontweight='bold')
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# Title split into two lines
plt.title("Predicted Percentage Change in Coral Cover\nas a Function of SST and pH Change", 
          fontsize=12, fontweight='bold', pad=10, ha='center')

# Caption text
caption_text = (
    r"$\bf{Figure\ 2.}$ Predicted percentage change in coral cover from 2020 to 2100 as a function of SST "
    "change and pH change, averaged across simulations. Each point represents a site, with colors indicating "
    "coral cover change percentages (blue for greater declines, red for stability or minor declines). This scatter "
    "plot highlights the expected decline in coral cover under increased SST and decreased pH, illustrating how "
    "changes in temperature and ocean acidification are linked to coral ecosystem health."
)

# Add the caption below the figure in a box
plt.figtext(0.5, -0.01, caption_text, wrap=True, ha='center', fontsize=8, va='top',
            bbox=dict(facecolor='whitesmoke', edgecolor='gray', boxstyle='round,pad=0.5'))

# Save and show the plot
plt.savefig('/Users/emilyrutkowski/Documents/MBIO691Project/coral_cover_change_sst_ph_final_with_caption.png', dpi=300, bbox_inches='tight')
plt.show()

#---Moving on to Figure 3---

data['coral_cover_2020'] = pd.to_numeric(data['coral_cover_2020'], errors='coerce')
data['coral_cover_2100'] = pd.to_numeric(data['coral_cover_2100'], errors='coerce')

# Calculate coral cover change percentage, SST change, and pH change
data['coral_change_percent'] = ((data['coral_cover_2100'] - data['coral_cover_2020']) / data['coral_cover_2020']) * 100
data['SST_change'] = data['SST_2100'] - data['SST_2020']
data['pH_change'] = data['pH_2100'] - data['pH_2020']

# Pearson's Correlation Coefficient
correlation_data = data[['coral_change_percent', 'SST_change', 'pH_change', 'SST_seasonal', 'PAR', 'longitude', 'latitude']].corr()

# Plot heatmap
plt.figure(figsize=(12, 10))
heatmap = sns.heatmap(
    correlation_data, 
    annot=True, 
    fmt=".2f",  # Format annotation to 2 decimal places
    cmap="RdBu",  # Use RdBu for clearer distinction
    vmin=-1, vmax=1, center=0, 
    square=True, 
    linewidths=.5,  # Thin lines around cells
    cbar_kws={"shrink": 0.6, "label": "Pearson's Correlation Coefficient"},  # Updated label
    annot_kws={"size": 10}  # Annotation font size
)

# Two-line title with extra padding
plt.title("Correlation Matrix of Explanatory Variables\nand Coral Cover Change", fontsize=16, fontweight='bold', pad=30)

# Bold axis labels and adjust rotation
plt.xlabel("", fontsize=12, fontweight='bold')
plt.ylabel("", fontsize=12, fontweight='bold')
plt.xticks(rotation=30, ha='right', fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')

# Access and modify the color bar directly
colorbar = heatmap.collections[0].colorbar
colorbar.set_label("Pearson's Correlation Coefficient", fontsize=12, fontweight='bold')  # Bold label
colorbar.ax.tick_params(labelsize=10)  # Adjust tick label font size

# Caption text
caption_text = (
    r"$\bf{Figure\ 3.}$ Correlation matrix of explanatory variables and coral cover change. The heatmap displays "
    "Pearson correlation coefficients between coral cover change and each explanatory variable, as well as correlations "
    "among explanatory variables themselves. Negative correlations are shown in shades of red, while positive correlations "
    "are in shades of blue. The strength of correlation is represented by color intensity, with values closer to ±1 indicating "
    "stronger relationships. Notably, PAR and latitude show the highest correlations with coral cover change, while SST change "
    "and SST seasonal cycle are also positively correlated with each other."
)

# Add the caption below the figure in a box
plt.figtext(0.5, -0.03, caption_text, wrap=True, ha='center', fontsize=9, va='top',
            bbox=dict(facecolor='whitesmoke', edgecolor='gray', boxstyle='round,pad=0.5'))

# Save the plot
plt.savefig('/Users/emilyrutkowski/Documents/MBIO691Project/coral_cover_correlation_heatmap_with_caption_final.png', dpi=300, bbox_inches='tight')
plt.show()
