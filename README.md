# The Algorithms - Python

[![Contributors](https://img.shields.io/github/contributors/vJechsmayr/PythonAlgorithms)](https://github.com/vJechsmayr/PythonAlgorithms/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/vJechsmayr/PythonAlgorithms)](https://github.com/vJechsmayr/PythonAlgorithms/issues)
[![Open Pull Requests](https://img.shields.io/github/issues-pr-raw/vJechsmayr/PythonAlgorithms)](https://github.com/vJechsmayr/PythonAlgorithms/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/vJechsmayr/PythonAlgorithms)](https://github.com/vJechsmayr/PythonAlgorithms)
[![Stars](https://img.shields.io/github/stars/vJechsmayr/PythonAlgorithms)](https://github.com/vJechsmayr/PythonAlgorithms/stargazers)
[![Forks](https://img.shields.io/github/forks/vJechsmayr/PythonAlgorithms)](https://github.com/vJechsmayr/PythonAlgorithms/network/members)
[![Watchers](https://img.shields.io/github/watchers/vJechsmayr/PythonAlgorithms)](https://github.com/vJechsmayr/PythonAlgorithms/watchers)
[![License](https://img.shields.io/github/license/vJechsmayr/PythonAlgorithms)](https://github.com/vJechsmayr/PythonAlgorithms/blob/master/LICENSE)


## Table of Contents
* [Inspiration and Motivation](#inspiration)
* [Contributing Guidelines](#contributing-guidelines)
* [Start Here](#getting-started)




### All algorithms implemented in Python 3 (for education)
There implementations are for learning purposes. If you want to contribute more efficient solutions feel free to open an issue and commit your solution.

## Inspiration

You can look for Algorithms to implement at: [LeetCode Algorithms](https://leetcode.com/problemset/algorithms/) 

To contribute make sure the Algorithm isn't commited yet! Make sure to add the number of the Issue in your PR.

## Contributing Guidelines

### Folders and Files
Please make sure your file is in the `LeetCode`-Folder and Named like this:
`0001_TwoSum.py` -> 4-digit Number of the LeetCode Issue, Underscore, LeetCodeName

### Pull Requests
Only Pull Requests **joined with an Issue** and matching the **naming-conventions** (See Folders and Files) will be merged!
If there is no Issue joined in the PR your PR will be labeld as **spam** and closed.
If your code don't passes the Check on LeetCode.com your PR will be labeld as **"invalid"** and the Issue stays open for the next PR!

## Getting Started
* Fork this repository (Click the Form button, top right of this page)
* Clone your fork down to your local machine
```markdown
git clone https://github.com/your-username/pythonalgorithms.git
```
* Comment to the Issue you want to work on - so I can assign you to it OR create a new Issue from a LeetCode Problem that is not implemented yet
* Create a branch for a new feature
```markdown
git checkout -b feature/branch-name
```
* Or if its a bugfix to a file
```markdown
git checkout -b bugfix/branch-name
```
* Make your changes (choose from the Tasks above!)
* Commit and Push
```markdown
git add .
git commit -m 'commit message'
git push origin branch-name
```
* Create a New Pull Request from your forked repository ( Click the 'New Pull Request' Button located at the top of your repo)
* Wait for your PR review and merge approval!
* __Star this repository__ if you had fun!

## Which PR will be accepted?
* Ones you are assigned to
* Your PR has to link the Issue
* Your Solution must be correct - you can check ist on LeetCode (submit) if it works on different test-cases
Posterior Analysis − This is an empirical analysis of an algorithm. The selected algorithm is implemented using programming language. This is then executed on target computer machine. In this analysis, actual statistics like running time and space required, are collected.

## Algorithm Complexity
Suppose X is an algorithm and n is the size of input data, the time and space used by the algorithm X are the two main factors, which decide the efficiency of X.

Time Factor − Time is measured by counting the number of key operations such as comparisons in the sorting algorithm.

Space Factor − Space is measured by counting the maximum memory space required by the algorithm.

The complexity of an algorithm f(n) gives the running time and/or the storage space required by the algorithm in terms of n as the size of input data.

Space Complexity
Space complexity of an algorithm represents the amount of memory space required by the algorithm in its life cycle. The space required by an algorithm is equal to the sum of the following two components −

A fixed part that is a space required to store certain data and variables, that are independent of the size of the problem. For example, simple variables and constants used, program size, etc.

A variable part is a space required by variables, whose size depends on the size of the problem. For example, dynamic memory allocation, recursion stack space, etc.

Space complexity S(P) of any algorithm P is S(P) = C + SP(I), where C is the fixed part and S(I) is the variable part of the algorithm, which depends on instance characteristic I. Following is a simple example that tries to explain the concept −

## Algorithm: SUM(A, B)
Step 1 -  START
Step 2 -  C ← A + B + 10
Step 3 -  Stop
Here we have three variables A, B, and C and one constant. Hence S(P) = 1 + 3. Now, space depends on data types of given variables and constant types and it will be multiplied accordingly.

## Time Complexity
Time complexity of an algorithm represents the amount of time required by the algorithm to run to completion. Time requirements can be defined as a numerical function T(n), where T(n) can be measured as the number of steps, provided each step consumes constant time.

For example, addition of two n-bit integers takes n steps. Consequently, the total computational time is T(n) = c ∗ n, where c is the time taken for the addition of two bits. Here, we observe that T(n) grows linearly as the input size increases.

 


__Thank You!__ 
