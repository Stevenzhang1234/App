from flask import Flask, jsonify
from flask_cors import CORS 
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = 'sk-None-x5GV8w0obPPl79OZSP9rT3BlbkFJGlALBhnAqH4FOz7kY7pX'

@app.route('/test/<message>')
def test_method(message):
  response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."}, 
                  {"role": "user", "content": message}],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
  )
  openai_response = response['choices'][0]['message']['content'].strip()
  print(message)
  return jsonify({'message': message, 'response': openai_response})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)