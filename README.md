# WELCOME TO TESTCASE FOR DSA ASSIGNMENT

## Introduction

<div>
<h1> Viet Nam National University 
<h2> Ho Chi Minh City University of Technology
<h3> Faculty of Computer Science and Engineering
<h4> Data Structure and Algorithm - HK241
<h5> First Author: Nguyen Phuc Nhan
</div>

- Version v1.1 : Restructuring the project's folder and adding more test cases for the assignment
- Version v0.1 : If you use same folder structure as the assignment 1, you can read here [README.old.md](README.old.md)

* For new version, I will provide more test cases for the assignment 2. You can check the result of your code with mine. Additionally, I will update argruments for compile project with C++.

## How to?

### Set up
Place the files in the same directory as your project.

* Example for folder's structure

Assume you extract the root folder from LMS, then go to dsastudents like this:

> Assignment
```
$  tree -L 3
.
├── Code
│   ├── Makefile
│   ├── compilation-command.sh
│   ├── config.txt
│   ├── datasets
│   │   ├── 2c-classification
│   │   └── 3c-classification
│   ├── demo
│   │   ├── ann
│   │   ├── graph
│   │   ├── hash
│   │   ├── heap
│   │   ├── list
│   │   ├── loader
│   │   ├── sformat
│   │   ├── sorting
│   │   ├── stacknqueue
│   │   ├── tensor
│   │   ├── tree
│   │   └── util
│   ├── include
│   │   ├── ann
│   │   ├── dsaheader.h
│   │   ├── graph
│   │   ├── hash
│   │   ├── heap
│   │   ├── list
│   │   ├── loader
│   │   ├── sformat
│   │   ├── sorting
│   │   ├── stacknqueue
│   │   ├── tensor
│   │   ├── tree
│   │   └── util
│   ├── models
│   │   ├── 2c-classification
│   │   ├── 2c-classification-1
│   │   ├── 3c-classification
│   │   └── 3c-classification-1
│   └── src
│       ├── ann
│       ├── program.cpp
│       └── tensor
├── Spec
│   └── V1.0
│       ├── Assignment2-en.pdf
│       ├── Assignment2-vn.pdf
│       └── DSA241-VN.pdf
└── Tutorials
    ├── ann-tutorials-en.pdf
    └── ann-tutorials-vn.pdf
```

Then, place all file here into `Assignment`:

```
$  tree -L 3
.
├── Code
│   ├── Makefile
│   ├── compilation-command.sh
│   ├── config.txt
│   ├── datasets
│   │   ├── 2c-classification
│   │   └── 3c-classification
│   ├── demo
│   │   ├── ann
│   │   ├── graph
│   │   ├── hash
│   │   ├── heap
│   │   ├── list
│   │   ├── loader
│   │   ├── sformat
│   │   ├── sorting
│   │   ├── stacknqueue
│   │   ├── tensor
│   │   ├── tree
│   │   └── util
│   ├── include
│   │   ├── ann
│   │   ├── dsaheader.h
│   │   ├── graph
│   │   ├── hash
│   │   ├── heap
│   │   ├── list
│   │   ├── loader
│   │   ├── sformat
│   │   ├── sorting
│   │   ├── stacknqueue
│   │   ├── tensor
│   │   ├── tree
│   │   └── util
│   ├── models
│   │   ├── 2c-classification
│   │   ├── 2c-classification-1
│   │   ├── 3c-classification
│   │   └── 3c-classification-1
│   └── src
│       ├── ann
│       ├── program.cpp
│       └── tensor
├── Self_test
│   ├── DemoLog.txt
│   ├── TestLog
│   │   ├── Array
│   │   ├── BaseModel
│   │   ├── DLinkedList
│   │   ├── DataSetAndLoader
│   │   ├── FCLayer
│   │   ├── HashMap
│   │   ├── ReLU
│   │   └── Softmax
│   ├── test_BaseModel.cpp
│   ├── test_FCLayer.cpp
│   ├── test_MLP.cpp
│   ├── test_ReLU.cpp
│   ├── test_Softmax.cpp
│   ├── test_array_list.cpp
│   ├── test_dataset_and_loader.cpp
│   ├── test_doubly_linked_list.cpp
│   ├── test_hash_map.cpp
│   ├── test_load_data
│   ├── test_xtensor_lib.cpp
│   ├── training.cpp
│   ├── unit_test_program
│   └── valgrind-out.txt
├── Spec
│   └── V1.0
│       ├── Assignment2-en.pdf
│       ├── Assignment2-vn.pdf
└── Tutorials
    ├── ann-tutorials-en.pdf
    └── ann-tutorials-vn.pdf
```

### Run Test
Now, run this command in the terminal to compile the code into an executable file:

<h2>To compile</h2>

**For Array List, Doubly Linked List, Heap, Hash, ...**
```
g++ -o <your_exe> -ICode/include -ICode/include/ann -ICode/include/tensor -ICode/include/sformat -ICode/demo -ICode/src -ISelf_test -std=c++17 -g ./Self_test/<file_need_to_be_run>.cpp
```

Ex: g++ -o test_list -ICode/include -ICode/include/ann -ICode/include/tensor -ICode/include/sformat -ICode/demo -ICode/src -ISelf_test -std=c++17 -g array_list_test.cpp

**For Dataset and Data Loader**
```
g++ -o <your_exe> -ICode/include -ICode/include/ann -ICode/include/tensor -ICode/include/sformat -ICode/demo -ICode/src -ISelf_test -std=c++17 -g ./Self_test/<file_need_to_be_run>.cpp ./Code/src/tensor/xtensor_lib.cpp
```

Ex: g++ -o test_loaddata -ICode/include -ICode/include/ann -ICode/include/tensor -ICode/include/sformat -ICode/demo -ICode/src -ISelf_test -std=c++17 -g test_dataset_and_loader.cpp src/ann/ReLU.cpp src/ann/functions.cpp src/ann/xtensor_lib.cpp

Note: In case of an error, ensure that function.cpp and xtensor_lib.cpp are implemented exactly as required. If not, please comment out your code.

**For layer of MLP**
```
g++ -o <your_exe> -ICode/include -ICode/include/ann -ICode/include/tensor -ICode/include/sformat -ICode/demo -ICode/src -ISelf_test -std=c++17 -g <file_need_to_be_run>.cpp src/ann/<Layer you want to test>.cpp src/ann/functions.cpp src/ann/xtensor_lib.cpp
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