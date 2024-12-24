import pandas as pd

# Load your data (replace 'transactions.csv' with your file)
df = pd.read_csv(r"D:\transactions.csv")

# Clean the description column (convert to uppercase)
df['Description'] = df['Description'].str.upper().str.strip()

# Extract the text between the first two dashes after "UPI-" (convert to uppercase)
df['Category'] = df['Description'].str.extract(r'UPI-(.*?)-', expand=False)

# Group transactions by category and count occurrences
grouped_df = df.groupby('Category').size().reset_index(name='Count')

# Print or save the grouped results
print(grouped_df)

# Save the grouped results to the specified path
grouped_df.to_csv(r"D:\transactions_result.csv", index=False)
