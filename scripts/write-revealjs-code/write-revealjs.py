import os
from natsort import os_sorted
path= "C:/Users/Venu/Documents/GitHub/venugvgk.github.io/books/own-picture-books/treekar-shomus"
file_names = os_sorted(os.listdir(path))
print(file_names)
f = open("reveal.txt", "w")
for name in file_names:
    f = open("reveal.txt", "a")
    f.write("\n##\n\n![]" + name + "\n")
f.close()

