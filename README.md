# WELCOME TO TESTCASE FOR DSA ASSIGNMENT

## Introduction

<div>
<h1> Viet Nam National University 
<h2> Ho Chi Minh City University of Technology
<h3> Faculty of Computer Science and Engineering
<h4> Data Structure and Algorithm - HK241
<h5> First Author: Nguyen Phuc Nhan
</div>

- Version v0.1 : Test Array List Method

## How to?

### Set up
Place the files in the same directory as your project.

* Example for folder's structure

Assume you extract the root folder from LMS, then go to dsastudents like this:

> dsastudents
```
$ tree -L 2
.
|-- include
|   |-- ann
|   |-- list
|   |-- util
|   |-- xflens
|   |-- xtensor     
|   |-- xtensor-blas
|   `-- xtl
|-- main.cpp        
|-- src
|   `-- ann
```

Then, place all file here into ./dsastudents:

```
$ tree -L 2
.   
|-- TestLog
|   |-- Array
|   `-- DLinkedList
|-- array_list_test.cpp 
|-- doubly_linked_list_test.cpp
|-- include
|   |-- ann
|   |-- list
|   |-- util
|   |-- xflens
|   |-- xtensor     
|   |-- xtensor-blas
|   `-- xtl
|-- main.cpp        
|-- src
|   `-- ann

18 directories, 7 files
```

### Run Test
Now, run this command in the terminal to compile the code into an executable file:

Notes: Please come to `dsastudents` directory before run test

<h6>To compile</h6>
```
g++ -o <your_exe> -Isrc -Iinclude -std=c++17 -g <file_need_to_be_run>.cpp
```
<h6>To run</h6>

> For Linux
```
./your_exe [OPTION] [OTHERs (optional)]
```

> For Window
```
your_exe.exe [OPTION] [OTHERs (optional)]
```

OPTIONS:
  - ?help: To print usage
  - !demo: Run demo from original source
  - !test: Run all test
  - !test num_of_test: Run test numth
  - !test num_start_test num_end_test: Run from <start> test to <end> test

![Check it](usage.png)

### Check your result with mine
All result in TestLog

## What next?
- Dataset and DataLoader
- Class Layers and functions for MLP and xtensor_lib

## Contributing
- Create an issue if you encounter a problem.
- Send a pull request (to generate tests or fix test cases).

## Connect

[![Github](https://img.shields.io/badge/Github-nhan2892005-Black?logo=github)](https://github.com/nhan2892005)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Phuc_Nhan_Nguyen-blue?logo=linkedin)](https://www.linkedin.com/in/phuc-nhan-nguyen/)

[![Facebook](https://img.shields.io/badge/Facebook-Phúc_Nhân-blue?logo=facebook)](https://www.facebook.com/phucnhancshcmut/)

[![LeetCode](https://img.shields.io/badge/LeetCode-N289-orange?logo=leetcode)](https://leetcode.com/u/N289/)

[![CodinGame](https://img.shields.io/badge/CodinGame-nhan__289-yellow?logo=codingame)](https://www.codingame.com/profile/3f88b771e04c6894b7485decd4291a7e8589985)

[![Email](https://img.shields.io/badge/Email-nhan.nguyen2005phuyen@hcmut.edu.vn-green?logo=gmail)](nhan.nguyen2005phuyen@hcmut.edu.vn)

[![Website](https://img.shields.io/badge/Website-Visit-blue?logo=globe)](https://phucnhan289.great-site.net/1/Ph%C3%BAc-Nh%C3%A2n.html)

## Bonus: How to check memory leaks

Prerequisite: Linux, MacOs, Solaris, FreeBSD or WSL

- Step 1: install valgrind
  
 Check Here: `https://valgrind.org/docs/manual/dist.readme.html`
 or : `https://stackoverflow.com/questions/24935217/how-to-install-valgrind-properly`

- Step 2: after compile your source into <your_exe_file>
  
  ```
    valgrind \
    --leak-check=full \
    --show-leak-kinds=all \
    --track-origins=yes \
    --verbose \
    --log-file=<path_to_your_log_file> \
    <your_exe_file> <arg of your program (optional)>
  ```

- Step 3: check log file