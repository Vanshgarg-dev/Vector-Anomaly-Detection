"""
Utility script to inject synthetic anomalies into a credit card transaction CSV.

Randomly modifies a subset of rows to simulate anomalous behavior:
- Unusual Customer IDs (prefixed with 'ndi')
- Extreme transaction amounts (1M–3M)
- Unexpected category ('other')

Usage:
    python datalter.py
"""

import pandas as pd
import random

# Load the clean transaction dataset
file_path = 'credit_card_transaction_flow.csv'
df = pd.read_csv(file_path)

# Number of rows to inject anomalies into
num_rows_to_edit = 100

# Select random rows to modify
rows_to_edit = random.sample(range(len(df)), num_rows_to_edit)

# Inject anomalous values into selected rows
for i in rows_to_edit:
    df.at[i, 'Customer ID'] = 'ndi' + str(random.randint(1000, 9999))
    df.at[i, 'Transaction Amount'] = random.uniform(1_000_000, 3_000_000)
    df.at[i, 'Category'] = "other"

# Save the modified dataset
df.to_csv('updated_file.csv', index=False)

print(f"Injected {num_rows_to_edit} anomalous rows → updated_file.csv")
