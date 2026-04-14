from datetime import date
from ddgs import DDGS


def get_ai_news(max_results=5):
    today = date.today().strftime("%B %d, %Y")
    query = f"AI news {today}"

    results = []
    with DDGS() as ddgs:
        for r in ddgs.news(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "url": r.get("url", ""),
                "body": r.get("body", "")[:400],
            })

    return results
