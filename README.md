![Chickn Legs Logo](https://www.chicknlegs.com/cdn/shop/files/Logo_Yellow_122_C_Black_Name_TM_c810b369-e4a8-482f-85bc-577f20140603.png?v=1659964521)
# StoreLocatorDataFormatter
This is the public tool for ChicknLegs to convert their private store data to a usable json format with latitude and longitude.

## Step 1. Fill in path to data and API key.
On line 7, copy the path to the data you've downloaded from the drive. The data should be under "Retail Locations for Google Maps". Download it as a .csv.

Then on line 10, paste the Google Maps JavaScript API key into the blank. You can find the API Key at the top of assets/storeLatLon.json.

## Step 2. Run it.
Run it! It should take a minute for the geolocater to run. 

## Step 3. Upload storeLatLon.json to Shopify.
Upload it under the assets tab. It should replace the current version. Make sure not to delete the comment at the top. If you do- the API key can be found in sections/map_with_store_locations.liquid.
