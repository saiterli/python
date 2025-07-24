import csv

def read_csv(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            print("Name\t\tAge")
            print("-------------------")
            for row in reader:
                print(f"{row['name']}\t\t{row['age']}")
    except FileNotFoundError:
        print("File not found. Please make sure 'data.csv' is in the same folder.")
    except Exception as e:
        print("Something went wrong:", e)

if __name__ == "__main__":
    read_csv('data.csv')
