import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    dt = datetime.fromisoformat(iso_string) #Check with .year .month format
    return dt.strftime("%A %d %B %Y")
  


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_farenheit=float(temp_in_farenheit)
    result=((temp_in_farenheit-32)*5)/9
    result=round(result,1)
    return result


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum = 0
    total_items = len(weather_data)
    for item in weather_data:
        item = float(item)
        sum += item
    mean = sum/(total_items)
    return float(mean)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather_data = []
    with open(csv_file) as this_file:
        results = csv.reader(this_file)
        count = 0
        for line in results:
            if line == []:
                pass
            elif count != 0:
                updated_line = line
                updated_line[1] = int(line[1])
                updated_line[2] = int(line[2])
                weather_data.append(updated_line)
            count += 1
    return weather_data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data != []:
        min_value = round(float(weather_data[0]),1)
        counter = -1
        for item in weather_data:
            counter +=1
            item_float = round(float(item),1)
            if min_value >= item_float:
                min_value = item_float
                start_value = counter
                item_in_type = item
        position_value = weather_data.index(item_in_type,start_value)    
        return (min_value, position_value)
    else:
        return () 
print(find_min([]))

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data != []:
        max_value = round(float(weather_data[0]),1)
        counter = -1
        for item in weather_data:
                counter +=1
                item_float = round(float(item),1)
                if max_value <= item_float:
                    max_value = item_float
                    start_value = counter
                    item_in_type = item
        position_value = weather_data.index(item_in_type,start_value)    
        return (max_value, position_value)
    else:
        return () 

print(find_max([]))


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    sum_min = 0
    sum_max = 0
    total_items = len(weather_data)
    min_value = (((weather_data[0][1])-32)*5)/9
    max_value = (((weather_data[0][2])-32)*5)/9
    min_date = weather_data[0][0]
    max_date = weather_data[0][0]

    for item in weather_data:
        date = item[0]
        min_temp = (((item[1])-32)*5)/9
        max_temp = (((item[2])-32)*5)/9
        sum_min += min_temp
        sum_max += max_temp
        if min_temp < min_value:
            min_value = min_temp            
            min_date = date
        if max_temp > max_value:
            max_value = max_temp
            max_date = date    
    min_mean = sum_min/total_items
    max_mean = sum_max/total_items
    min_date_in_format = datetime.fromisoformat(min_date)
    min_date_output = min_date_in_format.strftime("%A %d %B %Y")
    min_date_in_format = datetime.fromisoformat(max_date)
    max_date_in_format = datetime.fromisoformat(max_date)
    max_date_output = max_date_in_format.strftime("%A %d %B %Y")
    max_date_in_format = datetime.fromisoformat(max_date)
    output_line_1 = f"{total_items} Day Overview"
    output_line_2 = f" The lowest temperature will be {round(float(min_value),1)}{DEGREE_SYBMOL}, and will occur on {min_date_output}."
    output_line_3 = f" The highest temperature will be {round(float(max_value),1)}{DEGREE_SYBMOL}, and will occur on {max_date_output}."
    output_line_4 = f" The average low this week is {round(float(min_mean),1)}{DEGREE_SYBMOL}."
    output_line_5 = f" The average high this week is {round(float(max_mean),1)}{DEGREE_SYBMOL}."
    return f"{output_line_1}\n {output_line_2}\n {output_line_3}\n {output_line_4}\n {output_line_5}\n"


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #We want ---- Friday 02 July 2021 ----   Minimum Temperature: 9.4°C   Maximum Temperature: 19.4°C
    output_list = []
    for item in weather_data:
        min_value = round(float((((item[1])-32)*5)/9),1)
        max_value = round(float((((item[2])-32)*5)/9),1)
        date_in_format = datetime.fromisoformat(item[0])
        date_output = date_in_format.strftime("%A %d %B %Y")
        output_1 = f"---- {date_output} ----"
        output_2 = f"  Minimum Temperature: {min_value}{DEGREE_SYBMOL}"
        output_3 = f"  Maximum Temperature: {max_value}{DEGREE_SYBMOL}"
        output_list.append([output_1,output_2,output_3])
    result=""
    for day in output_list:

        for text in day:
            result+=text
            result+="\n"
        result+="\n"
    return result


