import sys
import io
from datetime import date
from gmail_client import get_unread_emails
from news_client import get_ai_news
from claude_client import generate_brief

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def main():
    today = date.today().strftime("%A, %B %d, %Y")
    print(f"\n## Daily Brief — {today}\n")
    print("Fetching emails...")
    emails = get_unread_emails(max_results=5)

    print("Fetching AI news...")
    news = get_ai_news(max_results=5)

    print("Generating brief...\n")
    brief = generate_brief(emails, news, today)

    print(brief)
    print()


if __name__ == "__main__":
    main()
