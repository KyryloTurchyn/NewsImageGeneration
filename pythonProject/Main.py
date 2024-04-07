from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from ParserClass import Parser
from SummarizationModel import SummarizationModel
from StableDiffusionModel import StableDiffusionModel

if __name__ == '__main__':
    text_from_url = Parser.parse("https://www.washingtonpost.com/politics/2024/04/06/trump-fundraising-dinner/")

    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model_type = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    summarizer_model = SummarizationModel(tokenizer, model_type)
    summary = summarizer_model.summerize(text_from_url, 100)

    diffusion_model = StableDiffusionModel(
        model_name="stabilityai/stable-diffusion-xl-base-1.0",
        repo_name="ByteDance/SDXL-Lightning",
        checkpoint_name="sdxl_lightning_8step_unet.safetensors"
    )
    prompt = "Enter your prompt here"
    diffusion_model.generate_image(prompt)

"""
classes for text extracting and summarizing from sites
site - class
https://www.theguardian.com/ - dcr-4cudl2
https://www.washingtonpost.com - wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy
https://edition.cnn.com/ - paragraph inline-placeholder
"""
