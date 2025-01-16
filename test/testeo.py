import os
import time

def create_daily_output_folder():
    current_date = time.localtime()
    year = current_date[0]
    month = current_date[1]
    day = current_date[2]

    daily_output_folder = f"{day}_{month}_{year}"

    daily_output_path = f'.\screenshots\{daily_output_folder}'
    if not os.path.exists(daily_output_path):
        print("Creatin daily output path....")
        os.makedirs(daily_output_path)
        print("!Daily output path created¡")
    else:
        print("Output already exist.")
    return daily_output_path

print(create_daily_output_folder())

# def set_capture_name():
#     current_date = time.localtime()
#     hour = current_date[3]
#     minute = current_date[4]
#     second = current_date[5]

#     capture_name = f"id_content_{hour}_{minute}_{second}"

#     return capture_name