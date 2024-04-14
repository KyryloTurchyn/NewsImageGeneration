import requests

# Setup
SYSTEM_PROMPT = ("your job is to generate detailed prompts that start with generate the abstract preview-image which describe "
                 "summary of journalistic article, for image generation models based on user summary. Make prompt "
                 "which can cleaely describe what happend in summary.Be descriptive and specific, but also make sure "
                 "your prompts are clear and concise.")
zephyr_7b_beta = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta/"
HF_TOKEN = "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"  # Ensure you have set your Hugging Face token in an environment
# variable named HF_TOKEN
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}


# Functions
def post_request_beta(payload):
    """
    Sends a POST request to the Hugging Face inference API and returns the JSON response.
    """
    response = requests.post(zephyr_7b_beta, headers=HEADERS, json=payload)
    response.raise_for_status()  # Will raise an HTTPError for bad requests
    return response.json()


def predict_beta(message, system_prompt=SYSTEM_PROMPT):
    """
    Generates a prompt using the provided message and system prompt.
    """
    input_prompt = f"{system_prompt}\n\nUser: {message}\nLLM:"
    data = {"inputs": input_prompt}
    try:
        response_data = post_request_beta(data)
        json_obj = response_data[0]
        # Extract only the generated text after the last occurrence of the user message
        generated_text = json_obj.get('generated_text', "No response generated")
        if message in generated_text:
            # Find the last occurrence of the user message and extract the text after it
            generated_text = generated_text.split(message)[-1].strip()[5:]
        return generated_text
    except requests.HTTPError as e:
        print(f"Request failed with status code {e.response.status_code}: {e.response.text}")
        return None
