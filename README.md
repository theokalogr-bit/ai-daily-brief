# AI Daily Brief

A Python CLI tool that generates a personalized daily brief using the Claude API, Gmail, and live web search. Run it every morning to get a summary of your unread emails and the latest AI news — all in one clean output.

## What It Does

- Fetches your unread emails from Gmail and summarizes each one in plain English
- Searches the web for the latest AI news from the past 24 hours
- Feeds everything into Claude (Anthropic) to generate a clean, formatted brief
- Outputs to terminal in seconds

## Example Output

```
## Daily Brief — Tuesday, April 14, 2026

### Inbox
- **AUEB (Androutsos):** Solutions for Java chapters 1 & 2 uploaded to GitHub.
- **Slack (Coding Factory):** New message in #databases from Stavroula (Apr 13).
- **Grant Cardone:** (promo)
- **Revolut:** (promo)

---

### AI News Today

**AI Fails Primary Patient Diagnosis Over 80% of the Time**
A new study found generative AI still lacks the reasoning for safe clinical use,
failing primary diagnosis in more than 4 out of 5 cases.

**Gemini 3.1 Pro and GPT-5.4 Pro Tied at Top of AI Benchmarks**
Google's Gemini 3.1 Pro leads or ties across 13 of 16 major benchmarks,
neck-and-neck with OpenAI's GPT-5.4 Pro.
```

## Setup

### 1. Clone and install dependencies

```bash
git clone https://github.com/your-username/ai-daily-brief.git
cd ai-daily-brief
pip install -r requirements.txt
```

### 2. Add your Anthropic API key

```bash
cp .env.example .env
```

Edit `.env` and add your key:
```
ANTHROPIC_API_KEY=your_key_here
```

Get your key at [console.anthropic.com](https://console.anthropic.com).

### 3. Set up Gmail API

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a project and enable the **Gmail API**
3. Go to **APIs & Services → Credentials → Create credentials → OAuth 2.0 Client ID**
4. Application type: **Desktop app**
5. Download the JSON and save it as `credentials.json` in the project root

### 4. Run it

```bash
python3 brief.py
```

The first run will open a browser for Gmail OAuth. After that, it runs instantly with no browser needed.

## Tech Stack

- **[Claude API](https://docs.anthropic.com)** (Anthropic) — generates the brief
- **Gmail API** (Google) — fetches unread emails
- **[DDGS](https://github.com/deedy5/ddgs)** — free web search, no API key needed
- **Python 3.9+**

## Project Structure

```
ai-daily-brief/
├── brief.py          # Entry point
├── gmail_client.py   # Gmail OAuth + email fetching
├── news_client.py    # Web search for AI news
├── claude_client.py  # Claude API integration
├── requirements.txt
└── .env.example
```

## License

MIT
