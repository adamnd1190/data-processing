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

# Example Output
The script will print the processed data tuples and display a combination plot showing the average price for each number of bedrooms.

        Loading Data:   0%|                                                        | 0/3585 [00:00<?, ?it/s]
        (0, '0', '1', 1, 1, 1, 1, '0', 34, 9, 40, 3.689)
        (1, '2', '1', 2, 1, 1, 1, '0', 36, 10, 145, 4.977)
        (2, '0', '0', 4, 1, 1, 2, '0', 47, 9, 195, 5.273)
        (3, '0', '1', 2, 1, 1, 1, '0', 41, 10, 65, 4.174)
        (4, '0', '0', 3, 1, 1, 1, '0', 18, 10, 154, 5.037)
        .
        .
        .
        (2822, '2', '1', 2, 1, 1, 1, '0', 2, 8, 79, 4.369)
        (2824, '0', '0', 14, 2, 3, 9, '0', 1, 10, 536, 6.284)
        (2825, '0', '0', 6, 1, 1, 2, '0', 1, 10, 200, 5.298)
        (2827, '0', '1', 2, 1, 1, 1, '0', 2, 10, 125, 4.828)
        (2828, '0', '0', 5, 2, 2, 2, '0', 3, 10, 349, 5.855)
        Loading Data: 100%|███████████████████████████████████████████| 3585/3585 [00:00<00:00, 5662.69it/s]
        
        Average price per bedroom size 
        0    149.789700
        1    126.906439
        2    253.956522
        3    315.603175
        4    411.100000
        5    487.583333
        Name: price, dtype: float64

