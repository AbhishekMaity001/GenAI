# import requests
# # from utils.config import WIKI_API_URL
# WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

# def search_wikipedia(query):
#     params = {
#         "action": "query",
#         "format": "json",
#         "prop": "extracts",
#         "exintro": True,
#         "explaintext": True,
#         "titles": query
#     }

#     response = requests.get(WIKI_API_URL, params=params).json()
#     page = next(iter(response["query"]["pages"].values()))

#     return page.get("extract", "")


import requests

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

def search_wikipedia(query):
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": query,
    }

    response = requests.get(WIKI_API_URL, params=params,headers= {"User-Agent": "MyApp/1.0"}, timeout=10)

    # 1️⃣ Ensure HTTP request succeeded
    response.raise_for_status()

    # 2️⃣ Ensure response is JSON
    try:
        data = response.json()
    except ValueError:
        raise RuntimeError(
            f"Wikipedia returned non-JSON response: {response.text[:200]}"
        )

    # 3️⃣ Safely extract page
    pages = data.get("query", {}).get("pages", {})
    if not pages:
        return ""

    page = next(iter(pages.values()))

    # 4️⃣ Handle missing pages
    if "missing" in page:
        return ""

    return page.get("extract", "")
