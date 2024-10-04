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
├── TestLog
│   ├── Array
│   ├── DLinkedList
│   ├── DataSetAndLoader
│   ├── FCLayer
│   ├── ReLU
│   └── Softmax
├── include
│   ├── ann
│   ├── list
│   ├── util
│   ├── xflens
│   ├── xtensor
│   ├── xtensor-blas
│   └── xtl
├── main.cpp
├── src
│   └── ann
├── array_list_test.cpp
├── doubly_linked_list_test.cpp
├── test_FCLayer.cpp
├── test_ReLU.cpp
├── test_Softmax.cpp
└── test_dataset_and_loader.cpp
```

### Run Test
Now, run this command in the terminal to compile the code into an executable file:

Notes: Please come to `dsastudents` directory before run test

<h2>To compile</h2>

**For Array List and Doubly Linked List**
```
g++ -o <your_exe> -Iinclude -std=c++17 -g <file_need_to_be_run>.cpp
```

Ex: g++ -o test_list -Iinclude -std=c++17 -g array_list_test.cpp

**For Dataset and Data Loader**
```
g++ -o <your_exe> -Iinclude -std=c++17 -g <file_need_to_be_run>.cpp src/ann/xtensor_lib.cpp
```

Ex: g++ -o test_loaddata -Isrc -Iinclude -std=c++17 -g test_dataset_and_loader.cpp src/ann/ReLU.cpp src/ann/functions.cpp src/ann/xtensor_lib.cpp

Note: In case of an error, ensure that function.cpp and xtensor_lib.cpp are implemented exactly as required. If not, please comment out your code.

**For layer of MLP**
```
g++ -o <your_exe> -Isrc -Iinclude -std=c++17 -g <file_need_to_be_run>.cpp src/ann/<Layer you want to test>.cpp src/ann/functions.cpp src/ann/xtensor_lib.cpp
```

Ex: g++ -o test_ReLU -Isrc -Iinclude -std=c++17 -g test_ReLU.cpp src/ann/ReLU.cpp src/ann/functions.cpp src/ann/xtensor_lib.cpp

Note: In case of an error, ensure that function.cpp and xtensor_lib.cpp are implemented exactly as required. If not, please comment out your code.

<h2>To Run</h2>

> For Linux
```
./your_exe [OPTION] [OTHERs (optional)]
```

> For Window
```
./your_exe.exe [OPTION] [OTHERs (optional)]
```

OPTIONS:
  - ?help: To print usage
  - demo: Run demo from original source
  - test: Run all test
  - test num_of_test: Run test numth
  - test num_start_test num_end_test: Run from <start> test to <end> test

![Check it](asset/usage.png)

### Check your result with mine
All result in TestLog

## What next?
- Test for xtensor_lib

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