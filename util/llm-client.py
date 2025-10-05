import os, yaml
from openai import OpenAI
import requests


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


config = load_config()
backend = config["backend"]


def get_llm():
    if backend == "openai":
        return OpenAI(api_key=config["openai"]["api_key"])

    elif backend == "deepseek":
        return OpenAI(
            api_key=config["deepseek"]["api_key"],
            base_url=config["deepseek"]["base_url"]
        )

    elif backend == "groq":
        return OpenAI(
            api_key=config["groq"]["api_key"],
            base_url=config["groq"]["base_url"]
        )

    elif backend == "huggingface":
        def hf_call(prompt):
            url = f"https://api-inference.huggingface.co/models/{config['huggingface']['model']}"
            headers = {"Authorization": f"Bearer {config['huggingface']['api_key']}"}
            response = requests.post(url, headers=headers, json={"inputs": prompt})
            return response.json()[0]["generated_text"]

        return hf_call

    elif backend == "ollama":
        def ollama_call(prompt):
            url = f"{config['ollama']['base_url']}/api/generate"
            payload = {"model": config["ollama"]["model"], "prompt": prompt}
            response = requests.post(url, json=payload, stream=True)
            output = ""
            for line in response.iter_lines():
                if line:
                    output += line.decode("utf-8")
            return output

        return ollama_call

    else:
        raise ValueError(f"Unsupported backend: {backend}")
