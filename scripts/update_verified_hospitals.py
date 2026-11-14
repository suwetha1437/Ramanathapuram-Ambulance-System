import csv
from pathlib import Path

file_path = Path("data/processed/hospitals_map.csv")

verified = {
    "H003": {
        "latitude": "9.554880",
        "longitude": "78.575356",
        "emergency_available": "Yes",
    },
    "H005": {
        "latitude": "9.282768",
        "longitude": "79.312173",
        "emergency_available": "Yes",
    },
    "H009": {
        "latitude": "9.234683",
        "longitude": "78.786096",
    },
}

with file_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

for row in rows:
    hospital_id = row["hospital_id"]

    if hospital_id in verified:
        for column, value in verified[hospital_id].items():
            row[column] = value

with file_path.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Updated verified hospital coordinates.")
print("Updated hospitals:", ", ".join(verified.keys()))