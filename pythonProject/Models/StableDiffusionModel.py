import torch
from diffusers import UNet2DConditionModel, StableDiffusionXLPipeline, EulerDiscreteScheduler
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file


class StableDiffusionModel:
    def __init__(self, model_name, repo_name, checkpoint_name, device='cuda'):
        self.model_name = model_name
        self.repo_name = repo_name
        self.checkpoint_name = checkpoint_name
        self.device = device
        self.pipe = self.setup_pipeline()

    def setup_pipeline(self):
        """
        Set up the Stable Diffusion XL pipeline by loading the model and the associated U-Net architecture.
        The function initializes the U-Net model from configuration, downloads the checkpoint, and sets up the pipeline.

        Returns:
        StableDiffusionXLPipeline: A pipeline object that is ready for inference with the Stable Diffusion model.
        """
        unet = UNet2DConditionModel.from_config(self.model_name, subfolder="unet").to(self.device, torch.float16)
        unet.load_state_dict(load_file(hf_hub_download(self.repo_name, self.checkpoint_name), device=self.device))
        pipe = StableDiffusionXLPipeline.from_pretrained(self.model_name, unet=unet, torch_dtype=torch.float16,
                                                         variant="fp16").to(self.device)
        pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")
        return pipe

    def generate_image(self, prompt: str):
        """
        Generate an image from a text prompt using the Stable Diffusion XL pipeline.

        Parameters:
        prompt (str): The prompt text used to generate the image.

        Saves:
        The generated image is saved as 'output.png' in the 'static' directory.

        Returns:
        Image: The generated image as a PIL Image object.
        """
        image = self.pipe(prompt, num_inference_steps=8, guidance_scale=0, ).images[0]
        image.save("static/output.png")
        print(123)
        return image
