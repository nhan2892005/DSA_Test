# WELCOME TO TESTCASE FOR DSA ASSIGNMENT

## Introduction

Automation test for DSA Assignment

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

Assume you extract the root folder from LMS like this:

```
tree -L 3
.
|-- __MACOSX       
|   `-- dsastudents
|       |-- include
|       `-- src    
`-- dsastudents
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

Then, place ‘ArrayTest’ and ‘array_list_test.cpp’ into ./dsastudents:

```
tree -L 3
.
|-- __MACOSX       
|   `-- dsastudents
|       |-- include
|       `-- src    
`-- dsastudents    
    |-- ArrayTest  
    |   |-- test
    |   `-- write_test.py       
    |-- array_list_test.cpp
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

### Run Test
Now, run this command in the terminal to compile the code into an executable file:

Notes: Please come to `dsastudents` directory before run test

```
g++ -o <your exe> -Isrc -Iinclude -std=c++17 -g array_list_test
```

* Explanation: 

```
g++ : compiler (recommend because it be used for formal test)
-o your_exe : choose file you will compile to
-Isrc, -Iinclude: add parent path to run project
-std=c++17 : run c++ on version c++17
-g source_file : choose file need to be compile
```

### Check your result with mine

- Path to input: `'./ArrayTest/test/input/input' + str(num) + '.txt'`
- Path to your output: `'./ArrayTest/test/output/output' + str(num) + '.txt'`
- Path to my output: `'./ArrayTest/test/expected/expect' + str(num) + '.txt'`
- Path to log file: `'./ArrayTest/test/log/log' + str(num) + '.txt'`


## How to generate test

check ./ArrayTest/write_test.py

## What next?

Based on the assignment brief, proceed to test the next task.

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