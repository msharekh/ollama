import ollama
import chromadb
import pypdf

PERSIST_DIR = "./chroma_db"
PDF_PATH = "popular_car_prices_2021_2026.pdf"

chromadb_client = chromadb.PersistentClient(path=PERSIST_DIR)
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
    upload_pdf(PDF_PATH)


while True:
    prompt = input("Enter your prompt: ").strip()

    while not prompt:
        prompt = input("Prompt cannot be empty. Enter your prompt: ").strip()

    closest_pages = collection.query(
        query_texts=[prompt],
        n_results=1,
    )

    messages = []
    docs = closest_pages.get("documents", [])

    if docs and docs[0]:
        messages.append({"role": "system", "content": docs[0][0]})

    messages.append({"role": "user", "content": prompt})

    response = ollama.chat(
        model=model,
        messages=messages,
    )

    print("response from the model")
    print(response.message.content)

    again = input("Do you want to ask another request? (y/n): ").strip().lower()

    while again not in {"y", "yes", "n", "no"}:
        again = input("Please enter y or n: ").strip().lower()

    if again in {"n", "no"}:
        break