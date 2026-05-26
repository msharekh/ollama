import ollama
import chromadb
import pypdf

chromadb_client = chromadb.Client()
collection = chromadb_client.get_or_create_collection("pdf_collection")


def upload_pdf(file_path):
    with open(file_path, "rb") as file:
        pdf_reader = pypdf.PdfReader(file)

    for doc_id, page in enumerate(pdf_reader.pages):
        text = page.extract_text()
        if text:
            collection.add(
                documents=[text],
                ids=[f"{file_path}_{doc_id}"],
            )


client = ollama.Client()
model = "gemma3"

if collection.count() == 0:
    upload_pdf("popular_car_prices_2021_2026.pdf")


while True:
    prompt = input("Enter your prompt: ").strip()

    while not prompt:
        prompt = input("Prompt cannot be empty. Enter your prompt: ").strip()

    closest_pages = collection.query(
        query_texts=[prompt],
        n_results=3,
    )

    messages = []
    docs = closest_pages.get("documents", [])

    if docs and docs[0]:
        for doc in docs[0][:3]:
            messages.append({"role": "system", "content": doc})

    messages.append({"role": "user", "content": prompt})

    response = ollama.chat(
        model=model,
        messages=messages,
    )

    print("response from the model")
    print(response.response)

    again = input("Do you want to ask another request? (y/n): ").strip().lower()

    while again not in {"y", "yes", "n", "no"}:
        again = input("Please enter y or n: ").strip().lower()

    if again in {"n", "no"}:
        break