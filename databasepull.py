# SQL DATABASE for AI
# Slava
import openai


openai.api_key = "org-06K6M21iUb96lU9q74tenur4"



# Replace 'your-api-key-here' with your actual API key

def continuous_chat(prompt, conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *conversation,
            {"role": "user", "content": prompt},
        ],
    )
    return response['choices'][0]['message']['content']

def main():
    conversation = []
    response = continuous_chat("What is machine learning?", conversation)
    print(response)

if __name__ == "__main__":
    main()
