
# OutreachGPT

## Overview
OutreachGPT is a Flask-based web application designed to generate personalized outreach messages and emails using OpenAI's GPT-3.5 model. This tool is ideal for professionals looking to automate their client communication with a touch of personalization and AI-powered creativity.

## Features
- Generate personalized text messages or emails.
- Customizable inputs for different aspects of the message (e.g., name, company name, occasion).
- Integration with OpenAI's GPT-3.5 model for natural language processing.
- User-friendly web interface.

## Installation

### Prerequisites
- Python 3.12 or later
- pip
- Access to OpenAI API (API key required)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-github-username/outreachgpt.git
   ```
2. Navigate to the project directory:
   ```sh
   cd outreachgpt
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the environment variables:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```plaintext
   API_KEY='your_openai_api_key'
   ```

## Running the Application
Run the Flask application:
```sh
flask run
```
The application will be accessible at `http://localhost:5000`.


## Contributing
Contributions to OutreachGPT are welcome! Please refer to the contributing guidelines for more information.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- OpenAI for providing the GPT-3.5 API & the Flask community for the fun web framework.
