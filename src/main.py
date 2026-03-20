"""
AI Job Application Assistant
Main entry point
"""

import argparse
from src.assistant import JobAssistant
from src.utils import load_config, print_banner


def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description="AI Job Application Assistant — Tailor your CV and cover letter for any job"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a job posting")
    analyze_parser.add_argument("--url", type=str, help="Job posting URL")
    analyze_parser.add_argument("--text", type=str, help="Job posting text")
    analyze_parser.add_argument("--cv", type=str, required=True, help="Path to your CV (PDF or TXT)")

    # Tailor command
    tailor_parser = subparsers.add_parser("tailor", help="Tailor your CV for a job")
    tailor_parser.add_argument("--url", type=str, help="Job posting URL")
    tailor_parser.add_argument("--text", type=str, help="Job posting text")
    tailor_parser.add_argument("--cv", type=str, required=True, help="Path to your CV")
    tailor_parser.add_argument("--output", type=str, default="tailored_cv.txt", help="Output file")

    # Cover letter command
    cover_parser = subparsers.add_parser("cover", help="Generate a cover letter")
    cover_parser.add_argument("--url", type=str, help="Job posting URL")
    cover_parser.add_argument("--text", type=str, help="Job posting text")
    cover_parser.add_argument("--cv", type=str, required=True, help="Path to your CV")
    cover_parser.add_argument("--output", type=str, default="cover_letter.txt", help="Output file")

    # Score command
    score_parser = subparsers.add_parser("score", help="Score your CV against a job")
    score_parser.add_argument("--url", type=str, help="Job posting URL")
    score_parser.add_argument("--text", type=str, help="Job posting text")
    score_parser.add_argument("--cv", type=str, required=True, help="Path to your CV")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    config = load_config()
    assistant = JobAssistant(config)

    if args.command == "analyze":
        assistant.analyze_job(args)
    elif args.command == "tailor":
        assistant.tailor_cv(args)
    elif args.command == "cover":
        assistant.generate_cover_letter(args)
    elif args.command == "score":
        assistant.score_cv(args)


if __name__ == "__main__":
    main()
