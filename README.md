# AI Daily Brief

> A CLI tool that pulls your unread Gmail, searches for the latest AI news, and delivers a formatted morning briefing — all in under 30 seconds.

## Demo

> Demo GIF coming soon — see [Setup](#setup) to run locally.

## What This Does

Most people start their day scanning email and checking news separately. This tool combines both into a single terminal command: unread emails get summarized, the latest AI developments from the past 24 hours get surfaced, and Claude synthesizes everything into a clean brief you can read in two minutes.

Built for developers and operators who work with AI tools daily and need to stay current — without the noise.

## How It Works

```
python brief.py
      │
      ▼
Gmail API → fetch unread emails → summarize
      │
      ▼
DDGS search → "AI news last 24h" → top results
      │
      ▼
Claude API → synthesize → formatted brief
      │
      ▼
Terminal output
```

## Example Output

```
=== YOUR DAILY BRIEF ===

EMAIL SUMMARY
- Invoice received (Notion, €12.00) — auto-payment, no action needed
- 2 client inquiries via contact form — follow up today
- GitHub: pull request merged on ai-business-research-agent

AI NEWS
- Anthropic releases Claude claude-sonnet-4-6 with extended context
- OpenAI announces GPT-5 developer access rollout
- Google DeepMind publishes reasoning benchmark results

FOCUS
Two leads need replies. Block 30 minutes this morning.
```

## Tech Stack

| Component | Technology |
|---|---|
| AI | Claude API (Anthropic) |
| Email | Gmail API (OAuth2) |
| News | DDGS (DuckDuckGo Search — no API key needed) |
| Language | Python 3.9+ |

## Setup

**1. Clone and install:**
```bash
git clone https://github.com/theokalogr-bit/ai-daily-brief
cd ai-daily-brief
pip install -r requirements.txt
```

**2. Add your Anthropic API key:**
```bash
cp .env.example .env
# Edit .env: add ANTHROPIC_API_KEY
```

**3. Configure Gmail OAuth:**
- Go to [Google Cloud Console](https://console.cloud.google.com)
- Create a project → Enable Gmail API → Download `credentials.json`
- Place `credentials.json` in the project root
- First run opens a browser for OAuth — authentication persists after that

**4. Run:**
```bash
python brief.py
```

## Use Cases

- **AI developers and consultants** — stay informed on the tools you build with, without opening a browser every morning
- **Operators and founders** — combine email triage and industry news into a single 2-minute daily ritual
- **Anyone using Claude Code** — connect to your inbox and get context before starting your day

---
Built by [Theo](https://github.com/theokalogr-bit) — AI automation consultant based in Greece.
