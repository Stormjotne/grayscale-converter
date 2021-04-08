import os
import grayscale_converter

root_folder = "EUVP"
copy_folder = "Carbon_copy"
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("{}".format(root_folder)):
    path = root.split(os.sep)
    #   print((len(path) - 1) * '---', os.path.basename(root))
    #   print(path)
    #   print(root)
    for file in files:
        # Split the extension from the path and normalise it to lowercase.
        if os.path.splitext(file)[-1].lower() == ".jpg":
            #   print(len(path) * '---', file)
            output = grayscale_converter.convert(root, copy_folder, file)
            print(output)
            '''print(file)
            print(os.path.join(root, file))
            print(os.path.join(copy_folder, root, file))'''
