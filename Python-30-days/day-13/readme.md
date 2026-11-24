1. JSON methods (import json)
Method	One-line explanation
json.load()	Reads JSON data from a file and converts it into a Python object.
json.loads()	Converts a JSON-formatted string into a Python object.
json.dump()	Writes a Python object into a JSON file.
json.dumps()	Converts a Python object into a JSON-formatted string.

Memory trick:
- load = File → Python
- loads = String → Python
- dump = Python → File
- dumps = Python → String
2. CSV methods (import csv)
Method	One-line explanation
csv.reader()	Reads CSV data row by row as lists.
csv.DictReader()	Reads CSV data row by row as dictionaries using column headers as keys.
csv.writer()	Creates a CSV writer that writes rows as lists.
csv.DictWriter()	Creates a CSV writer that writes rows as dictionaries using column headers as keys.
writer.writerow()	Writes a single row into a CSV file.
writer.writerows()	Writes multiple rows into a CSV file.
writer.writeheader()	Writes the column headers into a CSV file.

3. Important CSV file handling
Syntax	Purpose
open("file.csv", "r")	Opens a CSV file for reading.
open("file.csv", "w", newline="")	Opens a CSV file for writing and avoids unwanted blank lines on some platforms.
fieldnames=[...]	Defines the column names for DictWriter.
int(row["cpu"])	Converts a CSV string value into an integer.