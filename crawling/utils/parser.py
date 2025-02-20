from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    topics = []
    for topic in soup.select(".topic"):
        title = topic.select_one(".title").text.strip()
        comments = [c.text.strip() for c in topic.select(".comment")]
        topics.append({"title": title, "comments": comments})
    return topics
