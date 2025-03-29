"""
Script to Extract Phone Numbers from a PDF via a Hidden Google Drive Link in a CSV.

Steps:
1. Read a CSV file (`find_the_link.csv`) that contains a hidden Google Drive link.
2. Extract the link by traversing the CSV diagonally.
3. Use regex to extract the file ID from the Google Drive URL.
4. Download the corresponding PDF file using `gdown`.
   - If the download fails, use a fallback temporary PDF file (`temp.Downloaded_PhoneNumbers.pdf`).
5. Open and read the PDF using `PyPDF2`.
6. Search for phone numbers in the format `XXX.XXX.XXXX` using regex.
7. Print all extracted phone numbers along with relevant messages.
8. Handle errors for missing files and failed downloads gracefully.

Note:
- If the Google Drive download fails, ensure that the PDF is manually placed as `temp.Downloaded_PhoneNumbers.pdf` in the script directory.
"""

import csv
import PyPDF2
import re
import gdown

print("Starting the process...")

# Open the CSV file containing a hidden Google Drive link
csv_file_path = './find_the_link.csv'
print(f"Attempting to read CSV file: {csv_file_path}")

try:
    with open(csv_file_path, encoding='utf-8') as data:
        csv_data = csv.reader(data)
        data_lines = list(csv_data)
    print("CSV file read successfully.")
except FileNotFoundError:
    print(f"Error: CSV file '{csv_file_path}' not found.")
    exit()

# Extract the Google Drive link by traversing diagonally
print("Extracting Google Drive link from CSV...")
googleDriveLink = ''
i = 0
while i < len(data_lines):
    googleDriveLink += str(data_lines[i][i])
    i += 1

print(f"Extracted Google Drive Link: {googleDriveLink}")

# Extract the file ID from the Google Drive URL using regex
match = re.search(r"id=([\w-]+)", googleDriveLink)
file_id = match.group(1) if match else None

# Define output PDF file name
pdf_file_name = "Downloaded_PhoneNumbers.pdf"
fallback_pdf_file_name = f"temp.{pdf_file_name}"  # Used if download fails

# Download the PDF file from Google Drive
if file_id:
    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Downloading PDF from: {url}")
    try:
        gdown.download(url, pdf_file_name, quiet=False)
        print("PDF downloaded successfully.")
    except Exception as e:
        print(f"Download failed: {e}")
        print(f"Using existing file: {fallback_pdf_file_name}")
        pdf_file_name = fallback_pdf_file_name
else:
    print("No valid Google Drive file ID found! Please download the file manually.")
    pdf_file_name = fallback_pdf_file_name

# Open and read the PDF (fallback if download failed)
print(f"Attempting to open PDF file: {pdf_file_name}")
try:
    with open(pdf_file_name, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        total_pages = len(pdf_reader.pages)

        # Define regex pattern to find phone numbers
        pattern = r'\d{3}.\d{3}.\d{4}'
        print("Extracting phone numbers from the PDF...")

        # Loop through pages to extract phone numbers
        for page_number in range(total_pages):
            current_page = pdf_reader.pages[page_number]
            current_page_text = current_page.extract_text()
            
            # Search for phone numbers using regex
            for match in re.finditer(pattern, current_page_text):
                print(f"The extracted Phone number is: {match.group()}")

except FileNotFoundError:
    print(f"Error: The file '{pdf_file_name}' was not found.")
