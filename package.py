import ollama

client = ollama.Client()

model = "gemma3"

while True:
    prompt = input("Enter your prompt: ").strip()

    while not prompt:
        prompt = input("Prompt cannot be empty. Enter your prompt: ").strip()

    #send a prompt to the model and get the response
    response = client.generate(model=model, prompt=prompt)

    #print the response
    print("response from the model")
    print(response.response)

    again = input("Do you want to ask another request? (y/n): ").strip().lower()

    while again not in {"y", "yes", "n", "no"}:
        again = input("Please enter y or n: ").strip().lower()

    if again in {"n", "no"}:
        break