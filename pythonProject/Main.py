import warnings
warnings.filterwarnings("ignore")

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from ParserClass import Parser
from SummarizationModel import SummarizationModel
from StableDiffusionModel import StableDiffusionModel
from PromptModel import *

if __name__ == '__main__':
    url = "https://edition.cnn.com/2024/04/05/tech/meta-nonprofit-newspaper-independent-journalist-alleged-censorship/index.html"

    text_from_url = Parser.parse(url)

    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    summarizer_model = SummarizationModel(tokenizer, model)
    summary = summarizer_model.summerize(text_from_url)
    print(summary)
    prompt = predict_beta(summary + "4k, photorealistic")

    diffusion_model = StableDiffusionModel(
        model_name="stabilityai/stable-diffusion-xl-base-1.0",
        repo_name="ByteDance/SDXL-Lightning",
        checkpoint_name="sdxl_lightning_8step_unet.safetensors")

    diffusion_model.generate_image(prompt)
