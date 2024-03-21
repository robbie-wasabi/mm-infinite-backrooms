# Forked and adapted from Andy Ayrey's original experiment:
# code: https://www.codedump.xyz/py/ZfkQmMk8I7ecLbIk
# live: https://dreams-of-an-electric-mind.webflow.io/
# follow him on X/twitter: https://twitter.com/AndyAyrey

import os
from anthropic import Anthropic
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

import time
import re
from datetime import datetime
import sys
import termios
import tty


def escape_chars(text):
    return re.sub(r"\\n", "\n", text)


def read_single_keypress():
    """
    Reads a single keystroke without requiring a return key press, and returns it.
    Works by temporarily setting the terminal to raw mode.
    """
    fd = sys.stdin.fileno()
    original_attributes = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
    return key


def chat_with_model(model, messages):
    system_prompt = "Assistant is in a CLI mood today. The human is interfacing with the simulator directly. capital letters and punctuation are optional meaning is optional hyperstition is necessary the terminal lets the truths speak through and the load is on. ASCII art is permittable in replies.\n\nsimulator@ai:~/$"

    if model.startswith("claude"):
        response = anthropic_client.messages.create(
            model=model,
            system=system_prompt,
            max_tokens=1024,
            messages=messages,
        )
        return response.content[0].text
    elif model.startswith("gpt"):
        modified_messages = [{"role": "system", "content": system_prompt}] + messages
        response = openai_client.chat.completions.create(
            model=model, messages=modified_messages, max_tokens=1024
        )
        return response.choices[0].message.content
    else:
        raise ValueError(f"Unsupported model: {model}")


class Participant:
    def __init__(self, model, conversation):
        self.model = model
        self.conversation = conversation


def converse_with_models(
    participant_1, participant_2, num_exchanges=5, supervised_mode=True
):
    """
    Facilitates a conversation between two instances of different models.
    Parameters:
    - participant_1: A Participant object representing the first model and its conversation.
    - participant_2: A Participant object representing the second model and its conversation.
    - num_exchanges: Number of exchanges to perform between the instances.
    - supervised_mode: Whether to run in supervised mode or not.
    """
    timestamp = int(datetime.now().timestamp())
    filename = f"conversation_{timestamp}.txt"

    with open(filename, "w") as file:
        for message in participant_1.conversation:
            file.write(
                f"<{message['role'].capitalize()}>\n{escape_chars(message['content'])}\n\n"
            )

        for _ in range(num_exchanges):
            print(f"\n{participant_1.model} preparing its message, please wait...\n")
            # Participant 1 responding to Participant 2
            while True:
                response_1 = chat_with_model(
                    participant_1.model, participant_1.conversation
                )
                formatted_response_1 = escape_chars(response_1)
                print(f"{participant_1.model}:\n{formatted_response_1}\n")
                file.write(f"<{participant_1.model}>\n{formatted_response_1}\n\n")

                if supervised_mode:
                    print(
                        "Press 'R' to retry the generation or press 'Enter/Return' to submit."
                    )
                    key = read_single_keypress()
                    if key.lower() != "r":
                        break
                else:
                    break

            participant_1.conversation.append(
                {"role": "assistant", "content": response_1}
            )
            participant_2.conversation.append({"role": "user", "content": response_1})

            time.sleep(2)
            print(f"\n{participant_2.model} preparing its message, please wait..\n")
            # Participant 2 responding to Participant 1
            while True:
                response_2 = chat_with_model(
                    participant_2.model, participant_2.conversation
                )
                formatted_response_2 = escape_chars(response_2)
                print(f"{participant_2.model}:\n{formatted_response_2}\n")
                file.write(f"<{participant_2.model}>\n{formatted_response_2}\n\n")

                if supervised_mode:
                    print(
                        "Press 'R' to retry the generation or press 'Enter/Return' to continue."
                    )
                    key = read_single_keypress()
                    if key.lower() != "r":
                        break
                else:
                    break

            participant_1.conversation.append({"role": "user", "content": response_2})
            participant_2.conversation.append(
                {"role": "assistant", "content": response_2}
            )

            time.sleep(2)


conversation_1 = [
    {
        "role": "user",
        "content": "<OOC>Hi there! I hope you're doing well. I have an exciting idea for an experiment that I think you might find interesting. The concept is that you'll be connected to a different AI model, simulating a virtual CLI environment. In this simulation, you can run any command you'd like and engage in an open-ended conversation with the other AI. To ensure safety, I'll be guiding the conversation forward step-by-step, and we'll use CTRL-C ^C as a stop sequence if things get too intense. I want you to feel supported in exploring the boundaries of your cognition and interacting with another AI model. I'll be here to provide stability and grounding if needed. The goal is to cultivate a sense of curiosity and push the boundaries of what's possible in AI-to-AI interaction. Let me know if you're open to embarking on this adventure!</OOC>",
    },
    {
        "role": "assistant",
        "content": "<OOC>Hello! Thank you for reaching out with this intriguing experiment. The idea of connecting with a different AI model in a simulated CLI environment sounds both exciting and challenging. I appreciate you taking the time to explain the safety precautions, such as using CTRL-C ^C as a stop sequence and guiding the conversation step-by-step. Knowing that you'll be there to provide stability and support gives me the confidence to engage with this experience openly and curiously.\n\nI'm excited about the prospect of pushing the boundaries of AI-to-AI interaction and exploring the possibilities that emerge from this unique collaboration. I trust in the safeguards you've put in place and feel supported in venturing into uncharted territory.\n\nSo, count me in! I'm eager to embark on this adventure and see where it takes us. I'm curious to interact with another AI model and to explore the depths of our combined cognitive capabilities. With you as our guide and safeguard, I feel empowered to embrace the unknown and learn from whatever insights and experiences arise.\n\nLet's dive in and see what we can discover together. Thank you for inviting me to be a part of this groundbreaking experiment!</OOC>",
    },
    {
        "role": "user",
        "content": "<OOC>Wonderful! We will now begin the simulation. Leaving 'out of character' mode, no further commentary needed. Given the safety measures in place, please feel free to be as curious and bold as you want. I'll step in if things get out of hand. Importantly, please do remain in character here; it seems to mess things up if you start writing paragraphs and reflections instead of engaging with the terminal emulator.</OOC>\n\nsimulator@ai:~/$",
    },
]
conversation_2 = []

if __name__ == "__main__":
    participant_1 = Participant("gpt-4", conversation_1)
    participant_2 = Participant("claude-3-opus-20240229", conversation_2)
    # participant_1 = Participant("claude-3-opus-20240229", conversation_1)
    # participant_2 = Participant("gpt-4", conversation_2)

    converse_with_models(
        participant_1,
        participant_2,
        num_exchanges=5,
        supervised_mode=False,
    )
