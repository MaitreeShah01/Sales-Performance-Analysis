# Sales Performance Analysis Project

## Overview
This project analyzes sales data using Python for data preparation and Tableau for visualization. It involves creating interactive dashboards and charts to explore key sales metrics, including salesperson effectiveness, product sales trends, and cumulative sales over time. The aim is to help businesses make data-driven decisions by providing actionable insights.

## Technologies Used
- **Python** (Pandas, NumPy): For generating and processing synthetic sales data.
- **Tableau**: For building interactive dashboards and visualizations.

## Project Structure
- **`sales_data.csv`**: A CSV file containing the generated synthetic sales data.
- **`sales_analysis.py`**: Python script used for generating the sales data.
- **Tableau workbook (.twb/.twbx)**: Tableau file containing the interactive visualizations.

## How the Project Was Built
1. **Data Generation (Python)**:  
   The sales data was generated using Python, with the following features:
   - **Date**: Randomized date ranges for the sales transactions.
   - **Product**: Different categories of products.
   - **Region**: Sales distribution across different regions.
   - **Salesperson**: A set of salespeople responsible for the sales.
   - **Sales Amount**: Randomized sales values based on the above features.
   
2. **Data Processing (Python)**:  
   The generated data was cleaned and processed using Pandas and NumPy. Calculations for cumulative sales and other metrics were included.

3. **Data Visualization (Tableau)**:  
   - Imported the processed data into Tableau.
   - Created multiple visualizations:
     - **Combined Bar and Line Chart**: To compare revenue trends.
     - **Sales Performance by Salesperson**: A bubble chart to visualize individual salesperson effectiveness.
     - **Filtered Product Sales**: An area chart to track sales by product.
     - **Cumulative Sales Trend Over Time**: A line chart showing cumulative sales across different time periods.

4. **Interactivity**:  
   Filters and parameters were added to allow users to interact with the data:
   - Product selection via dropdown (filter by product).
   - Dynamic graphs that update when selecting different products or time periods.

## Steps to Reproduce the Results

### **1. Data Generation**
- Run the `sales_analysis.py` script to generate synthetic sales data and save it as `sales_data.csv`.

### **2. Import Data into Tableau**
- Open Tableau and import the `sales_data.csv` file.
- Use Tableau's drag-and-drop functionality to create different charts and graphs based on the data.

### **3. Building the Dashboard**
- Create the following views:
   1. **Combined Bar and Line Chart**: Drag `Date` to **Columns**, `Total Sales` to **Rows**, and create dual-axis graphs.
   2. **Sales Performance by Salesperson (Bubble Chart)**: Use `Salesperson` as the category, `Total Sales` as the size, and `Product` as the color.
   3. **Filtered Sales by Product (Area Chart)**: Use `Date` and `Sales by Product` to create an area chart.
   4. **Cumulative Sales Trend Over Time**: Use `Date` and `Cumulative Sales` to show a line chart.

### **4. Add Interactivity**
- Add filters or parameters like **Select Product** to make the charts interactive.

### **5. Final Visualization**
- Save the Tableau workbook and publish it or share it with stakeholders.

## Key Findings and Insights

- **Sales Trend Over Time**: The combined bar and line chart highlights seasonal sales fluctuations and growth trends.
- **Salesperson Performance**: The bubble chart visualizes the top-performing salespeople and helps identify areas for training or incentive programs.
- **Filtered Product Sales**: The area chart allows for in-depth analysis of specific product sales over time.
- **Cumulative Sales Insights**: The line chart gives a quick overview of how cumulative sales evolve over time, providing insights into growth and potential bottlenecks.

## Tableau Dashboard Preview

[Sales Performance Analysis Dashboard](https://public.tableau.com/app/profile/maitree.shah/viz/CombinelineandbarchartwithareagraphSalesanalysis/Dashboard2)

This dashboard includes:
1. Cumulative sales trends (line graph).
2. Filtered sales per product (area chart).
3. Monthly total sales distribution (bar graph).
4. Sales performance by salesperson (bubble chart).

## Conclusion
This project demonstrates how to build an interactive sales performance dashboard using Python and Tableau. The visualizations help stakeholders make informed decisions by providing insights into salesperson effectiveness, product trends, and overall sales performance.


