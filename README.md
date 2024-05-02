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

![trump 1](https://github.com/KyryloTurchyn/NewsImageGeneration/assets/64077721/396689ea-1aa5-425e-b1dc-af9ab63a94df)


[Irish moonshine and the village that declared itself an outlaw republic](https://edition.cnn.com/travel/urris-donegal-moonshine-poitin-outlaw-republic/index.html)

![ireland 1](https://github.com/KyryloTurchyn/NewsImageGeneration/assets/64077721/89559a45-1dc0-402d-979e-e57a30de41b3)


[Original cover art for ‘Harry Potter and the Philosopher’s Stone’ expected to set auction record](https://www.theguardian.com/music/article/2024/may/02/yunchan-lim-chopin-etudes-op-10-op-25-album-review)
![harry 1](https://github.com/KyryloTurchyn/NewsImageGeneration/assets/64077721/1b1df3d5-0ecb-41d0-812f-5315bbce976c)

[Who was Alexei Navalny, Russian opposition leader and Putin critic?](https://www.washingtonpost.com/world/2024/02/16/alexei-navalny-death-what-to-know/)
![lexa 1](https://github.com/KyryloTurchyn/NewsImageGeneration/assets/64077721/9d63b8ec-2656-4906-849e-7e4529f37f3d)
