# line_count

## Description

### Python Line Count Exercise

Write a Python program that takes a directory as a required argument and a filename extension as optional argument that defaults to “.txt”. The program should locate all files with the given extension in the given directory and all its subdirectories to produce a list of all matching files with the numbers of lines within the file. The program should also output the total number of lines and the average number of lines per file. For example:
```txt
./file1.txt 10
./file2.txt 25
./d1/d1fa.txt 5
./d1/d1fb.txt 37
===============
Number of files found: 4
Total number of lines: 77
Average lines per file: 19.25
```
Your solution should come with a README, suitable unit tests and should pass pylint.
Please make a git repository with your solution available at least two business days before the interview, so we have time to review it.

## Usage

Standerd:
```txt
python3 line_count.py directory_path 
```

Optional:
There are three filename extension (.txt, .docx, .pdf) can choose as optional argument.
```txt
python3 line_count.py directory_path .pdf
```

## Result

### Testing environment
Macbook Pro

Processor: 2.6 GHz 6-Core Intel Core i7

Memory: 16 GB 2667 MHz DDR4

Python Version: 3.96

### Unit tests
- Standerd & with optional argument
  <img width="931" alt="image" src="https://user-images.githubusercontent.com/15319203/192912318-68992da1-621b-410c-b568-35cb4bfbf313.png">

- Get not allow file extesion
  <img width="933" alt="image" src="https://user-images.githubusercontent.com/15319203/192912382-f82b8e75-4426-4fb1-8279-7bd571c704a5.png">

- Wrong directory
  <img width="922" alt="image" src="https://user-images.githubusercontent.com/15319203/192912441-8ac08f81-a275-4f49-9ef1-0610bec12cc8.png">

- File extension does not exist in the path
  <img width="989" alt="image" src="https://user-images.githubusercontent.com/15319203/192912631-3a720e5e-9645-4176-a93b-f573a2c35789.png">


### Pylint result
<img width="859" alt="image" src="https://user-images.githubusercontent.com/15319203/192911992-5f9bc43c-b8cb-4b19-9184-69ff971fcc69.png">



