import openai

# Get API key
openai.api_key = "Your Open AI API Key"

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()
	

while True:
    user_input = input("User: ")
    if user_input == "exit":
        break
    response = generate_response(user_input)
    print("Chatbot:", response)
