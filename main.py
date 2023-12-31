import requests
import fitz

def download_pdf(url, file_name):
    response = requests.get(url)
    with open(file_name, 'wb') as pdf_file:
        pdf_file.write(response.content)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    doc.close()
    return text

def extract_images_from_pdf(pdf_path, image_folder):
    doc = fitz.open(pdf_path)
    for page_num in range(doc.page_count):
        page = doc[page_num]
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            with open(f"{image_folder}/page{page_num+1}_img{img_index+1}.png", "wb") as img_file:
                img_file.write(base_image["image"])

    doc.close()


pdf_url = "Mention the URL from where PDF file needs to be downloaded"
pdf_path = "Mention the path where the downloaded PDF file needs to be saved"
image_folder = "Mention the path where the downloaded PDF file needs to be saved"

download_pdf(pdf_url, pdf_path)
text = extract_text_from_pdf(pdf_path)
print(text)

extract_images_from_pdf(pdf_path, image_folder)
