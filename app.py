from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace with your own OpenAI API key
openai.api_key = "your-api-key"

@app.route('/popebot', methods=['POST'])
def popebot():
    user_input = request.json['input']
    response = get_popebot_response(user_input)
    return jsonify(response=response)

def get_popebot_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"System: you are PopeBot. {prompt}",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
