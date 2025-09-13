import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

file_path = "E:\\Unemployment Analysis\\Unemployment in India.csv"  # change path if needed

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert Date column if present
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Dataset info
    buffer = io.StringIO()
    df.info(buf=buffer)
    print("Dataset Info:\n", buffer.getvalue())

    # First rows
    print("\nFirst Five Rows:\n", df.head())

    # Missing values
    print("\nMissing Values:\n", df.isnull().sum())

    # Summary statistics
    print("\nSummary Statistics:\n", df.describe())

    # Visualization 1: Unemployment Rate Over Time
    if 'Date' in df.columns and 'Estimated Unemployment Rate (%)' in df.columns:
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=df)
        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Unemployment Rate (%)')
        plt.title('Unemployment Rate Over Time')
        plt.show()

    # Visualization 2: Distribution of Unemployment Rate
    if 'Estimated Unemployment Rate (%)' in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(df['Estimated Unemployment Rate (%)'].dropna(), bins=20, kde=True)
        plt.title('Distribution of Unemployment Rate')
        plt.xlabel('Unemployment Rate (%)')
        plt.ylabel('Frequency')
        plt.show()

    # Visualization 3: Unemployment by Region
    if 'Region' in df.columns:
        plt.figure(figsize=(15, 6))
        sns.barplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)
        plt.xticks(rotation=90)
        plt.title('Unemployment Rate by Region')
        plt.xlabel('Region')
        plt.ylabel('Unemployment Rate (%)')
        plt.show()

else:
    print(f"Error: File '{file_path}' not found.")
