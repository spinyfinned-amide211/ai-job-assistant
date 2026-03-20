<div align="center">

# 🤖 AI Job Application Assistant

### Tailor your CV & Cover Letter for any job in seconds — powered by GPT-4

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/khaledxbenali92/ai-job-assistant?style=for-the-badge&color=yellow)](https://github.com/khaledxbenali92/ai-job-assistant/stargazers)
[![Issues](https://img.shields.io/github/issues/khaledxbenali92/ai-job-assistant?style=for-the-badge)](https://github.com/khaledxbenali92/ai-job-assistant/issues)

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## 🎯 The Problem

You apply to 50 jobs. You get 2 callbacks.

The reason? Your CV is **generic**. ATS systems filter you out before a human ever reads your application.

**AI Job Application Assistant** solves this by tailoring your CV and cover letter to each job posting in seconds — using the exact keywords and language that hiring managers and ATS systems are looking for.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Job Analyzer** | Extract key requirements, skills & culture signals from any job posting |
| ✍️ **CV Tailor** | Rewrite your CV to match the exact job requirements |
| 📝 **Cover Letter Generator** | Create personalized, compelling cover letters |
| 📊 **Match Scorer** | Get a score (0-100) showing how well your CV matches the job |
| 🔗 **URL Support** | Paste any job URL — LinkedIn, Indeed, Greenhouse, Lever, etc. |
| 📄 **PDF Support** | Upload your CV as PDF or TXT |
| 🔑 **Keyword Analysis** | Find missing keywords that ATS systems are looking for |

---

## 🚀 Demo

```bash
# Analyze a job posting
python -m src.main analyze --url "https://linkedin.com/jobs/view/123" --cv my_cv.pdf

# Score your CV against a job
python -m src.main score --url "https://jobs.lever.co/company/role" --cv my_cv.pdf

# Tailor your CV
python -m src.main tailor --url "https://greenhouse.io/job/123" --cv my_cv.pdf --output tailored_cv.txt

# Generate a cover letter
python -m src.main cover --url "https://jobs.ashbyhq.com/company/role" --cv my_cv.pdf --output cover_letter.txt
```

**Example Output:**

```
╔══════════════════════════════════════════════════════════╗
║         🤖 AI Job Application Assistant v1.0             ║
║      Tailor your CV & Cover Letter with AI Power         ║
╚══════════════════════════════════════════════════════════╝

📊 CV Match Score: 73/100

✅ Skills Found: Python, React, Node.js, AWS, Docker
❌ Missing Keywords: Kubernetes, GraphQL, CI/CD, Agile

🎯 Top 3 Improvements:
1. Add "Kubernetes" experience from your DevOps work
2. Mention "Agile/Scrum" methodology
3. Quantify your AWS experience with specific metrics
```

---

## 🛠️ Installation

### Prerequisites

- Python 3.9+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Step 1 — Clone the repository

```bash
git clone https://github.com/khaledxbenali92/ai-job-assistant.git
cd ai-job-assistant
```

### Step 2 — Create a virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure your API key

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your OpenAI API key
nano .env  # or use any text editor
```

Your `.env` file should look like:
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_MODEL=gpt-4o
```

---

## 📖 Usage

### 1. Analyze a Job Posting

Understand what a job really requires before applying:

```bash
# From URL
python -m src.main analyze \
  --url "https://linkedin.com/jobs/view/123456" \
  --cv path/to/your_cv.pdf

# From pasted text
python -m src.main analyze \
  --text "Senior Product Manager at Acme Corp. Requirements: 5+ years PM experience..." \
  --cv path/to/your_cv.pdf
```

### 2. Score Your CV

Get an objective score before applying:

```bash
python -m src.main score \
  --url "https://jobs.lever.co/company/role-id" \
  --cv my_cv.pdf
```

Output includes:
- Overall match score (0-100)
- Skills match breakdown
- Missing keywords
- Top improvements ranked by impact

### 3. Tailor Your CV

Get a rewritten CV optimized for the specific job:

```bash
python -m src.main tailor \
  --url "https://greenhouse.io/jobs/12345" \
  --cv my_cv.pdf \
  --output tailored_cv.txt
```

### 4. Generate a Cover Letter

Create a personalized cover letter in seconds:

```bash
python -m src.main cover \
  --url "https://jobs.ashbyhq.com/company/role" \
  --cv my_cv.pdf \
  --output cover_letter.txt
```

---

## 📁 Project Structure

```
ai-job-assistant/
├── src/
│   ├── __init__.py          # Module exports
│   ├── main.py              # CLI entry point
│   ├── assistant.py         # Core AI logic
│   ├── parser.py            # CV & job posting parser
│   ├── scorer.py            # Keyword match scoring
│   └── utils.py             # Helper functions
├── tests/
│   └── test_assistant.py    # Unit tests
├── config/
│   └── config.example.json  # Configuration template
├── docs/
│   └── CONTRIBUTING.md      # Contribution guide
├── .env.example             # Environment variables template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧪 Running Tests

```bash
# Install test dependencies
pip install pytest

# Run all tests
pytest tests/ -v

# Run with coverage
pip install pytest-cov
pytest tests/ --cov=src --cov-report=term-missing
```

---

## 🗺️ Roadmap

- [x] CLI interface with 4 commands
- [x] PDF CV parsing
- [x] URL job scraping
- [x] Keyword scoring
- [ ] Web UI (Streamlit)
- [ ] Browser Extension
- [ ] Batch processing (multiple jobs at once)
- [ ] Export to DOCX/PDF
- [ ] Job tracking dashboard
- [ ] LinkedIn integration
- [ ] Email alerts for matching jobs

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### 1. Fork the repository

Click the **Fork** button at the top of this page.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR-USERNAME/ai-job-assistant.git
cd ai-job-assistant
```

### 3. Create a feature branch

```bash
git checkout -b feature/your-feature-name
```

### 4. Make your changes

Follow the existing code style. Add tests for new features.

### 5. Run tests

```bash
pytest tests/ -v
```

### 6. Commit and push

```bash
git add .
git commit -m "feat: add your feature description"
git push origin feature/your-feature-name
```

### 7. Open a Pull Request

Go to the original repository and click **New Pull Request**.

### Contribution Ideas

- 🌐 Add support for more job board URLs
- 🎨 Build a Streamlit web interface
- 📄 Add DOCX export support
- 🌍 Add multilingual support
- 🔧 Improve PDF parsing accuracy
- 📊 Add more scoring metrics

---

## ⚙️ Configuration

| Option | Default | Description |
|--------|---------|-------------|
| `OPENAI_API_KEY` | required | Your OpenAI API key |
| `OPENAI_MODEL` | `gpt-4o` | OpenAI model to use |

**Cost estimate:** Each analysis costs approximately $0.01-0.05 with GPT-4o.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Khaled Ben Ali**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/benalikhaled)
[![Twitter](https://img.shields.io/badge/Twitter-Follow-1DA1F2?style=flat&logo=twitter)](https://twitter.com/khaledbali92)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-333?style=flat&logo=github)](https://github.com/khaledxbenali92)

---

<div align="center">

⭐ **Star this repo if it helped you land your next job!** ⭐

</div>
