

import torch
from transformers import BertTokenizer, BertModel

# Load the BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Encode the text input as a sequence of token-ids
input_ids = torch.tensor([tokenizer.encode("Here is a sample input text.", add_special_tokens=True)])

# Load the BERT model
model = BertModel.from_pretrained('bert-base-uncased')

# Put the model in evaluation mode
model.eval()

# Forward pass the encoded text through the model
with torch.no_grad():
    outputs = model(input_ids)
    last_hidden_states = outputs[0]  # The last hidden state is the representation of the input text
