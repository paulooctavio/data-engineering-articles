def main():
    # Simulate a simple ETL process
    data = extract_data()
    transformed_data = transform_data(data)
    result = load_data(transformed_data)
    return result

def extract_data():
    # Simulate data extraction
    return [1, 2, 3, 4, 5]

def transform_data(data):
    # Simulate data transformation
    return [x * 2 for x in data]

def load_data(data):
    # Simulate loading data
    # Here, we just return True to indicate success
    print(f"Loaded data: {data}")
    return True

if __name__ == "__main__":
    main()
