import openai
import os
from dotenv import load_dotenv

# Load the contents of the .env file into the environment variables
load_dotenv()

# Fetch the openai api key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


def invoke_completion_api(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=1000,
        top_p=0.1,
        presence_penalty=0,
        frequency_penalty=0,
    )
    print(
        {
            "openai_prompt": prompt,
            "openai_response": response,
        }
    )
    response_text = response.choices[0].text
    return response_text
