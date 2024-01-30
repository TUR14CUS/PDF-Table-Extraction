# PDF Table Extraction and Export Readme

This Python script leverages the `camelot` library to extract tables from a PDF file, exporting the data into CSV files. The script provides flexibility for the user to specify the PDF file path, the page number to extract, and the extraction flavor. Here's a guide on understanding and using the script.

## Table of Contents
1. [Features](#features)
2. [Usage Instructions](#usage-instructions)
3. [Prerequisites](#prerequisites)
4. [Configuration](#configuration)
5. [Review the Output](#review-the-output)
6. [Adjustments](#adjustments)
7. [Notes](#notes)
8. [License](#license)

## Features:

1. **PDF Table Extraction:**
   - Utilizes `camelot` to extract tables from a PDF file.

2. **CSV Export:**
   - Exports all tables to a CSV file named `<PDF_filename>_all_tables.csv`.
   - Exports the first table to a separate CSV file named `<PDF_filename>_table_1.csv`.

3. **Informative Output:**
   - Displays the number of tables detected in the PDF.
   - Provides informative messages for successful operations.

4. **User Inputs:**
   - Prompts the user for the PDF file path, page number to extract (default is '1'), and extraction flavor (default is 'lattice').

5. **Error Handling:**
   - Handles potential errors during PDF reading and exporting, providing descriptive error messages.

## Usage Instructions:

1. **Prerequisites:**
   - Ensure you have the `camelot` library installed using:
     ```bash
     pip install camelot-py[cv]
     ```
   - Install any additional dependencies mentioned in the `camelot` documentation if needed.

2. **Configuration:**
   - Run the script using a Python interpreter.
   - Input the full path to the PDF file when prompted.
   - Optionally, specify the page number to extract (default is '1') and the extraction flavor (default is 'lattice').

3. **Review the Output:**
   - The script will generate CSV files in the same directory as the PDF file.
   - Review the console output for informative messages and any potential errors.

4. **Adjustments:**
   - Customize the script based on your specific requirements.
   - Experiment with different extraction flavors supported by `camelot` based on the structure of the PDF.

5. **Notes:**
   - Ensure that you have the required dependencies installed.
   - Use responsibly and in compliance with the terms of service of the PDF source.

## License
This project is licensed under the [MIT License](LICENSE).
