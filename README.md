

## Overview
This project extracts useful data from messy raw text using regular expressions.  
The input simulates untrusted data coming from an external source like an API or logs.



# Data Extracted
- Email addresses  
- URLs  
- Phone numbers  
- Credit card numbers  

Only valid formats are extracted. Broken or unsafe input is ignored.

---

## Security Notes
- Input is treated as untrusted  
- Regex patterns are strict and non-greedy  
- Emails and credit card numbers are masked in the output  
- Script-like or malformed data is not processed  

---

## How to Run

python main.py
