from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from ParserClass import Parser
from SummarizationModel import Model


if __name__ == '__main__':
    text_from_url = Parser.parse("https://www.washingtonpost.com/politics/2024/04/06/trump-fundraising-dinner/")

    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    summarizer_model = Model(tokenizer, model)
    summary = summarizer_model.summerize(text_from_url, 100)


"""
https://www.theguardian.com/ - dcr-4cudl2
https://www.washingtonpost.com - wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy
https://edition.cnn.com/ - paragraph inline-placeholder
"""