import pandas as pd

# Assuming your input CSV file is named 'your_input_file.csv'
input_file_path = 'human_main.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file_path)

# Calculate the variance row-wise
row_variances = df.iloc[:, 1:].var(axis=1)  # Assuming the numeric data starts from the second column

# Create a new DataFrame with 'Gene Symbol' and row-wise variances
result_df = pd.DataFrame({'Gene Symbol': df['Gene Symbol'], 'Variance': row_variances})

# Save the result to a new CSV file named 'new.csv'
output_file_path = 'final_human_var.csv'
result_df.to_csv(output_file_path, index=False)

# Display a message indicating the process is completed
print(f"Row-wise variances saved to {output_file_path}")

