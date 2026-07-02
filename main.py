from pdf_processor import extract_text
from rag import chunk_text, retrieve
from embedding import (
    model,
    generate_embeddings
)
from llm import answer_question


pdf_path = input(
    "Enter PDF path: "
)

print("Reading PDF...")

text = extract_text(
    pdf_path
)

print("Chunking text...")

chunks = chunk_text(text)

print("Generating embeddings...")

embeddings = generate_embeddings(
    chunks
)

print(
    f"Loaded {len(chunks)} chunks."
)

history = []

while True:
    query = input(
        "\nAsk a question (exit to quit): "
    )

    if query.lower() == "exit":
        break

    top_chunks = retrieve(
        query,
        chunks,
        embeddings,
        model
    )

    context = "\n".join(
        top_chunks
    )

    history_text = "\n".join(
        history
    )

    answer = answer_question(
        query,
        context,
        history_text
    )

    print("\nAnswer:\n")
    print(answer)

    history.append(
        f"User: {query}"
    )

    history.append(
        f"Assistant: {answer}"
    )