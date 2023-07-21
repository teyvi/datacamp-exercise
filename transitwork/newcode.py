#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 04:37:00 2023

@author: angelateyvi
"""

import gpxpy
import json

# Replace 'your_track.gpx' with the actual file path of your GPX track
gpx_file = 'routes-file.gpx'

# Read the GPX file
gpx = gpxpy.parse(open(gpx_file, 'r'))


# Extract latitude and longitude data from GPX track
latitude_list = [point.latitude for track in gpx.tracks for segment in track.segments for point in segment.points]
longitude_list = [point.longitude for track in gpx.tracks for segment in track.segments for point in segment.points]

# Create a list of (longitude, latitude) pairs
coordinates = [(lon, lat) for lat, lon in zip(latitude_list, longitude_list)]

# Create a GeoJSON linestring
linestring = {
    "type": "LineString",
    "coordinates": coordinates
}

# Calculate the bounding box (minimum and maximum latitude and longitude)
min_lon = min(longitude_list)
max_lon = max(longitude_list)
min_lat = min(latitude_list)
max_lat = max(latitude_list)

# Create the bounding box in Overpass Turbo format (South, West, North, East)
bbox = f"{min_lat},{min_lon},{max_lat},{max_lon}"

# Output the GeoJSON linestring and bounding box
linestring_json_str = json.dumps(linestring)
print("GeoJSON linestring:")
print(linestring_json_str)

print("\nOverpass Turbo bounding box:")
print(bbox)
