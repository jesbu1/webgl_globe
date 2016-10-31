import csv, json, random
data = csv.reader(open("Impacts.csv"))
locations = []
false_data = ['-', '-1', 'Lat', 'Lon', 'Diameter']
for lat, lon, diameter in data:
    if lat not in false_data and lon not in false_data and diameter not in false_data:
        locations += (lat, lon, diameter)
output = [["Diameters", locations]]
print(json.dumps(output))
