import PyPDF2
import sys

def merge(input,output):
    merger = PyPDF2.PdfFileMerger();
    try:
        for pdf in pdf_files:
            merger.append(pdf)
        merger.write(newPDF)
        merger.close()
    except:
        print("An error has occured try again")
        exit(1)


if __name__ == "__main__":
    size = len(sys.argv)
    """
    Checks if the user gave at least 2 pdfs to merge
    if not it prints an error, displays the
    correct form and exits
    """
    if size < 4:
        print("Unsupported format")
        print("Correct syntax: python pdfmerger.py file1.pdf file2.pdf ... fileN.pdf OutputName.pdf")
        exit(1)
    newPDF = sys.argv[size-1]
    pdf_files = sys.argv[1:size-1]
    print("Pdf merging is about to start")
    
    merge(pdf_files,newPDF)

    exit_text = newPDF + " has been successfully saved!"
    print(exit_text)
    exit(0)