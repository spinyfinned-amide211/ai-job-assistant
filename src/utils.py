"""
Utility functions
"""

import os
import json
from pathlib import Path


def print_banner():
    banner = """
╔══════════════════════════════════════════════════════════╗
║         🤖 AI Job Application Assistant v1.0             ║
║      Tailor your CV & Cover Letter with AI Power         ║
║              github.com/khaledxbenali92                  ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)


def print_success(message: str):
    print(f"\n✅ {message}")


def print_error(message: str):
    print(f"\n❌ {message}")


def load_config() -> dict:
    """Load configuration from config.json or environment."""
    config_path = Path("config/config.json")

    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)

    return {
        "openai_api_key": os.getenv("OPENAI_API_KEY", ""),
        "model": os.getenv("OPENAI_MODEL", "gpt-4o"),
    }


def save_output(content: str, output_path: str):
    """Save generated content to file."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
