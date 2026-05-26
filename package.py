import ollama

client = ollama.Client()

model = "gemma3"
prompt = "What is the capital of France?"

#send a prompt to the model and get the response
response = client.generate(model=model, prompt=prompt)

#print the response
print("response from the model")
print(response.response)