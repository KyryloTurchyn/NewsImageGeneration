## Overview
This programme allows to get preview images for journalistic articles from "WashingtonPost", "CNN" or "The Guardian" websites with the use of the Facebook [BART](https://huggingface.co/facebook/bart-large-cnn) text generation model, the [zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) promt generation model and the 8-steps [SDXL-Lightning](https://huggingface.co/ByteDance/SDXL-Lightning) stackable diffusion model.
## Instalation
```
git clone https://github.com/KyryloTurchyn/NewsImageGeneration
pip install -r requirements.txt
```
Since image generation is done using CUDA, you will need to activate it. You can use the official [Pytorch website](https://pytorch.org/), but for Windows it will probably be:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
After that, you will need to go to the directory and run app.py
```
cd pythonProject
python.py
```
## Structure of the project
```
pythonProject/
│
├── Models/
│   ├── __init__.py             # Initializes the Models package
│   ├── PromptModel.py          # Module for the prompt generation model
│   ├── StableDiffusionModel.py # Module for the stable diffusion model
│   └── SummarizationModel.py   # Module for the text summarization model
│
├── static/
│   └── output.png              # Static image file for the web interface
│
├── templates/
│   └── index.html              # HTML template for the main page of the web application
│
└── Utils/
    ├── __init__.py             # Initializes the Utils package
    └── ParserClass.py          # Module with parser class
│
└── app.py                      # Main file for the Flask application
└── logic.py                    # Module containing the business logic of the application
```
## How does it work
1) **Parsing** - you pass a link to the article into the code. Then all the text from the site is parsed.
2) **Summarization** - for the prompt model to generate a good prompt, we need to summarise the text.
3) **Prompting** - on the basis of summery and base prompt a separate prompt is prepared in the image generation model
4) **Image Generation** - the image is generated on the basis of the existing promt, which is specially generated for the preview photo. 
## Examples of work
[Trump in ‘full sprint’ to close Biden’s money lead as legal bills mount](https://www.washingtonpost.com/politics/2024/04/06/trump-fundraising-dinner/)
[Irish moonshine and the village that declared itself an outlaw republic](https://edition.cnn.com/travel/urris-donegal-moonshine-poitin-outlaw-republic/index.html)
[Sea of Thieves on PlayStation 5 review – you’ll laugh, you’ll sail, you’ll drink grog until you’re sick](https://www.theguardian.com/games/2024/may/02/sea-of-thieves-on-playstation-5-review-youll-laugh-youll-sail-youll-drink-grog-until-youre-sick)
[Who was Alexei Navalny, Russian opposition leader and Putin critic?](https://www.washingtonpost.com/world/2024/02/16/alexei-navalny-death-what-to-know/)