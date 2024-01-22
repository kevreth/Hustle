import datetime
import pytz
import yaml

def generate_timestamp_gmt():
    gmt = pytz.timezone('GMT')
    now = datetime.datetime.now(tz=gmt)
    timestamp = now.strftime("%Y%m%d%H%M%S")
    return timestamp

# Example usage:
filename = generate_timestamp_gmt()[:8] + ".yml"
with open(filename, "w") as file:
    file.write("test")


def extract_and_write_daily_goals(input_file, output_file):
    # Load the YAML data from the input file
    with open(input_file, 'r') as file:
        data = yaml.safe_load(file)

    # Extract the goals.daily section
    daily_goals = data.get('goals', {}).get('daily', [])
    transformed_daily_goals = transform_leaf_nodes(daily_goals)

    # Create a new dictionary with the transformed daily goals
    extracted_data = {'goals': {'daily': transformed_daily_goals}}

    # Write the extracted data to the output file in YAML format
    with open(output_file, 'w') as file:
        yaml.dump(extracted_data, file)

def transform_leaf_nodes(data):
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = transform_leaf_nodes(value)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            data[i] = transform_leaf_nodes(item)
    else:
        data = {data: "none"}
    return data

# Input and output file paths
input_file = 'plan.yml'
output_file =  generate_timestamp_gmt()[:8] + ".yml"

# Call the function to extract and write daily goals
extract_and_write_daily_goals(input_file, output_file)

print(f'Daily goals extracted and saved to {output_file}')
