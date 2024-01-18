import pandas as pd

# Assuming your input CSV file is named 'your_input_file.csv'
input_file_path = 'rat_main.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file_path)

# Transpose the DataFrame
transposed_df = df.transpose()

# Save the transposed DataFrame to a new CSV file named 'transposed_output.csv'
output_file_path = 'transposed_rat.csv'
transposed_df.to_csv(output_file_path, header=False)  # Avoid writing column names as headers

# Display a message indicating the process is completed
print(f"Transposed data saved to {output_file_path}")

