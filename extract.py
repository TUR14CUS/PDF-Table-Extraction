import camelot

def read_and_export_pdf(pdf_path, page='1', flavor='lattice'):
    try:
        # Read PDF
        tables = camelot.read_pdf(pdf_path, pages=page, flavor=flavor)
        print(f"Number of tables detected in PDF: {len(tables)}")

        if len(tables) > 0:
            # Export to CSV
            csv_path = pdf_path.replace('.pdf', '_all_tables.csv')
            tables.export(csv_path, f='csv', compress=True)
            print(f"All tables exported to CSV: {csv_path}")

            # Export the first table to CSV
            first_table_csv_path = pdf_path.replace('.pdf', '_table_1.csv')
            tables[0].to_csv(first_table_csv_path)
            print(f"First table exported to CSV: {first_table_csv_path}")

            # Print the first table as a DataFrame
            print(f"\nFirst Table as DataFrame:\n{tables[0].df}")

        else:
            print("No tables found in the specified PDF.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        # User Inputs
        PDF_PATH = input("Enter the full path to the PDF file: ").strip()
        PAGE_NUMBER = input("Enter the page number to extract (default is '1'): ") or '1'
        FLAVOR = input("Enter the flavor (default is 'lattice'): ") or 'lattice'

        # Read and export PDF
        read_and_export_pdf(PDF_PATH, PAGE_NUMBER, FLAVOR)

    except Exception as ex:
        print(f"An unexpected error occurred: {str(ex)}")
