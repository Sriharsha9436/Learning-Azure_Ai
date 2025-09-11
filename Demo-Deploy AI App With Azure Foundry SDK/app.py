import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

def main():
    # Load environment variables from .env file
    load_dotenv()

    endpoint = os.getenv("PROJECT_ENDPOINT")
    model_name = os.getenv("MODEL_DEPLOYMENT_NAME")

    if not endpoint or not model_name:
        raise ValueError("PROJECT_ENDPOINT and MODEL_DEPLOYMENT_NAME must be set in .env file")

    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint, credential)

    # Get chat completions client
    chat_client = project.inference.get_chat_completions_client()

    # Example chat messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how can you assist me today?"}
    ]

    response = chat_client.complete(model=model_name, messages=messages)

    print("Assistant:", response.choices[0].message.content)

if __name__ == "__main__":
    main()
