import csv
from pathlib import Path

input_file = Path("data/raw/hospitals.csv")
output_file = Path("data/processed/hospitals_map.csv")

new_columns = [
    "latitude",
    "longitude",
    "google_maps_url",
    "emergency_available",
    "icu_available",
    "bed_capacity",
]

with input_file.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    original_columns = reader.fieldnames

all_columns = original_columns + [
    column for column in new_columns
    if column not in original_columns
]

for row in rows:
    for column in new_columns:
        if column not in row:
            row[column] = ""

with output_file.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=all_columns)
    writer.writeheader()
    writer.writerows(rows)

print("Created:", output_file)
print("Total hospitals:", len(rows))
print("Columns:", all_columns)