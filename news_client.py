from datetime import date
from ddgs import DDGS


def get_ai_news(max_results=5):
    today = date.today().strftime("%B %d, %Y")
    query = f"AI artificial intelligence news {today}"

    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "url": r.get("href", ""),
                "body": r.get("body", "")[:400],
            })

    return results
