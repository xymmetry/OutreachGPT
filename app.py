from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

key = os.getenv("OPENAI_API_KEY")
if key is None:
    raise Exception("OPENAI_API_KEY env variable not set.")

client = OpenAI(api_key=key)


@app.route('/', methods=['GET','POST'])
def generate():
    name = 'Enter your name.'
    phone_number = 'Enter your phone number.'
    company_name = 'Enter the name of your company.'
    client_name = "Enter Recipient's Name(s)"
    details = 'Provide the details or purpose of your outreach.'
    message = 'Generated message will appear here.'

    if request.method == 'POST':
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        company_name = request.form.get('company_name')
        client_name = request.form.get('client_name')
        details = request.form.get('details')
        tone = request.form.get('tone')
        action = request.form.get('generate_text') or request.form.get('generate_email')

        prompt = [{"role" : "user", "content": f"Write a {tone} message with these details '{details}' from '{name}' of '{company_name}' to '{client_name}'. Include phone number {phone_number}."}]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            max_tokens=200
        )

        generated_text = response.choices[0].message.content


        if action == 'Generate Email':
            message = f"Subject: Regarding {details}\n\nDear {client_name},\n\n{generated_text}\n\nBest regards,\n{name}\n{company_name}\nPhone: {phone_number}"
        else:
            message = generated_text

    return render_template('index.html', message=message, name=name, phone_number=phone_number, company_name=company_name, client_name=client_name, details=details)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
