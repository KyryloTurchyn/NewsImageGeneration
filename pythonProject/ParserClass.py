from LxmlSoup import LxmlSoup
import requests


class Parser:
    def __init__(self):
        pass

    @staticmethod
    def parse(url: str) -> str:
        html = requests.get(url).text
        soup = LxmlSoup(html)
        paragraphs = soup.find_all('p', class_='wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy')
        full_text = ' '.join(paragraph.text() for paragraph in paragraphs)
        return full_text
