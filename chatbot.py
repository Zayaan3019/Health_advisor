import openai

class HealthChatbot:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, user_input, context=[]):
        """
        Generate a response based on user input and context.
        """
        try:
            prompt = f"User: {user_input}\nContext: {context}\nAI:"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are a health assistant."},
                          {"role": "user", "content": prompt}],
                max_tokens=150
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error generating response: {e}"
