# 🤖 Chatbot em Cascata – Projeto Acadêmico

## 📝 Descrição
Este projeto implementa um chatbot em português baseado em arquitetura **em cascata**, onde dois modelos diferentes geram respostas a partir de um prompt do usuário, e um terceiro modelo atua como **árbitro**, escolhendo a melhor resposta com base em critérios objetivos.

O web app foi desenvolvido utilizando **Gradio** e está hospedado no **Hugging Face Spaces**.

## 🚧 Funcionamento do Sistema

1. **Usuário insere uma pergunta (prompt).**
2. **Dois modelos geradores** processam o prompt e produzem **duas respostas independentes**.
3. **Um terceiro modelo (árbitro)** analisa as duas respostas e seleciona a que melhor atende aos critérios definidos.
4. **A resposta escolhida é exibida ao usuário**, juntamente com as duas respostas e a justificativa da escolha.

## ⚙️ Modelos Utilizados

### 📤 Modelos Geradores

1. **pierreguillou/gpt2-small-portuguese**
   - Baseado no GPT-2, treinado especificamente em português.
   - Modelo leve (124M parâmetros), ideal para ambientes com 2vCPU e 16GB RAM.
   - Utilizado para gerar texto de maneira autônoma e fluente em português.

> Ambos os geradores usam o mesmo modelo neste exemplo, mas podem ser trocados por versões distintas.

### ⚖️ Modelo Árbitro

- **neuralmind/bert-base-portuguese-cased**
  - Versão do BERT treinada em português brasileiro.
  - Utilizado para comparar o prompt com cada resposta, avaliando **clareza**, **relevância** e **coerência**.

## 📊 Critérios de Avaliação do Árbitro

| Critério     | Definição                                                              |
|--------------|-------------------------------------------------------------------------|
| Clareza      | A resposta está bem formulada e compreensível?                          |
| Relevância   | A resposta realmente responde ao prompt do usuário?                    |
| Coerência    | A resposta é lógica e gramaticalmente correta?                         |

> A avaliação é feita através da **similaridade semântica** entre o prompt e cada resposta.

## 🖥️ Requisitos de Hardware

- CPU: 2 vCPU  
- RAM: 16 GB  
- Armazenamento: suficiente para carregar 3 modelos pequenos

## 🌐 Tecnologias Utilizadas

- [Gradio](https://www.gradio.app/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Hugging Face Spaces](https://huggingface.co/spaces)
- PyTorch

## 🚀 Executando Localmente

```bash
git clone https://huggingface.co/spaces/SlickSlick/Chatbot-cascata-fmu
cd Chatbot-cascata-fmu
pip install -r requirements.txt
python app.py
```

## 🧪 Exemplos de Uso

**Prompt:** "Qual é a capital do Brasil?"

- **Resposta 1:** "A capital do Brasil é Brasília."
- **Resposta 2:** "Rio de Janeiro é uma cidade importante do Brasil."
- **Escolhida pelo Árbitro:** Resposta 1
- **Justificativa:** Resposta 1 é mais clara, direta e responde exatamente à pergunta.

## 📬 Contato e Autoria

- **Projeto acadêmico desenvolvido por:** Gabriel dos Reis Rodrigues Dias  
- **Curso:** Ciência da Computação  
- **Universidade:** Centro Universitário das Faculdades Metropolitanas Unidas – FMU  
- **Professor:** Renè Teixeira
