import ollama 
import time

class promptGenerator():
    MODEL = 'llama3'
    prompt = ""
    PROMPT_FILE = "./prompt_file/prompt.txt"

    def __init__(self):
        with open(self.PROMPT_FILE, 'r') as f:
            self.prompt = f.read()

        print("Prompt file done reading...")

    
    def generate_prompt(self, user_prompt, model = MODEL, temp = 0.4):
        start_t = time.perf_counter()
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": "You are a prompt engineering expert. You are required to generate a prompt for the base on the user input. Only the prompt is needed, no extra words needed..."},
                                {"role": "user", "content": f"{self.prompt} \nUser prompt: \"{user_prompt}\". Return only the resulting prompt, and nothing else."}
            ],
            options={"temperature": temp}

        )
        end_t = time.perf_counter()
        return (response["message"]["content"], round(end_t - start_t, 2))
