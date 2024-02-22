from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from openai import OpenAI
from pandas.io import clipboard

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)


@app.route('/', methods=['GET','POST'])
def generate():
    message = "Generated message will appear here."

    if request.method == 'POST':
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        company_name = request.form.get('company_name')
        client_name = request.form.get('client_name')
        occasion = request.form.get('occasion')
        tone = request.form.get('tone')
        action = request.form.get('generate_text') or request.form.get('generate_email')

        prompt = [{"role" : "user", "content": f"Write a {tone} message for the occasion '{occasion}' from '{name}' of '{company_name}' to '{client_name}'. Include phone number {phone_number}."}]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            max_tokens=200
        )

        generated_text = response.choices[0].message.content


        if action == 'Generate Email':
            message = f"Subject: Regarding {occasion}\n\nDear {client_name},\n\n{generated_text}\n\nBest regards,\n{name}\n{company_name}\nPhone: {phone_number}"
        else:
            message = generated_text

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
