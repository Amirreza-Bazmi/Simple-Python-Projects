# Compute π Using an Infinite Series

## Overview
This program calculates an approximation of π using an infinite series. By summing a finite number of terms from the series, we can estimate the value of π with increasing accuracy.

## Formula
The formula used to approximate π is:

```
π = 4 × (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ⋯ + (-1)^(i+1) / (2i - 1))
```

Where:
- `i` is the term index (starting from 1).
- The series alternates between addition and subtraction.

## Input Requirements
The program computes the approximation of π for various values of `i`:
- `i = 10,000`
- `i = 20,000`
- ...
- `i = 100,000`

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/Amirreza-Bazmi/Simple-Python-Projects/Compute Pi.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Compute Pi
   ```

3. Run the program:
   ```bash
   python compute_pi.py
   ```
