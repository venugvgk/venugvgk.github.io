import PyPDF2
import os
from natsort import os_sorted

# Create a PdfFileMerger object
merger = PyPDF2.PdfMerger()

# List of PDF files to merge
path = "C:/Users/Venu/Documents/GitHub/venugvgk.github.io/scripts/pdfmerge/to-merge/"
file_names = os_sorted(os.listdir(path))
paths_files = [os.path.join(path, x) for x in file_names if x.lower().endswith('.pdf')]
print(paths_files)

# Append each PDF to the merger
for pdf in paths_files:
    merger.append(pdf)

# Write out the merged PDF
output_path = os.path.join(path, "merged.pdf")
merger.write(output_path)
merger.close()
