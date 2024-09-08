import ollama
import sys


response = ollama.chat(model='llama3_tech', messages=[
  {
    'role': 'user',
    'content': 'create an ssh connection using the following command to connect to an arch linux system   ssh -p 3022 llm_arch@127.0.0.1 ',
    'stream':True,
  },
])
print(response['message']['content'])

