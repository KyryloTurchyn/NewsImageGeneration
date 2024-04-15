import requests



class PromptModel:
    def __init__(self, api_token):
        self.api_token = api_token
        self.api_url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
        self.headers = {"Authorization": f"Bearer {api_token}"}
        self.system_prompt = ("your job is to generate detailed prompts that start with generate the abstract "
                              "photo in 4k which describe summary of journalistic article, for image generation models"
                              "based on user summary. Make prompt which can clearly describe what happened in summary. "
                              "Be descriptive and specific, but also make sure your prompts are clear and concise.")

    def post_request(self, payload):
        """
        Sends a POST request to the API and returns the JSON response.
        """
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def generate_prompt(self, message):
        """
        Generates a prompt using the provided message and the stored system prompt.
        """
        input_prompt = f"{self.system_prompt}\n\nUser: {message}\nLLM:"
        data = {"inputs": input_prompt}
        try:
            response_data = self.post_request(data)
            json_obj = response_data[0]
            generated_text = json_obj.get('generated_text')
            if message in generated_text:
                generated_text = generated_text.split(message)[1].strip()[5:]
            return generated_text
        except requests.HTTPError as e:
            print(f"Request failed with status code {e.response.status_code}: {e.response.text}")
            return None
