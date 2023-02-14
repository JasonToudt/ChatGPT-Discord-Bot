from dotenv import load_dotenv
import openai
import os

#Import environment variables in .env file
load_dotenv()

#Setting API_KEY variable from .env file
openai.api_key = os.getenv('API_KEY')

#Function to take prompt from the user
def chatgpt_response(prompt):
    response = openai.Completion.create(
        #API request body
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=2048
    )
    
    #Assigning variables to extract response text from AI JSON response
    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response
