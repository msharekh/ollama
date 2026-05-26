# ollama 

### Ollama 

>is the easiest way to get up and running with large language models such as gpt-oss, Gemma 3, DeepSeek-R1, Qwen3 and more


## install
PS C:\Users\Personal\Documents\Development\Ai\ollama> irm https://ollama.com/install.ps1 | iex
>>> Downloading Ollama for Windows...
######################################## 100.0%
>>> Installing Ollama...
>>> Install complete. Run 'ollama' from the command line.

 ollama version is 0.24.0
 
 ## models
 
 https://ollama.com/library
smallest: ollama run gemma3

ollama list

## run
ollama serve

success
>>> hello
Hello there! How's your day going so far? 😊

Is there anything you'd like to talk about, or were you just
saying hello?

>>> /?
Available Commands:
  /set            Set session variables
  /show           Show model information
  /load <model>   Load a session or model
  /save <model>   Save your current session
  /clear          Clear session context
  /bye            Exit
  /?, /help       Help for a command
  /? shortcuts    Help for keyboard shortcuts

Use """ to begin a multi-line message.
Use \path\to\file to include .jpg, .png, .webp images, or .wav audio files.


http://localhost:11434
Ollama is running

## create app (client)

pip install ollama

C:\Users\Personal\Documents\Development\Ai\ollama

 import ollama

client = ollama.Client()

model = "gemma3"
prompt = "What is the capital of France?"

#send a prompt to the model and get the response
response = client.generate(model=model, prompt=prompt)

#print the response
print("response from the model")
print(response.response)