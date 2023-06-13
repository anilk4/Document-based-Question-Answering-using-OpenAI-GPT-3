import openai

# Set your OpenAI API key
openai.api_key = "Your Open AI Key"

# Load the documents from the files
documents = {}
for i in range(1, 4):
    with open(f"document{i}.txt", "r") as file:
        documents[f"document{i}.txt"] = file.read()

# Ask a question
question = "What is the origin of Mount Everest?"

# Initialize the variables for answer and origin
answer = ""
origin = ""

# Iterate through the documents and find the answer
for document_name, document_text in documents.items():
    # Combine the question and document into a single string
    prompt = f"Question: {question}\nDocument: {document_text}\nAnswer:"

    # Use OpenAI's GPT-3 API to answer the question based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

    # Extract the answer from the response
    answer = response.choices[0].text.strip()

    # Check if the answer is not empty
    if answer:
        origin = document_name
        break

# Print the answer and its origin
print("Answer:", answer)
print("Origin:", origin)
