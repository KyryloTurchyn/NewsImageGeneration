from LxmlSoup import LxmlSoup
import requests


def select_class(url: str) -> str:
    if "https://www.theguardian.com/" in url:
        parse_class = "dcr-4cudl2"
    elif "https://www.washingtonpost.com" in url:
        parse_class = "wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy"
    else:
        parse_class = "paragraph inline-placeholder"
    return parse_class


class Parser:
    def __init__(self):
        pass

    def select_class(url: str) -> str:
        if "https://www.theguardian.com/" in url:
            parse_class = "dcr-4cudl2"
        elif "https://www.washingtonpost.com" in url:
            parse_class = "wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy"
        else:
            parse_class = "paragraph inline-placeholder"
        return parse_class

    def parse(self: str) -> str:
        html = requests.get(self).text
        soup = LxmlSoup(html)
        paragraphs = soup.find_all('p', class_=select_class(self))
        full_text = ' '.join(paragraph.text() for paragraph in paragraphs)
        return full_text