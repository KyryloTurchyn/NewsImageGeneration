from ParserClass import Parser

if __name__ == '__main__':
    text = Parser.parse("https://www.washingtonpost.com/politics/2024/04/06/trump-fundraising-dinner/")
    print(text)

"""
https://www.theguardian.com/ - dcr-4cudl2
https://www.washingtonpost.com - wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy
https://edition.cnn.com/ - paragraph inline-placeholder
"""