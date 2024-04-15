from LxmlSoup import LxmlSoup
import requests


class ParserClass:
    def __init__(self, url):
        self.url = url
        self.parse_class = self.select_class(url)

    def select_class(self, url: str) -> str:
        """
        Select the appropriate CSS class for parsing the article content
        based on the provided URL's domain.

        Parameters:
        url (str): The URL of the article to be parsed.

        Returns:
        str: The CSS class name to use for parsing the article content.
        """
        if "https://www.theguardian.com/" in url:
            parse_class = "dcr-4cudl2"
        elif "https://www.washingtonpost.com" in url:
            parse_class = "wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy"
        else:
            parse_class = "paragraph inline-placeholder"
        return parse_class

    def parse(self) -> str:
        """
        Parse the article content from the URL provided during class instantiation
        using the CSS class determined by the `select_class` method.

        Returns:
        str: The concatenated string of all paragraph texts within the article.
        """
        html = requests.get(self.url).text
        soup = LxmlSoup(html)
        paragraphs = soup.find_all('p', class_=self.parse_class)
        full_text = ' '.join(paragraph.text() for paragraph in paragraphs)
        return full_text
