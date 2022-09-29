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
python3 line_count.py /Users/hsiaotinghuang/Desktop/OA_Analog_Devices/Test 
```

Optional:
There are three filename extension (.txt, .docx, .pdf) can choose as optional argument.
```txt
python3 line_count.py /Users/hsiaotinghuang/Desktop/OA_Analog_Devices/Test .pdf
```

## Result

### Testing environment
Macbook Pro
Processor 2.6 GHz 6-Core Intel Core i7
Memory 16 GB 2667 MHz DDR4

### Unit tests
- Standerd & with optional argument
![image](https://user-images.githubusercontent.com/15319203/192910189-fc6a55ec-c00a-449a-bb4f-40c98103ef3b.png)
- Get not allow file extesion
![image](https://user-images.githubusercontent.com/15319203/192910218-46ebf072-57d4-47fc-9e31-df84ec3bd8ba.png)
- Wrong directory
![image](https://user-images.githubusercontent.com/15319203/192910286-b3718d92-666f-4334-a444-191155b453a8.png)
- File extension does not exist
![image](https://user-images.githubusercontent.com/15319203/192910003-8f51a499-1289-48b2-97aa-89e3bfba8b25.png)

### Pylint result
![image](https://user-images.githubusercontent.com/15319203/192910513-bc80e14f-d57e-4eaa-b399-4c209e01a84c.png)


