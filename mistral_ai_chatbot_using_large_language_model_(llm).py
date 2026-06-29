 

!pip install -q ctransformers jupyter_bokeh panel





import panel as pn
from ctransformers import AutoModelForCausalLM
 
pn.extension()

llm = AutoModelForCausalLM.from_pretrained(
    "TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
    model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    model_type="mistral",
    gpu_layers=0
)

print("✅ Mistral model loaded successfully!")

prompt = "AI is going to"

response = llm(
    prompt,
    max_new_tokens=100,
    temperature=0.7
)

print("Prompt:")
print(prompt)

print("\nResponse:")
print(response)

llms = {}

async def callback(contents: str, user: str, instance):

    global llm

    response = llm(
        contents,
        stream=True,
        max_new_tokens=300,
        temperature=0.7
    )

    message = ""

    for token in response:
        message += token
        yield message

!pip install -q gradio

import gradio as gr

def chat(message, history):
    response = llm(
        message,
        max_new_tokens=300,
        temperature=0.7
    )
    return response

demo = gr.ChatInterface(
    fn=chat,
    title="🤖 Mistral Chatbot"
)

demo.launch()

import gradio as gr

def chat(message, history):
    response = llm(
        message,
        max_new_tokens=100,
        temperature=0.7
    )
    return response

demo = gr.ChatInterface(
    fn=chat,
    title="🤖 Mistral Chatbot"
)

demo.launch(share=True)

print(llm)

demo.launch()

