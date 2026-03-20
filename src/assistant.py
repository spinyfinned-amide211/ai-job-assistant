"""
AI Job Application Assistant — Core Logic
"""

import os
from openai import OpenAI
from .parser import parse_cv, parse_job_posting
from .scorer import calculate_match_score
from .utils import save_output, print_success, print_error


class JobAssistant:
    def __init__(self, config):
        self.config = config
        self.client = OpenAI(api_key=config.get("openai_api_key") or os.getenv("OPENAI_API_KEY"))
        self.model = config.get("model", "gpt-4o")

    def _ask_ai(self, system_prompt: str, user_prompt: str) -> str:
        """Send a prompt to OpenAI and return the response."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            print_error(f"OpenAI API error: {e}")
            raise

    def analyze_job(self, args) -> dict:
        """Analyze a job posting and extract key requirements."""
        print("\n🔍 Analyzing job posting...\n")

        job_text = parse_job_posting(args.url if hasattr(args, "url") else None,
                                     args.text if hasattr(args, "text") else None)
        cv_text = parse_cv(args.cv)

        system_prompt = """You are an expert career coach and HR specialist.
        Analyze job postings and extract key insights to help candidates succeed."""

        user_prompt = f"""Analyze this job posting and provide:

1. **Required Skills** (must-have)
2. **Nice-to-have Skills**
3. **Key Responsibilities**
4. **Company Culture Signals**
5. **Red Flags** (if any)
6. **Keywords to include** in CV/cover letter
7. **Match Score** with the provided CV (0-100)
8. **Top 3 improvements** to make the CV stronger

JOB POSTING:
{job_text}

CANDIDATE CV:
{cv_text}

Format your response clearly with sections and bullet points."""

        result = self._ask_ai(system_prompt, user_prompt)
        print(result)
        return result

    def tailor_cv(self, args) -> str:
        """Rewrite CV to match a specific job posting."""
        print("\n✍️  Tailoring your CV...\n")

        job_text = parse_job_posting(args.url if hasattr(args, "url") else None,
                                     args.text if hasattr(args, "text") else None)
        cv_text = parse_cv(args.cv)

        system_prompt = """You are an expert CV writer with 15 years of experience.
        You know exactly how to tailor CVs to pass ATS systems and impress hiring managers.
        You never fabricate information — you only reframe and highlight existing experience."""

        user_prompt = f"""Tailor this CV for the job posting below.

Rules:
- Keep all facts accurate — never invent experience
- Use keywords from the job posting naturally
- Reorder and emphasize relevant experience
- Use strong action verbs
- Quantify achievements where possible
- Make it ATS-friendly

JOB POSTING:
{job_text}

ORIGINAL CV:
{cv_text}

Return the complete tailored CV, ready to use."""

        result = self._ask_ai(system_prompt, user_prompt)
        save_output(result, args.output)
        print_success(f"Tailored CV saved to: {args.output}")
        return result

    def generate_cover_letter(self, args) -> str:
        """Generate a personalized cover letter."""
        print("\n📝 Generating cover letter...\n")

        job_text = parse_job_posting(args.url if hasattr(args, "url") else None,
                                     args.text if hasattr(args, "text") else None)
        cv_text = parse_cv(args.cv)

        system_prompt = """You are an expert cover letter writer.
        You write compelling, personalized cover letters that get callbacks.
        You avoid clichés and write in a natural, confident tone."""

        user_prompt = f"""Write a compelling cover letter for this job application.

Guidelines:
- Hook the reader in the first sentence
- Show genuine interest in the company/role
- Connect 2-3 specific achievements from the CV to the job requirements
- Show personality — not robotic
- End with a clear call to action
- Length: 3-4 paragraphs maximum
- Tone: Professional but human

JOB POSTING:
{job_text}

CANDIDATE CV:
{cv_text}

Write the complete cover letter."""

        result = self._ask_ai(system_prompt, user_prompt)
        save_output(result, args.output)
        print_success(f"Cover letter saved to: {args.output}")
        return result

    def score_cv(self, args) -> dict:
        """Score how well a CV matches a job posting."""
        print("\n📊 Scoring your CV...\n")

        job_text = parse_job_posting(args.url if hasattr(args, "url") else None,
                                     args.text if hasattr(args, "text") else None)
        cv_text = parse_cv(args.cv)

        system_prompt = """You are an ATS system and expert recruiter.
        Score CVs objectively and provide actionable feedback."""

        user_prompt = f"""Score this CV against the job posting.

Provide:
1. **Overall Match Score**: X/100
2. **Skills Match**: X/100
   - Present: [list]
   - Missing: [list]
3. **Experience Match**: X/100
4. **Keywords Score**: X/100
   - Found: [list]
   - Missing: [list]
5. **Format Score**: X/100
6. **Top 5 Improvements** (ranked by impact)
7. **Verdict**: Should apply? (Yes/Maybe/No) with reasoning

JOB POSTING:
{job_text}

CV:
{cv_text}"""

        result = self._ask_ai(system_prompt, user_prompt)
        print(result)

        keyword_score = calculate_match_score(cv_text, job_text)
        print(f"\n📈 Keyword Match Rate: {keyword_score:.1f}%")
        return result
