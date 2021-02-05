import os
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


#建立convert函數
#output:管理處理後的輸出
#manager:是一個pdf資源管理器，目的是為了儲存共享資源
#converter:主要處理轉換的地方
#interpreter:創建一個pdf解析器
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, codec='utf-8', laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


def convertMultiple(pdfDir, txtDir):
    #iterate through pdfs in pdf directory
    for pdf in os.listdir(pdfDir): 
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            #get string of text content of pdf
            text = convert(pdfFilename) 
            textFilename = txtDir + pdf[:-4] + ".txt"
            #make text file
            textFile = open(textFilename, "w",encoding='utf-8') 
            #write text to text file
            textFile.write(text) 
            textFile.close()
            print("finish convert to txt", pdf)
    print("finish convert all file")
    
# =============================================================================
# for pdf in os.listdir(pdfDir): 
#     fileExtension = pdf.split(".")[-1]
#     if fileExtension == "pdf":
#         pdfFilename = pdfDir + pdf
# =============================================================================
            
pdfdir='F:/電子化企業期末報告 - 複製/covid19/'
textdir='F:/電子化企業期末報告 - 複製/covid19/test/'
convertMultiple(pdfdir,textdir)
