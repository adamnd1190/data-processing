import pandas as pd
from tqdm import tqdm
import math
import numpy as np
import matplotlib.pyplot as plt
import statistics

print_debug = True

def get_data_from_file():

    path_string = rf"https://raw.githubusercontent.com/adamnd1190/data-processing/main/raw_data.csv"
    simulation_data = pd.read_csv(path_string, encoding="ISO-8859-1")
    return simulation_data

def transfer_data(data):
    ready_list = []
    for data_row in data:
        ready_data_tuple = handle_data_row(data_row)
        ready_list.append(ready_data_tuple)

def handle_data_row(data_row, data):
    if any(pd.isnull(data_row[col]) for col in data_row.index[1:]):
        return None
    id = create_int(data_item=data_row[0])
    property_type = create_property_category(data_item=data_row[5], data_id=data_row.name)
    room_type = create_room_category(data_item=data_row[6], data_id=data_row.name)
    accommodates = create_acco_number(data_item=data_row[7], data_id=data_row.name)
    bathrooms = create_bathrooms_number(data_item=data_row[8], data_id=data_row.name)
    bedrooms = create_bedrooms_number(data_item=data_row[9], data_id=data_row.name)
    beds = create_beds_number(data_item=data_row[10], data_id=data_row.name)
    bed_type = create_bedtype_category(data_item=data_row[11], data_id=data_row.name)
    number_of_reviews = create_reviews_number(data_item=data_row[18], data_id=data_row)
    #number_of_reviews = data_row[18]
    review_scores_value = create_reviewscore_number(data_item=data_row[24], data_id=data_row.name)
    price = create_price_number(data_item=data_row[13], data_id=data_row.name, data=data)

    ln_price = None  # Default value if 'price' is None
    if price is not None:
        ln_price = round(np.log(price), 3)

    if any(value is None for value in (id, property_type, room_type, accommodates, bathrooms, bedrooms, beds, bed_type,
                                       number_of_reviews, review_scores_value, price)):
        return None

    ready_data_tuple = (id, property_type, room_type, accommodates, bathrooms, bedrooms, beds, bed_type,
                        number_of_reviews, review_scores_value, price, ln_price)
    return ready_data_tuple

def create_int(data_item):

    data_item = int(data_item)

    return data_item

def create_property_category(data_item, data_id):
    property_dict = {
        'Apartment': '0',
        'Condominium': '1',
        'House': '2',
        'Bed & Breakfast': '3',
        'Boat': '3',
        'Dorm': '3',
        'Entire Floor': '3',
        'Guesthouse': '3',
        'Loft': '3',
        'Other': '3',
        'Townhouse': '3',
        'Villa': '3'
    }

    if isinstance(data_item, int):
        if print_debug:
            print(f"The property type inserted by row {data_id} is an integer.")
        return None
    elif data_item in property_dict:
        return property_dict[data_item]
    else:
        if print_debug:
            print(f"The property type inserted by row {data_id} is not in the dictionary or is empty.")
        return None

def create_room_category(data_item, data_id):
    room_dict = {
        'Entire home/apt': '0',
        'Private room': '1',
        'Shared room': '2',
    }

    if isinstance(data_item, int):
        if print_debug:
            print(f"The room type inserted by row {data_id} is an integer.")
        return None
    elif data_item in room_dict:
        return room_dict[data_item]
    else:
        if print_debug:
            print(f"The room type inserted by row {data_id} is not in the dictionary or is empty.")
        return None

def create_acco_number(data_item, data_id):
    if math.isnan(data_item):  # In case there is nothing in the cell.
        if print_debug:
            print(f"The accommodation number that was inserted by row {data_id} is empty.")
        return None
    elif isinstance(data_item, str):
        if print_debug:
            print(f"The accommodation number that was inserted by row {data_id} is a string.")
        return None
    else:
        if data_item <= 0:  # In case the number in the cell is negative.
            if print_debug:
                print(f"The accommodation number that was inserted by row {data_id} is negative {data_item}.")
            return 0
        else:  # if all ok.
            data_item = create_int(data_item=data_item)
            return data_item

def create_bathrooms_number(data_item, data_id):
    if math.isnan(data_item):  # In case there is nothing in the cell.
        if print_debug:
            print(f"The bathroom number that was inserted by row {data_id} is empty.")
        return None
    elif isinstance(data_item, str):
        if print_debug:
            print(f"The bathrooms number that was inserted by row {data_id} is a string.")
        return None
    else:
        if data_item < 0:    # In case the number in the cell is negative.
            if print_debug:
                print(f"The bathroom that was inserted by row {data_id} is negative {data_item}.")
            return 0
        else:  # if all ok.
            data_item = create_int(data_item=data_item)
            return data_item

def create_bedrooms_number(data_item, data_id):
    if math.isnan(data_item):  # In case there is nothing in the cell.
        if print_debug:
            print(f"The bedroom number that was inserted by row {data_id} is empty.")
        return None
    elif isinstance(data_item, str):
        if print_debug:
            print(f"The bedrooms number that was inserted by row {data_id} is a string.")
        return None
    else:
        if data_item < 0:    # In case the number in the cell is negative.
            if print_debug:
                print(f"The bedroom number that was inserted by row {data_id} is negative {data_item}.")
            return 0
        else:  # if all ok.
            data_item = create_int(data_item=data_item)
            return data_item

def create_beds_number(data_item, data_id):
    if math.isnan(data_item):  # In case there is nothing in the cell.
        if print_debug:
            print(f"The bed number that was inserted by row {data_id} is empty.")
        return None
    elif isinstance(data_item, str):
        if print_debug:
            print(f"The beds number that was inserted by row {data_id} is a string.")
        return None
    else:
        if data_item < 0:    # In case the number in the cell is negative.
            if print_debug:
                print(f"The bed number that was inserted by row {data_id} is negative {data_item}.")
            return 0
        else:  # if all ok.
            data_item = create_int(data_item=data_item)
            return data_item

def create_bedtype_category(data_item, data_id):
    bed_dict = {
        'Real Bed': '0',
        'Pull-out Sofa': '1',
        'Futon': '2',
        'Couch': '3',
        'Airbed': '4'
    }

    if isinstance(data_item, int):
        if print_debug:
            print(f"The bed type inserted by row {data_id} is an integer.")
        return None
    elif data_item in bed_dict:
        return bed_dict[data_item]
    else:
        if print_debug:
            print(f"The bed type inserted by row {data_id} is not in the dictionary or is empty.")
        return None

def create_reviews_number(data_item, data_id):
    if math.isnan(data_item):  # In case there is nothing in the cell.
        if print_debug:
            print(f"The number of reviews that was inserted by row {data_id} is empty.")
        return None
    elif isinstance(data_item, str):
        if print_debug:
            print(f"The review score number that was inserted by row {data_id} is a string.")
        return None
    else:
        if data_item <= 0:   # In case the number in the cell is not in the required range.
            if print_debug:
                print(f"The number of reviews that was inserted by row {data_id} is negative. {data_item}.")
            return 0
        else:  # if all ok.
            data_item = create_int(data_item=data_item)
            return data_item

def create_reviewscore_number(data_item, data_id):
    if math.isnan(data_item):  # In case there is nothing in the cell.
        if print_debug:
            print(f"The review score number that was inserted by row {data_id} is empty.")
        return None
    elif isinstance(data_item, str):
        if print_debug:
            print(f"The review score number that was inserted by row {data_id} is a string.")
        return None
    else:
        if data_item < 0 or data_item > 10:  # In case the number in the cell is negative.
            if print_debug:
                print(f"The review score that was inserted by row {data_id} is our of range. {data_item}.")
            return 0
        else:  # if all ok.
            data_item = create_int(data_item=data_item)
            return data_item

def calculate_average_price(data):
    return data['price'].mean()

def create_price_number(data_item, data_id, data):
    if math.isnan(data_item):  # In case there is nothing in the cell.
        if print_debug:
            print(f"The price number that was inserted by row {data_id} is empty.")
        average_price = calculate_average_price(data)
        return average_price
    elif isinstance(data_item, str):
        if print_debug:
            print(f"The price number that was inserted by row {data_id} is a string.")
        return None
    else:
        data_item = create_int(data_item=data_item)
        if data_item < 0:    # In case the number in the cell is negative.
            if print_debug:
                print(f"The price number that was inserted by row {data_id} is negative {data_item}.")
            return 0
        else:  # if all ok.
            return data_item

def convert_to_dataframe(ready_list):
    column_names = ['id', 'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds',
                    'bed_type', 'number_of_reviews', 'review_scores_value', 'price', 'ln_price']
    df = pd.DataFrame(ready_list, columns=column_names)
    return df

def create_graph(x, y, avg_prices):
    fig, ax = plt.subplots()
    create_combination_plot(ax, x, y)
    create_title_labels(ax)
    create_axis_limits(ax, x, y)
    create_axis_labels(ax, avg_prices)  # Pass avg_prices to this function
    create_vertical_horizontal_line(ax, x, y)
    create_legend(ax)
    plt.show()

def create_combination_plot(ax, x, y):
    create_stack_plot(ax, x, y)  # Stack plot at the bottom
    create_bar_graph(ax, x, y)   # Bar graph on top of stack plot
    create_line_graph(ax, x, y)  # Line graph on top of both stack plot and bar graph

def create_axis_labels(ax, avg_prices):
    x = avg_prices['bedrooms']
    ax.set_xticks(x)
    ax.set_xticklabels(x.astype(str))  # Convert numerical values to string labels

def create_stack_plot(ax, x, y):
    ax.stackplot(x, y, alpha=0.5, labels=['Stack Plot'])

def create_bar_graph(ax, x, y):
    barwidth = 0.5
    ax.bar(x, y, color='orange', width=barwidth, align='center', label='Bar Plot')

def create_line_graph(ax, x, y):
    line = ax.plot(x, y, marker='o', linestyle='-', color='blue', label='Line Graph', markersize=8, linewidth=2)
    for i, (xi, yi) in enumerate(zip(x, y)):
        ax.annotate(f'{yi:.2f}', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')
    return line

def create_title_labels(ax):
    ax.set_title('Multiple Plots of Average Price for Each Bedroom')
    ax.set_xlabel('Bedrooms')
    ax.set_ylabel('Price')

def create_axis_limits(ax, x, y):
    ax.set_xlim(min(x) - 0.5, max(x) + 0.5)  # Adjust x-axis limits
    ax.set_ylim(0, 550)
def create_vertical_horizontal_line(ax, x, y):
    ax.axvline(np.mean(x), color='r', linestyle='--', label='Mean Bedrooms')
    ax.axhline(np.mean(y), color='g', linestyle='--', label='Mean Price')

def create_legend(ax):
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3, fontsize=10)
    plt.subplots_adjust(bottom=0.2)

def main():
    data = get_data_from_file()
    skipped_count = 0
    ready_list = []
    #transfer_data(data)
    for index, data_frame_item in tqdm(data.iterrows(), total=data.shape[0], desc="Loading Data", ncols=100):
        data_tuple = handle_data_row(data_row=data_frame_item, data=data)
        if data_tuple is None:
            skipped_count += 1  # Increment the count for skipped rows
        else:
            ready_list.append(data_tuple)
            print(data_tuple)
    print("Stop")
    total_rows = data.shape[0]
    percentage_skipped = (skipped_count / total_rows) * 100
    print(f"Percentage of rows skipped: {percentage_skipped:.2f}%")

    df = convert_to_dataframe(ready_list)  # Convert ready_list to DataFrame

    avg_prices = df.groupby('bedrooms')['price'].mean().reset_index()
    x = avg_prices['bedrooms']
    y = avg_prices['price']

    create_graph(x, y, avg_prices)

    print(x)
    print(y)



if __name__ == "__main__":
    main()