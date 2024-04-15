import warnings
warnings.filterwarnings("ignore")

from Utils import ParserClass
from Models import SummarizationModel, PromptModel, StableDiffusionModel


def logic_function(url:str) -> str:
    parser = ParserClass(url)
    text_from_url = parser.parse()

    summarizer_model = SummarizationModel()
    summary = summarizer_model.summerize(text_from_url)

    hf_api = PromptModel("HF_TOKEN")
    prompt = hf_api.generate_prompt(summary)

    diffusion_model = StableDiffusionModel(
        model_name="stabilityai/stable-diffusion-xl-base-1.0",
        repo_name="ByteDance/SDXL-Lightning",
        checkpoint_name="sdxl_lightning_8step_unet.safetensors")

    diffusion_model.generate_image(prompt)

