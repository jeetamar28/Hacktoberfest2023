import openai

# Replace with your API key
api_key = "YOUR_API_KEY"

# Initialize the OpenAI API client
openai.api_key = api_key

def chat_with_gpt3(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Chat loop
print("ChatGPT Clone: Hello! How can I assist you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ChatGPT Clone: Goodbye!")
        break

    chat_prompt = f"You: {user_input}\nChatGPT Clone:"
    bot_response = chat_with_gpt3(chat_prompt)
    print("ChatGPT Clone:", bot_response)
