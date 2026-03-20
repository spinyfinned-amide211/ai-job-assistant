"""
Parser module — CV and Job Posting extraction
"""

import re
import requests
from pathlib import Path
from bs4 import BeautifulSoup


def parse_cv(cv_path: str) -> str:
    """Parse CV from PDF or TXT file."""
    path = Path(cv_path)

    if not path.exists():
        raise FileNotFoundError(f"CV file not found: {cv_path}")

    if path.suffix.lower() == ".pdf":
        return _parse_pdf(cv_path)
    elif path.suffix.lower() in [".txt", ".md"]:
        return path.read_text(encoding="utf-8")
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}. Use PDF or TXT.")


def _parse_pdf(pdf_path: str) -> str:
    """Extract text from PDF."""
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text.strip()
    except ImportError:
        raise ImportError("pdfplumber not installed. Run: pip install pdfplumber")


def parse_job_posting(url: str = None, text: str = None) -> str:
    """Parse job posting from URL or raw text."""
    if text:
        return text.strip()
    elif url:
        return _scrape_job_url(url)
    else:
        raise ValueError("Provide either --url or --text for the job posting.")


def _scrape_job_url(url: str) -> str:
    """Scrape job posting from URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove noise
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        # Try common job posting containers
        selectors = [
            "article",
            '[class*="job-description"]',
            '[class*="description"]',
            '[class*="posting"]',
            "main",
        ]

        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                text = element.get_text(separator="\n", strip=True)
                if len(text) > 200:
                    return _clean_text(text)

        # Fallback to body
        return _clean_text(soup.get_text(separator="\n", strip=True))

    except requests.RequestException as e:
        raise ConnectionError(f"Failed to fetch job posting: {e}")


def _clean_text(text: str) -> str:
    """Clean extracted text."""
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" {2,}", " ", text)
    return text.strip()
