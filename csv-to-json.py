import csv
import json
import sys

def csv_to_json(csv_file_path):
    json_data = []

    # Read CSV file and add data to a list
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            json_data.append(row)

    return json_data

def write_json(json_data, json_file_path):
    with open(json_file_path, 'w', encoding='utf-8-sig') as file:
        json.dump(json_data, file, indent=4)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_csv_file>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    json_file_path = csv_file_path.rsplit('.', 1)[0] + '.json'

    json_data = csv_to_json(csv_file_path)
    write_json(json_data, json_file_path)

    print(f"CSV data has been converted to JSON and saved as '{json_file_path}'.")

if __name__ == "__main__":
    main()
