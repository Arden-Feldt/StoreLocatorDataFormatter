from geopy.geocoders import GoogleV3
import pandas as pd
import csv
import json

# TODO: Add the path to your store info csv.
address_csv = pd.read_csv(r"Path_to_your_data")

# TODO: Initialize the geocoder
geolocator = GoogleV3(api_key="Your_API_Key")

# Function to get coordinates for each address
def get_coordinates(address):
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Apply function to each address and create new columns for Latitude and Longitude
address_csv['Latitude'], address_csv['Longitude'] = zip(*address_csv['Address'].apply(get_coordinates))

# Save the results back to a CSV, including the new columns along with the original data
address_csv.to_csv("addresses_with_coordinates.csv", index=False)


def convert_csv_to_json_format(csv_filename):
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        output = []
        for row in reader:
            # Create a dictionary with all columns from the CSV
            output.append({
                "company": row['Company'],
                "address": row['Address'],
                "phone": row['Phone'],
                "email": row['Email'],
                "latitude": float(row['Latitude']),
                "longitude": float(row['Longitude'])
            })
    
    return output

# Example usage
output = convert_csv_to_json_format("addresses_with_coordinates.csv")

# Save the output to a JSON file
json_filename = "storeLatLon.json"
with open(json_filename, "w") as json_file:
    json.dump(output, json_file, indent=4)

print(f"Data has been saved to {json_filename}")


