import warnings
warnings.filterwarnings("ignore")

from Utils import ParserClass
from Models import SummarizationModel, PromptModel, StableDiffusionModel

if __name__ == '__main__':
    url = "https://www.theguardian.com/world/2024/mar/17/vladimir-putin-claims-prisoner-swap-alexei-navalny"

    parser = ParserClass(url)
    text_from_url = parser.parse()

    summarizer_model = SummarizationModel()
    summary = summarizer_model.summerize(text_from_url)
    print(summary)
    hf_api = PromptModel("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")
    prompt = hf_api.generate_prompt(summary)
    print(prompt)
    diffusion_model = StableDiffusionModel(
        model_name="stabilityai/stable-diffusion-xl-base-1.0",
        repo_name="ByteDance/SDXL-Lightning",
        checkpoint_name="sdxl_lightning_8step_unet.safetensors")

    diffusion_model.generate_image(prompt)
