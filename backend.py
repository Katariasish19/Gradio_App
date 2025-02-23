import os
from dotenv import dotenv_values
import openai
from openai import AzureOpenAI

# Load the .env file
config = dotenv_values("config.env")

# Set OpenAI API credentials
client = AzureOpenAI(
    api_key = config["AZURE_OPENAI_API_KEY"],
    azure_endpoint = config["AZURE_OPENAI_ENDPOINT"],
    # api_type = "azure",
    api_version = config["AZURE_OPENAI_API_VERSION"])

def generate_documentation(file):
    """
    Reads a C# code file and generates documentation using Azure OpenAI.
    """
    with open(file.name, "r") as f:
        code = f.read()

    prompt = f"Generate documentation for the following C# code:\n\n{code}\n\n### Documentation:"
    
    # Use the ChatCompletion API
    response = client.chat.completions.create(
        model = config["AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"],
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates documentation."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        temperature=0.5
    )

    # Return the response text
    documentation =  response.choices[0].message.content
    return documentation.strip()

