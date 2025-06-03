import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSequenceClassification, pipeline
import torch
import numpy as np

# === CARREGAR OS MODELOS GERADORES ===
generator_1_name = "pierreguillou/gpt2-small-portuguese"
generator_2_name = "pierreguillou/gpt2-small-portuguese"  # Usando o mesmo por simplicidade/teste

tokenizer_1 = AutoTokenizer.from_pretrained(generator_1_name)
model_1 = AutoModelForCausalLM.from_pretrained(generator_1_name)

tokenizer_2 = AutoTokenizer.from_pretrained(generator_2_name)
model_2 = AutoModelForCausalLM.from_pretrained(generator_2_name)

# === CARREGAR MODELO ÁRBITRO (BERT) ===
judge_model_name = "neuralmind/bert-base-portuguese-cased"
judge_tokenizer = AutoTokenizer.from_pretrained(judge_model_name)
judge_model = AutoModelForSequenceClassification.from_pretrained(judge_model_name, num_labels=2)

# Classificador de similaridade (baseado em relevância para o prompt)
def score_response(prompt, response):
    inputs = judge_tokenizer(prompt, response, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = judge_model(**inputs)
    score = torch.softmax(outputs.logits, dim=1)[0][1].item()  # Probabilidade da classe "boa"
    return score

# Gerar resposta com modelo
def generate_response(model, tokenizer, prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output_ids = model.generate(input_ids, max_new_tokens=60, num_return_sequences=1, do_sample=True)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Função principal
def chatbot(prompt):
    response_1 = generate_response(model_1, tokenizer_1, prompt)
    response_2 = generate_response(model_2, tokenizer_2, prompt)

    score_1 = score_response(prompt, response_1)
    score_2 = score_response(prompt, response_2)

    if score_1 > score_2:
        final = response_1
        chosen = "Resposta 1"
    else:
        final = response_2
        chosen = "Resposta 2"

    return (
        prompt,
        response_1,
        response_2,
        chosen,
        final
    )

# === INTERFACE GRADIO ===
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(label="Digite sua pergunta"),
    outputs=[
        gr.Textbox(label="Prompt"),
        gr.Textbox(label="Resposta 1"),
        gr.Textbox(label="Resposta 2"),
        gr.Textbox(label="Resposta escolhida pelo árbitro"),
        gr.Textbox(label="Resposta final exibida")
    ],
    title="Chatbot em Cascata (Português)",
    description="Dois modelos geram respostas e um árbitro (BERT) escolhe a melhor."
)

if __name__ == "__main__":
    iface.launch()
