import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class SummarizationModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

    def summerize(self, text):
        """
        Summarizes the input text into a shorter form using the tokenizer and model.

        This method handles text input, tokenizes the input without truncation, and processes it in chunks.
        For each chunk, it finds a suitable end index that doesn't break a word. Each chunk is then fed to the model
        to generate a summary. All summaries are concatenated to form the final summarized text.

        Parameters:
        text (str): The text to be summarized.

        Returns:
        str: The summarized text as a single string.
        """
        inputs_no_trunc = self.tokenizer(text, max_length=None, return_tensors='pt', truncation=False)

        chunk_start = 0
        chunk_end = 1024
        #chunk_end = self.tokenizer.model_max_length  # == 1024 for Bart
        inputs_batch_lst = []
        space_token_id = self.tokenizer.encode(' ', add_special_tokens=False)[0]

        while chunk_start <= len(inputs_no_trunc['input_ids'][0]):
            try:
                current_chunk = inputs_no_trunc['input_ids'][0][chunk_start:chunk_end].tolist()
                end_index = len(current_chunk) - 1 - current_chunk[::-1].index(space_token_id)
                chunk_end = chunk_start + end_index
            except ValueError:
                pass

            inputs_batch = inputs_no_trunc['input_ids'][0][chunk_start:chunk_end]  # get batch of n tokens
            inputs_batch = torch.unsqueeze(inputs_batch, 0)
            inputs_batch_lst.append(inputs_batch)
            chunk_start = chunk_end + 1
            chunk_end = min(chunk_start + self.tokenizer.model_max_length, len(inputs_no_trunc['input_ids'][0]))

        summary_ids_lst = [self.model.generate(inputs, num_beams=4, max_length=1024, early_stopping=True) for inputs in
                           inputs_batch_lst]

        summary_batch_lst = []
        for summary_id in summary_ids_lst:
            summary_batch = [self.tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in
                             summary_id]
            summary_batch_lst.append(summary_batch[0])
        summary_all = '\n'.join(summary_batch_lst)
        return summary_all