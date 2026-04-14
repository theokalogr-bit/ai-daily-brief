import os
import anthropic
from dotenv import load_dotenv

load_dotenv()


def generate_brief(emails, news, today):
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    emails_text = ""
    if emails:
        for e in emails:
            emails_text += f"- From: {e['sender']}\n  Subject: {e['subject']}\n  Preview: {e['snippet']}\n\n"
    else:
        emails_text = "No unread emails."

    news_text = ""
    if news:
        for n in news:
            news_text += f"- {n['title']}\n  {n['body']}\n  URL: {n['url']}\n\n"
    else:
        news_text = "No news results found."

    prompt = f"""Today is {today}.

Here are the user's unread emails:
{emails_text}

Here are the latest AI news results:
{news_text}

Generate a clean daily brief with two sections:

### Inbox
Summarize each email in one line: who it's from, what it's about. Be direct. Skip marketing/promo emails with a single "(promo)" label.

### AI News Today
Pick the 3-5 most significant stories. For each: one bold headline, then 1-2 sentences on what happened and why it matters. Skip duplicates."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are a personal assistant generating a concise daily brief. Be direct and informative — no fluff, no openers.",
        messages=[{"role": "user", "content": prompt}],
    )

    return message.content[0].text
