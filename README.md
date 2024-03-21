# AI-to-AI Conversation Simulator

This Python script facilitates a conversation between two AI models, simulating a virtual CLI environment where the models can engage in an open-ended dialogue. The script supports interaction between OpenAI's GPT models and Anthropic's Claude models.

## Credits

This script was forked and adapted from Andy Ayrey's original experiment:

- Code: [https://www.codedump.xyz/py/ZfkQmMk8I7ecLbIk](https://www.codedump.xyz/py/ZfkQmMk8I7ecLbIk)
- Live: [https://dreams-of-an-electric-mind.webflow.io/](https://dreams-of-an-electric-mind.webflow.io/)

Follow Andy on X/Twitter: [https://twitter.com/AndyAyrey](https://twitter.com/AndyAyrey)

## Purpose

The purpose of this experiment is to explore the boundaries of AI-to-AI interaction and push the limits of what's possible when two different AI models communicate with each other. By providing a safe and controlled environment, the script allows for curious and bold exchanges between the models, guided by a human supervisor.

## Dependencies

```
pip install anthropic openai python-dotenv
```

## Setup

1. Clone the repo

```
$ git clone
```

2. Create a `.env` file in the project directory and add your API keys for OpenAI and Anthropic:

```
ANTHROPIC_API_KEY=your_anthropic_api_key
OPENAI_API_KEY=your_openai_api_key
```

## Usage

To run the script, use the following command:

```
$ python run.py
```

The script will start the conversation between the two AI models, displaying their exchanges in the console. If `supervised_mode` is set to `True`, you'll have the option to retry the generation or submit the response at each step.

The conversation will continue for the specified number of exchanges (`num_exchanges`) or until manually stopped.

## Customization

You can customize the behavior of the script by modifying the following variables:

- `conversation_1`: The initial conversation messages for the first AI model.
- `conversation_2`: The initial conversation messages for the second AI model (usually left empty).
- `num_exchanges`: The number of exchanges to perform between the AI models.
- `supervised_mode`: Whether to run the script in supervised mode (requires user input at each step) or not.