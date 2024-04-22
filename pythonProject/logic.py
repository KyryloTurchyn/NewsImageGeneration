import warnings
warnings.filterwarnings("ignore")

from Utils import ParserClass
from Models import SummarizationModel, PromptModel, StableDiffusionModel


def logic_function(url: str):
    """
    Process the provided URL to summarize its content, generate a prompt, and create an image from the prompt.

    Parameters:
    url (str): A string containing the URL to be processed.

    Returns:
    None: This function does not return anything as it performs generation of an image directly.
    """
    parser = ParserClass(url)
    text_from_url = parser.parse()

    summarizer_model = SummarizationModel()
    summary = summarizer_model.summerize(text_from_url)

    hf_api = PromptModel("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")
    prompt = hf_api.generate_prompt(summary)

    diffusion_model = StableDiffusionModel(
        model_name="stabilityai/stable-diffusion-xl-base-1.0",
        repo_name="ByteDance/SDXL-Lightning",
        checkpoint_name="sdxl_lightning_8step_unet.safetensors")

    diffusion_model.generate_image(prompt)
