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