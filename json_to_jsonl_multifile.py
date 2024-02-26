'''
Merges multiple JSON files into one.,
'''

import os
import json
import shutil
import jq
import queue
import concurrent.futures


def process_json(file_path):
    '''Reads one file at a time, accepts the path to the file.'''

    with open(file_path, 'r') as file:

        # Loads the JSON content
        data = json.load(file)

        # Strips the outer array and returns it as JSONL
        payload = jq.compile(".[]").input_value(data).text()
        return payload


def merge_results(results, output_file):
    '''Reduce part of the Map and Reduce process.'''

    with open(output_file, 'w') as outfile:

        # Loops the returned JSONL fragments and merges into one
        for result in results:
            outfile.writelines(result)


def move_files(files, destination_folder):
    '''Moves the processed file to another folder'''

    for file_path in files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(file_path, destination_path)
        print(f"Moved {file_path} to {destination_path}")


def process_json_files(folder_path, output_file):
    '''Using multiple threads processes all files in a folder path.'''

    # Constructs a list of JSON files
    input_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.json')]

    # Creates a queue for the results
    result_queue = queue.Queue()

    # Runs separate threads one for each file
    with concurrent.futures.ThreadPoolExecutor() as executor:

        # Calls the process_json function with each file
        future_to_file = {executor.submit(process_json, file): file for file in input_files}

        # Processes the files
        for future in concurrent.futures.as_completed(future_to_file):
            file = future_to_file[future]
            try:
                result = future.result()
                result_queue.put(result)
            except Exception as exc:
                print(f'Error processing {file}: {exc}')

    # Stores the returned payloads into an array
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    # Calls the function to merge results
    merge_results(results, output_file)

    # Removes the files if processed, so it woon't be read again next time
    move_files(input_files, destination_folder)


if __name__ == "__main__":
    '''Hey guess what? I'm the main module.'''

    folder_path = "./multi_json/"
    destination_folder = "./multi_json/processed/"
    output_file = "merged_output.json"
    process_json_files(folder_path, output_file)
