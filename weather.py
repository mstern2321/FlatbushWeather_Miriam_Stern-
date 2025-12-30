"""
This program reads weather data from two CSV files.
It uses this data to create charts and graphs using matplotlib.
It also analyzes the max, min, and average for each graph.
"""

import matplotlib.pyplot as plt
import os

# Creates a relative path for the csv files
filepath_1 = os.path.join("data", "weather_data_flatbush.csv")
filepath_2 = os.path.join("data", "flatbush_extremes.csv")

# Lists for the average weather data
months = []
avg_high = []
avg_low = []
precipitation = []

def open_filepath_1():
    """
    Reads the weather_data_flatbush.csv file and creates lists with:
    month names, average high temperatures, average low temperatures, and average precipitation
    """
    with open(filepath_1, "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            parts = line.strip().split(",")
            months.append(parts[0])
            avg_high.append(int(parts[1]))
            avg_low.append(int(parts[2]))
            precipitation.append(float(parts[3]))

# Lists for the extreme weather data
months_extremes = []
record_high = []
record_low = []
average_snow = []
def open_filepath_2():
    """
    Reads the flatbush_extremes.csv file and creates lists with:
    month names, record high temperatures, record low temperatures, and average snowfall
    """
    with open(filepath_2, "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            parts = line.strip().split(",")
            months_extremes.append(parts[0])
            record_high.append(int(parts[1]))
            record_low.append(int(parts[2]))
            average_snow.append(float(parts[3]))

# Color palette for the graphs
colors = ("#d9ed92", "#b5e48c", "#99d98c", "#76c893", "#52b69a", "#34a0a4", "#168aad", "#1a759f", "#1e6091", "#184e77", "#013a63", "#012a4a")

#  Graph #1
def line_chart():
    """
    Creates a line chart that compares the average high and low temperatures per month.
    It also prints:
    A. The month with the highest average temperature
    B. The month with the lowest average temperature
    C. The average monthly temperature
    """
    x = range(len(months))
    plt.plot(x, avg_high, marker = "o", color = colors[0], label = "Average high")
    plt.plot(x, avg_low, marker = "o", color = colors[1], label = "Average low")
    plt.grid(True)
    plt.legend()
    plt.xlabel("Month")
    plt.ylabel("Temperature")
    plt.title("Average high and low temperatures")
    plt.xticks(ticks = x, labels = months)
    plt.show()

    average_of_avgs = (sum(avg_high) + sum(avg_low)) / (2 * len(months))
    highest_average_high = max(avg_high)
    lowest_average_low = min(avg_low)
    average_high_month = months[avg_high.index(highest_average_high)]
    average_low_month = months[avg_low.index(lowest_average_low)]
    print(f"The month with the highest average temperature is {average_high_month}.")
    print(f"The month with the lowest average temperature is {average_low_month}.")
    print(f"The average monthly temperature is {average_of_avgs:.2f}.\n")

#  Graph #2
def line_chart_2():
    """
    Creates a line chart to compare the record high and low temperatures each month.
    It also prints:
    A. The month with the highest record temperature
    B. The month with the lowest record temperature
    C. The average of all record temperatures
    """
    x = range(len(months_extremes))
    plt.plot(x, record_high, marker = "o", color = colors[0], label = "Record high")
    plt.plot(x, record_low, marker = "o", color = colors[1], label = "Record low")
    plt.legend()
    plt.title("Record highs and lows")
    plt.grid(True)
    plt.xlabel("Month")
    plt.ylabel("Temperature")
    plt.xticks(ticks = x, labels = months_extremes)
    plt.show()

    average_of_records = (sum(record_high) + sum(record_low)) / (2 * len(record_high))
    highest = max(record_high)
    lowest = min(record_low)
    highest_month = months_extremes[record_high.index(highest)]
    lowest_month = months_extremes[record_low.index(lowest)]
    print(f"The month with the highest temperature is {highest_month}.")
    print(f"The month with the lowest temperature is {lowest_month}.")
    print(f"The average monthly temperature of extremes is {average_of_records:.2f}.\n")

#  Graph #3
def bar_chart_2():
    """
    Creates a bar chart comparing the average snow per month.
    It also prints:
    A. The month with the highest snowfall
    B. The month with the lowest snowfall
    C. The average snowfall of all months
    """
    x = range(len(months_extremes))
    plt.bar(x, average_snow, color = colors)
    plt.xticks(ticks = x, labels = months_extremes)
    plt.grid(True)
    plt.title("Snowfall by month")
    plt.xlabel("Month")
    plt.ylabel("Snowfall")
    plt.show()

    average_snowfall = sum(average_snow)/len(average_snow)
    highest_snowfall = max(average_snow)
    lowest_snowfall = min(average_snow)
    highest_snowfall_month = months_extremes[average_snow.index(highest_snowfall)]
    lowest_snowfall_month = months_extremes[average_snow.index(lowest_snowfall)]
    print(f"The month with the highest snowfall is {highest_snowfall_month}.")
    print(f"The month with the lowest snowfall is {lowest_snowfall_month}.")
    print(f"The average snowfall is {average_snowfall:.2f}.\n")

#  Graph #4
def largest_temperature_range():
    """
    Calculates the temperature range per month by finding the difference between the record high and record low.
    Creates a line chart to compare the monthly temperature ranges.
    It also prints:
    A. The month with the highest temperature range
    B. The month with the lowest temperature range
    C. The average temperature range of all months
    """
    x = range(len(months_extremes))
    range_temps = [high - low for (high, low) in zip(record_high, record_low)]
    plt.plot(x, range_temps, marker="o", color=colors[0])
    plt.title("Monthly temperature range")
    plt.grid(True)
    plt.xlabel("Month")
    plt.ylabel("Temperature range")
    plt.xticks(ticks=x, labels=months_extremes)
    plt.show()

    average_range = sum(range_temps)/len(range_temps)
    largest_range = max(range_temps)
    smallest_range = min(range_temps)
    largest_range_month = months_extremes[range_temps.index(largest_range)]
    smallest_range_month = months_extremes[range_temps.index(smallest_range)]
    print(f"The month with the largest temperature range is {largest_range_month}.")
    print(f"The month with the smallest temperature range is {smallest_range_month}.")
    print(f"The average temperature range is {average_range:.2f}.\n")







if __name__ == "__main__":
    open_filepath_1()
    open_filepath_2()
    line_chart()
    line_chart_2()
    bar_chart_2()
    largest_temperature_range()

"""
1. Graph #1 compares the average high and low for each month using a line chart. 
The temperature increases steadily from January until july and then decreases toward December. 
July has the highest average temperature, while January has the lowest average temperature. 
This graph follows the seasonal patterns of hot summers and cold winters. 
I noticed that the average temperature change from month to month is pretty consistent. 
I was surprised that the difference between high and low temperatures was greater in the summer than in the winter.

2. Graph #2 compares the record high and low for each month using a line chart. 
July has the highest record temperature, while January has the lowest record temperature. 
There is a much bigger gap between record highs and lows than between average highs and lows. 
This shows that the extreme temperatures can be very different than the average temperatures. 
I was surprised to see that spring and fall have some very high temperatures too. 

3. Graph #3 uses a bar graph to show the average snowfall in Flatbush for each month. 
Snowfall occurs between November and April.
The highest snowfall is in January and February. 
There is no snowfall between March and October.
Snowfall is obviously a strictly winter event in Flatbush.
I was surprised that there was more snowfall in February than in December. 


4. Graph #4 uses a line graph to show the difference between the record highs and lows. 
April has the largest temperature range at 68 degrees, while July has the smallest at 47 degrees.
The temperature range is larger in Spring and Fall than Winter and summer. 
However, Winter also shows fairly large ranges, but those are due to very low record temperatures.
I was surprised that even though there are such hot summer days it still has a very small range of temperatures. 
"""