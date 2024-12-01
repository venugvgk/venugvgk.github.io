import PyPDF2
import os

# Create a PdfFileMerger object
merger = PyPDF2.PdfMerger()

# List of PDF files to merge
path = "C:/Users/Venu/Documents/GitHub/venugvgk.github.io/scripts/pdfmerge/to-merge/"
file_names = os.listdir(path)
string = "to-merge/"
paths_files = [string + x for x in file_names]
print(paths_files)

# Append each PDF to the merger
for pdf in paths_files:
    merger.append(pdf)

# Write out the merged PDF
merger.write("result.pdf")
merger.close()
