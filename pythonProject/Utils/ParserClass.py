from LxmlSoup import LxmlSoup
import requests


class ParserClass:
    def __init__(self, url):
        self.url = url
        self.parse_class = self.select_class(url)

    def select_class(self, url: str) -> str:
        if "https://www.theguardian.com/" in url:
            parse_class = "dcr-4cudl2"
        elif "https://www.washingtonpost.com" in url:
            parse_class = "wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy"
        else:
            parse_class = "paragraph inline-placeholder"
        return parse_class

    def parse(self) -> str:
        html = requests.get(self.url).text
        soup = LxmlSoup(html)
        paragraphs = soup.find_all('p', class_=self.parse_class)
        full_text = ' '.join(paragraph.text() for paragraph in paragraphs)
        return full_text
