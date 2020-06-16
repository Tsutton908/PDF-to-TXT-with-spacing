from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal

def parsedocument(document):
    # convert all horizontal text into a list of lines
    lines = []
    rsrcmgr = PDFResourceManager()
    #convert the pdf, neglecting whitespace, and allowing single space between words
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            for element in layout:
                if isinstance(element, LTTextBoxHorizontal):
                    lines.extend(element.get_text().splitlines())
    return lines

#make sure it works with an example pdf file
pdf_file_obj = open("sample.pdf","rb")
pdf_reader = parsedocument(pdf_file_obj)
string = str(pdf_reader).strip("[]")

print("Here are the contents of your pdf file:")
print(string)

#saves the contents to a created txt file
#add directory wanted to save to
file1 = open(r"C:\files_txt\\test.txt","a")
file1.writelines( "%s\n" % item for item in pdf_reader )
file1.close()
