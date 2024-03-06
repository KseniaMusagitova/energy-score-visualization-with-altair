import pandas as pd
import altair as alt

# Load the data from CSV file into a DataFrame
df = pd.read_csv('energy_disclosure_2021_rows.csv')

# Create a scatter plot using Altair
chart = alt.Chart(df).mark_point().encode(
    x='DOF_Gross_Square_Footage',
    y='Energy_Star_1-100_Score',
    tooltip=['Street_Name', 'Energy_Star_1-100_Score']
).properties(
    title='Energy Efficiency Score vs. Gross Square Footage'
)

# Save the chart as an HTML file
chart.save('chart2.html')