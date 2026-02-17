# csv_to_excel.py

import pandas as pd
import argparse
import logging
import os

def convert_csv_to_excel(input_file, output_file):
    try:
        logging.info("Reading CSV file...")
        df = pd.read_csv(input_file)

        # Handle missing values
        df.fillna("N/A", inplace=True)

        # Try to parse date columns automatically
        for col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                pass

        # Rename columns (example: make lowercase)
        df.columns = [col.strip().lower() for col in df.columns]

        # Save to Excel
        df.to_excel(output_file, index=False)
        logging.info("File successfully converted to Excel.")

    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV to Excel")
    parser.add_argument("input", help="Input CSV file path")
    parser.add_argument("output", help="Output Excel file path")

    args = parser.parse_args()

    logging.basicConfig(
        filename="conversion.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    if os.path.exists(args.input):
        convert_csv_to_excel(args.input, args.output)
    else:
        print("Input file does not exist.")