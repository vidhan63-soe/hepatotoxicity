import os
import zipfile

def extract_and_move_zip_files(input_directory=".", output_directory="."):
    zipped_files_directory = os.path.join(output_directory, "zipped_files")
    os.makedirs(zipped_files_directory, exist_ok=True)

    for file in os.listdir(input_directory):
        if file.endswith(".zip"):
            zip_file_path = os.path.join(input_directory, file)

            # Check if the file is a valid zip file before extraction
            if zipfile.is_zipfile(zip_file_path):
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    # Extract contents directly into the output directory
                    zip_ref.extractall(output_directory)

                print(f"Extracted: {zip_file_path} to {output_directory}")

                # Move the original zip file to another directory
                moved_zip_path = os.path.join(zipped_files_directory, file)
                os.rename(zip_file_path, moved_zip_path)
                print(f"Moved: {zip_file_path} to {moved_zip_path}")
            else:
                print(f"Skipping: {zip_file_path} (Not a valid zip file)")

if __name__ == "__main__":
    # Get the script's directory as the base directory
    base_directory = os.path.dirname(os.path.abspath(__file__))

    # Replace with your actual input and output directories
    input_directory = os.path.join(base_directory, 'DB_1')
    output_directory = os.path.join(base_directory, 'Unzipped')

    extract_and_move_zip_files(input_directory, output_directory)
