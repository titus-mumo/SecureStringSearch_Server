import time

def search_algorithm_1(file_path, search_string):
    start_time = time.time()
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip() == search_string:
                return "STRING EXISTS", time.time() - start_time
    return "STRING NOT FOUND", time.time() - start_time

# Add more search algorithms here
