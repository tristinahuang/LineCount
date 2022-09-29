"""
Author: Hsiao-Ting Huang (hthuang@uw.edu)

Question:
Write a Python program that takes a directory as a required argument and a filename extension
as optional argument that defaults to “.txt”. The program should locate all files with the given
extension in the given directory and all its subdirectories to produce a list of all matching files
with the numbers of lines within the file. The program should also output the total number of
lines and the average number of lines per file. For example:

./file1.txt 10
./file2.txt 25
./d1/d1fa.txt 5
./d1/d1fb.txt 37
===============
Number of files found: 4
Total number of lines: 77
Average lines per file: 19.25

Your solution should come with a README, suitable unit tests and should pass pylint.
Please make a git repository with your solution available at least two business days before the
interview, so we have time to review it.

"""
import os
import sys
import docx
from PyPDF2 import PdfFileReader

class LineCount:
    '''Get the files information from input directory path.'''

    def __init__(self):
        self.file_path = []
        self.file_info = []
        self.line_count = 0
        self.directory = ""
        self.filename_extension = ""
        self.allow_extension = ['.txt','.pdf','.docx']


    def set_file_path(self, argv_list, argv_len):
        '''Get all the .txt files in the dictionary'''
        exist = allow = False

        self.directory = argv_list[1]
        if argv_len == 3:
            self.filename_extension = argv_list[2]
        else:
            self.filename_extension = '.txt'

        if self.filename_extension in self.allow_extension:
            allow = True

        if os.path.exists(self.directory):
            for root, __, files in os.walk(self.directory):
                for file in files:
                    if file.endswith(self.filename_extension):
                        self.file_path.append(os.path.join(root, file))
                        exist = True
            if not exist:
                print(f'Extension {self.filename_extension} does not exist in the directory.')
            if not allow:
                print(f'System does not support extension {self.filename_extension}. \
                    Only support .txt, .docx, .pdf.')
        else:
            print(f'Input Path: {self.directory} does not exist.')

        return exist and allow

    def get_file_info(self):
        '''Get the number of lines in within the files'''
        for path in self.file_path:

            if self.filename_extension == ".txt":
                with open(path, 'r', encoding="utf8") as f_p:
                    lines = len(f_p.readlines())
            elif self.filename_extension == ".docx":
                doc = docx.Document(path)
                lines = len(doc.paragraphs)
            elif self.filename_extension == ".pdf":
                with open(path, 'rb') as f_p:
                    pdf_reader = PdfFileReader(f_p)
                    for page in pdf_reader.pages:
                        lines = len(page.extractText().splitlines())
            relative_path = path.replace(self.directory, '.')
            self.file_info.append(f'{relative_path} {lines}')
            self.line_count += lines

    def print_file_info(self):
        '''Print the files infromation'''
        print("===== FILE INFO ==========")
        for info in self.file_info:
            print(info)
        print("==========================")
        print("Number of files found:", len(self.file_info))
        print("Total number of lines:", self.line_count)
        print("Average lines per file:", self.line_count/len(self.file_info))



if __name__=="__main__":

    if len(sys.argv) <= 1 or len(sys.argv) > 3:
        print("ERROE: Please check your input!")
        print("Usage:python3 OA.py absolute_directory_path filename_extension(optional)")
    else:
        g = LineCount()

        # check the file extension exist and is allowed
        if g.set_file_path(argv_list = sys.argv, argv_len = len(sys.argv)):
            g.get_file_info()
            g.print_file_info()
