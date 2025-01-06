# Zeller's Congruence

## Overview
Zeller's Congruence is an algorithm devised by Christian Zeller to determine the day of the week for a given date.

## Formula
The formula used in Zeller's Congruence is:

```
h = (q + ⌊(26(m + 1)) / 10⌋ + k + ⌊k / 4⌋ + ⌊j / 4⌋ + 5j) % 7
```

Where:
- `h` is the day of the week:
  - 0: Saturday
  - 1: Sunday
  - 2: Monday
  - 3: Tuesday
  - 4: Wednesday
  - 5: Thursday
  - 6: Friday
- `q` is the day of the month.
- `m` is the month:
  - March = 3, April = 4, ..., December = 12.
  - January and February are considered months 13 and 14 of the previous year.
- `j` is the century (i.e., ⌊year / 100⌋).
- `k` is the year within the century (i.e., year % 100).

## Input Requirements
1. Year (e.g., 2025).
2. Month (1 for January, 2 for February, ..., 12 for December).
3. Day of the month (1 through 31).

> **Note:** For January and February, the month value should be converted to 13 and 14, respectively, and the year should be adjusted to the previous year.

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/Amirreza-Bazmi/Simple-Python-Projects/Zeller's Congruence.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Zeller's Congruence
   ```

3. Run the program:
   ```bash
   python zellers_congruence.py
   ```
