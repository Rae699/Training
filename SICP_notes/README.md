# SICP Exercise Solutions

This directory contains solutions to exercises from the book "Structure and Interpretation of Computer Programs" (SICP).

## Exercise 1.22 and 1.23 - Primality Testing

These exercises explore the efficiency of primality testing algorithms and verify the theoretical time complexity.

### Files:

1. `primality_runtime.py` - Original implementation for Exercise 1.22
   - Uses a basic primality test with trial division
   - Measures execution time for finding primes of different magnitudes

2. `primality_runtime_ex1_23.py` - Implementation for Exercise 1.23
   - Improves the primality test by only checking divisibility by 2 and then odd numbers
   - Should theoretically be about twice as fast as the original algorithm

3. `compare_primality_tests.py` - Directly compares both implementations
   - Runs both algorithms on the same inputs
   - Calculates and displays the speedup achieved by the improved algorithm

### Exercise 1.23 Description

Exercise 1.23 asks us to modify the `is_prime` function to be more efficient by:
1. Checking divisibility by 2 separately
2. Then only checking odd numbers as potential divisors

The theoretical expectation is that this algorithm should run about twice as fast as the original one, since we're testing approximately half as many divisors.

### Running the Code

To run the comparison script:

```bash
python compare_primality_tests.py
```

This will test both implementations on primes of different magnitudes and show the speedup achieved.

### Analysis

The actual speedup observed may differ from the theoretical 2x improvement due to factors such as:
1. The overhead of the `next_divisor` function call
2. CPU caching and branch prediction effects
3. Other system-level optimizations or bottlenecks

The comparison script provides detailed timing information to analyze the actual performance improvement.

# SICP Article Downloader

This script downloads SICP (Structure and Interpretation of Computer Programs) related articles from Eli Bendersky's website and converts them to PDF format.

## Prerequisites

1. Python 3.7 or higher
2. wkhtmltopdf (required for PDF conversion)

### Installing wkhtmltopdf

- **macOS**: `brew install wkhtmltopdf`
- **Ubuntu/Debian**: `sudo apt-get install wkhtmltopdf`
- **Windows**: Download from [wkhtmltopdf downloads](https://wkhtmltopdf.org/downloads.html)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python sicp_downloader.py
```

The script will:
- Create a `sicp_articles` directory for the PDFs
- Download each article and convert it to PDF
- Log progress to both console and `sicp_downloader.log`

## Features

- Asynchronous downloads for better performance
- Rate limiting to be respectful to the server
- Proper error handling and logging
- Automatic retry on failures
- Skips already downloaded articles
- Creates clean, readable PDFs

## Logging

The script logs all activities to:
- Console output
- `sicp_downloader.log` file

## Output

PDFs are saved in the `sicp_articles` directory with filenames in the format:
`YYYY.MM.DD_Article-Title.pdf` 