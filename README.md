# TSP-dynamic-programming-Python
This is a homework from the course Algorithms.

Using Dynamic Programming

Reference: https://github.com/phvargas/TSP-python.git

## Introduction
what is in the readfile.txt?

```bash
First column is the index of city

Second column is the x cooridinate

Third column is the y cooridinate
```
You can simply modify this txt file by changing its idex or position.
## 1. Run the program
```python
python3 TSP_dp.py
```
## 2. Two files will be generated

1. draw.txt -> used to draw the route
2. output.txt ->include route, best distance and execution time.
```bash
Best Visit Order: 1  3  2  11  9  10  5  4  6  7  8  1  
Best Distance：  167.80695975880067
Execution Time:  0.1690812110900879  (s)
```
## 3. gnuplot mode
```bash
gnuplot
```
## 4. draw path 
```bash
load "draw.plt"
```
## 5. Result

output.svg will be generated.

Use Chrome or safari to open it

<img width="644" alt="截圖 2021-04-13 下午3 22 30" src="https://user-images.githubusercontent.com/73986032/114512806-13f29c80-9c6c-11eb-949f-16cfa0450799.png">


