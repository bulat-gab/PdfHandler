import os
from pypdf import PageObject, PdfReader, PdfWriter
import sys


def get_new_file_name(old_name: str) -> str:
    if not old_name:
        print("Error: old name is empty")
        sys.exit()

    postfix = "Updated"
    
    name, ext = os.path.splitext(old_name)
    new_name = f"{name}.{postfix}{ext}"
    return new_name

def ensure_file_does_not_exist(name: str):
    if os.path.exists(name):
        print(f"File with name {name} already exists. Please delete it first.")
        sys.exit()

def extract_pages(pdf_path: str) -> list[PageObject]:
    pdf_reader = PdfReader(pdf_path)
    pages = pdf_reader.pages
    print(f"Document has {len(pages)} pages.")
    return pages

def write_page_to_file(pages: list[PageObject], output_file):
    print("Extracting the first page...")
    first_page = pages[0]

    pdf_writer = PdfWriter()
    pdf_writer.add_page(first_page)
    pdf_writer.write(output_file)

def main():
    args = sys.argv
    if len(args) <= 1:
        print("Please provide pdf file name (path)")
        return
    if len(args) > 2:
        print("Too many arguments")
        return

    try:
        pdf_path = args[1]

        pages = extract_pages(pdf_path)
        if len(pages) == 1:
            print("Document has only one page. Exiting...")
            sys.exit()

        output_file = get_new_file_name(pdf_path)
        ensure_file_does_not_exist(output_file)
        write_page_to_file(pages, output_file)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()