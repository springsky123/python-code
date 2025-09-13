import csv

def merge_csv_files(input_filenames, output_filename):
    """
    Merges multiple CSV files into a single CSV file.

    Args:
        input_filenames (list): A list of strings, where each string is the
                                filename of a CSV file to be merged.
        output_filename (str): The filename for the combined CSV output.
    """
    if not input_filenames:
        print("No input files provided.")
        return

    with open(output_filename, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        header_written = False

        for filename in input_filenames:
            try:
                with open(filename, 'r', newline='') as infile:
                    reader = csv.reader(infile)

                    # Read header
                    header = next(reader)

                    # Write header only once
                    if not header_written:
                        writer.writerow(header)
                        header_written = True

                    # Write remaining rows
                    for row in reader:
                        writer.writerow(row)
            except FileNotFoundError:
                print(f"Warning: File '{filename}' not found. Skipping.")
            except Exception as e:
                print(f"Error processing file '{filename}': {e}")

    print(f"Merged CSV files into '{output_filename}' successfully.")

if __name__ == "__main__":
    input_files = ["file1.csv", "file2.csv", "file3.csv"]
    output_file = "merged_output.csv"
    merge_csv_files(input_files, output_file)

