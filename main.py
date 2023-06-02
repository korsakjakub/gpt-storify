import os
import json
import openai

def set_output(name: str, value: str) -> None:
    with open(os.getenv('GITHUB_OUTPUT'), 'a') as outputFile:
        print(f'{name}={value}', file=outputFile)

def get_story(config: dict) -> str:
    openai.api_key = config['OPENAI_API_KEY']

    content = json.dumps(f"{config['INSTRUCTION']}\n\n{config['PROMPT']}")

    completion = openai.ChatCompletion.create(
      model = config['MODEL'],
      messages = [
        {"role": "user", "content": content}
      ]
    )

    return json.dumps(completion.choices[0].message.content)

if __name__ == "__main__":

    config = {
        'INSTRUCTION': os.getenv('INSTRUCTION'),
        'PROMPT': os.getenv('PROMPT'),
        'MODEL': os.getenv('MODEL'),
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
    }

    story = get_story(config)

    set_output('content', story)
