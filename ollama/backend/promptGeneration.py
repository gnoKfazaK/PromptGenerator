import ollama 
import time
import asyncio

class promptGenerator():
    MODEL = 'llama3'
    prompt = ""
    PROMPT_FILE = "../../prompt_file/prompt.txt"

    def __init__(self):
        start_t = time.perf_counter()
        with open(self.PROMPT_FILE, 'r') as f:
            self.prompt = f.read()
        end_t = time.perf_counter()
        # print(f"Prompt file done reading({round(end_t - start_t, 2)}s)")
        print(f"Prompt file done reading...")

    
    async def generate_prompt(self, user_prompt, model = MODEL, temp = 0.4):
        response = await asyncio.to_thread(
            ollama.chat,
            model=model,
            messages=[
                {"role": "system", "content": "You are a prompt engineering expert. You are required to generate a prompt for the base on the user input. Only the prompt is needed, no extra words needed..."},
                {"role": "user", "content": f"{self.prompt} \nUser prompt: \"{user_prompt}\". Return only the resulting prompt, and nothing else."}
            ],
            options={"temperature": temp}

        )
        return response["message"]["content"]
    

    # Stopped hereS
    async def generate_multiple_prompts(self, user_prompt, temp = 0.4, n_output = 1):
        tasks = [
                asyncio.create_task(self.generate_prompt(user_prompt=user_prompt, temp=temp))
                for i in range(n_output)
            ]
        start_t = time.perf_counter()
        results = await asyncio.gather(*tasks, return_exceptions=True)
        end_t = time.perf_counter()
        print(f'Duration(Temp={temp}, n_output = {n_output}) = {round(end_t - start_t, 2)}s ({round((end_t - start_t) / n_output, 2)}s/output)')
        my_dict = {'prompts': results}
        return my_dict

