# Data Processing Course Project

This repository contains the code and resources for the Data Processing course project. The primary goal of this project is to process and analyze Airbnb listing data using a simple pipeline.

## Overview

The project script processes raw Airbnb data, cleans and transforms it into a structured format, and generates visualizations to analyze various aspects of the data, such as average prices for different types of listings.

## Process Pipeline

The data processing and analysis workflow is structured as a pipeline with the following stages:

* Data Ingestion:
        get_data_from_file(): Loads raw data from a CSV file hosted on GitHub.

* Data Cleaning and Transformation:
        handle_data_row(data_row, data): Cleans and transforms each row of data.
        create_* functions: A set of helper functions to clean and categorize various columns (e.g., property type, room type, number of bathrooms).

* Data Aggregation:
        transfer_data(data): Collects cleaned data into a list of tuples.
        convert_to_dataframe(ready_list): Converts the cleaned data list into a pandas DataFrame.

* Data Analysis and Visualization:
        calculate_average_price(data): Computes the average price from the DataFrame.
        create_graph(x, y, avg_prices): Generates and displays a combination plot (stack plot, bar graph, line graph) for average prices based on the number of bedrooms.

Example Output

The script will print the processed data tuples and display a combination plot showing the average price for each number of bedrooms.
