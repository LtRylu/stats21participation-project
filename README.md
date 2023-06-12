# CSV Data Analysis with Streamlit

This Streamlit application allows you to upload a CSV file and perform basic data analysis on the dataset. It provides various statistics and visualizations based on the selected column.

## Features

- Upload a CSV file
- Display dataset statistics: number of rows, number of columns, and variable types
- Select a column from the dataset
- Display statistics and visualizations based on the column type:
  - For numerical columns: five number summary and distribution plot
  - For categorical columns: proportions table and bar plot
- Customizable histogram: input the number of bins for the histogram plot

## Prerequisites

- Python 3.6 or later
- Streamlit library (`pip install streamlit`)
- Pandas library (`pip install pandas`)
- Seaborn library (`pip install seaborn`)

## Usage

1. Clone this repository or download the source code.
2. Install the required libraries listed in the "Prerequisites" section.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the Streamlit application using the following command:

   ```bash
   streamlit run csv_analysis_app.py