#!/usr/bin/env python3
"""
SICP Article Downloader and PDF Converter.

Downloads SICP-related articles from Eli Bendersky's website and converts them
to PDF format. Includes error handling, logging, and rate limiting.
"""

import asyncio
import logging
import re
import tempfile
from pathlib import Path
from typing import List, NamedTuple, Optional
from urllib.parse import urljoin

import aiohttp
import pdfkit
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sicp_downloader.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class Article(NamedTuple):
    """Represents an SICP article with its metadata."""
    date: str
    title: str
    url: str

class SICPDownloader:
    """Handles downloading and converting SICP articles to PDF."""
    
    def __init__(self, output_dir: str = "sicp_articles"):
        """Initialize the downloader with configuration."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.base_url = "https://eli.thegreenplace.net"
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def __aenter__(self):
        """Set up async context manager."""
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Clean up async context manager."""
        if self.session:
            await self.session.close()

    def parse_articles(self, html_content: str) -> List[Article]:
        """Parse article information from HTML content."""
        articles = []
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all table rows
        for row in soup.find_all('tr'):
            date_cell = row.find('td')
            link_cell = row.find_all('td')[-1]
            
            if not (date_cell and link_cell):
                continue
                
            link = link_cell.find('a')
            if not link:
                continue
                
            date = date_cell.text.strip().rstrip(':')
            title = link.text.strip()
            url = urljoin(self.base_url, link['href'])
            
            articles.append(Article(date=date, title=title, url=url))
            
        return articles

    async def download_article(self, article: Article) -> Optional[str]:
        """Download an article's HTML content."""
        if not self.session:
            raise RuntimeError("Session not initialized")
            
        try:
            async with self.session.get(article.url) as response:
                if response.status == 200:
                    return await response.text()
                logger.error(
                    "Failed to download {}: Status {}".format(
                        article.url, response.status
                    )
                )
                return None
        except Exception as e:
            logger.error(f"Error downloading {article.url}: {str(e)}")
            return None

    def convert_to_pdf(self, html_content: str, output_path: Path) -> bool:
        """Convert HTML content to PDF."""
        try:
            # Create a temporary file to store the HTML content
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', encoding='utf-8', delete=False) as temp_file:
                temp_file.write("""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <style>
                        body { font-family: Arial, sans-serif; line-height: 1.6; }
                        pre { background-color: #f5f5f5; padding: 1em; }
                        code { font-family: monospace; }
                    </style>
                </head>
                <body>
                """)
                temp_file.write(html_content)
                temp_file.write("</body></html>")
                temp_path = temp_file.name

            options = {
                'quiet': True,
                'enable-local-file-access': None,
                'encoding': 'UTF-8',
                'load-error-handling': 'ignore',
                'load-media-error-handling': 'ignore',
                'no-stop-slow-scripts': None,
                'javascript-delay': 1000,
                'enable-javascript': None,
                'disable-smart-shrinking': None,
                'no-background': None,
                'disable-external-links': None,
                'enable-plugins': None,
                'custom-header': [
                    ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
                ]
            }
            
            # Create a configuration object
            config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
            
            # Convert HTML file to PDF
            pdfkit.from_file(
                temp_path,
                str(output_path),
                options=options,
                configuration=config
            )
            
            # Clean up temporary file
            Path(temp_path).unlink()
            return True
        except Exception as e:
            logger.error(f"Error converting to PDF {output_path}: {str(e)}")
            if 'temp_path' in locals():
                try:
                    Path(temp_path).unlink()
                except:
                    pass
            return False

    async def process_article(self, article: Article):
        """Process a single article: download and convert to PDF."""
        logger.info(f"Processing article: {article.title}")
        
        # Create sanitized filename
        safe_title = re.sub(r'[^\w\s-]', '', article.title)
        safe_title = re.sub(r'[-\s]+', '-', safe_title).strip('-')
        pdf_path = self.output_dir / f"{article.date}_{safe_title}.pdf"
        
        if pdf_path.exists():
            logger.info(f"Article already exists: {pdf_path}")
            return
            
        html_content = await self.download_article(article)
        if not html_content:
            return
            
        if self.convert_to_pdf(html_content, pdf_path):
            logger.info(f"Successfully created PDF: {pdf_path}")
        else:
            logger.error(f"Failed to create PDF for: {article.title}")

    async def process_all_articles(self, html_content: str):
        """Process all articles from the provided HTML content."""
        articles = self.parse_articles(html_content)
        logger.info(f"Found {len(articles)} articles to process")
        
        # Process articles with rate limiting
        for article in articles:
            await self.process_article(article)
            await asyncio.sleep(1)  # Rate limiting

async def main():
    """Main entry point of the script."""
    try:
        with open('sicp_articles.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        logger.error("sicp_articles.html not found")
        return
    except Exception as e:
        logger.error(f"Error reading HTML file: {str(e)}")
        return
    
    async with SICPDownloader() as downloader:
        await downloader.process_all_articles(html_content)

if __name__ == "__main__":
    asyncio.run(main())
