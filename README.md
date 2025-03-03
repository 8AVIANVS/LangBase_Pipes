# LangBase Pipes

A simple Python client for interacting with the LangBase Pipes API. This project allows you to send messages to AI models through LangBase's API and receive responses in your terminal.

## Features

- Send messages to LangBase's AI models
- Receive responses with token usage information
- Simple command-line interface
- Support for environment variables for API key management

## Requirements

- Python 3.6+
- `requests` library
- `python-dotenv` library

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd LangBase_pipes
   ```

2. Install the required dependencies:
   ```
   pip install requests python-dotenv
   ```

3. Create a `.env` file in the project root directory and add your LangBase API key:
   ```
   LB_API_KEY=your_langbase_api_key_here
   ```

## Usage

Run the script with Python:

```
python main.py
```

The script will prompt you to enter a message, which will be sent to the LangBase API. The AI's response will be displayed in the terminal along with token usage information.

### Example

```
$ python main.py
User: Who are you?
LangBase: I'm Less Wordy ChatGPT, a concise AI assistant.
--------------------------
Tokens used: 102
--------------------------
Raw: {'id': 'chatcmpl-B72velnZxUCEIBQo58atFVWcI1cwK', ...}
```

## Configuration

The script uses environment variables for configuration. Create a `.env` file in the project root with the following variables:

- `LB_API_KEY`: Your LangBase API key

## How It Works

1. The script loads your API key from the `.env` file
2. It prompts you to enter a message
3. The message is sent to the LangBase API
4. The response is parsed and displayed in the terminal

## Customization

You can modify the `main.py` file to change how messages are sent to the API or how responses are displayed. The script can be configured to use streaming responses by setting `'stream': True` in the request data.