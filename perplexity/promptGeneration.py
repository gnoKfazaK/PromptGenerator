from perplexity import AsyncPerplexity
import asyncio
import time

class promptGenerator:
    # Good for prompt generation
    MODEL = "sonar-pro"
    # 10 request at most each time
    sem = asyncio.Semaphore(10)
    PROMPT_FILE = "./prompt_file/prompt.txt"
    prompt = ""
    def __init__(self):
        with open(self.PROMPT_FILE, 'r') as f:
            self.prompt = f.read()

        print("Prompt file done reading...")


    
    async def generate_prompt(self, user_prompt, model = MODEL, temp = 0.4):
        async with self.sem:
            async with AsyncPerplexity() as client: # reads PERPLEXITY_API_KEY from env
                completion = await client.chat.completions.create(
                    model = model,
                    messages=[
                        {"role": "system", "content": "You are a prompt engineering expert. You are required to generate a prompt for the base on the user input. Only the prompt is needed, no extra words needed..."},
                        {"role": "user", "content": f"{self.prompt} \nUser prompt: \"{user_prompt}\". Return only the resulting prompt, and nothing else."}
                    ],
                    temperature = temp,
                )  
            prompt = completion.choices[0].message.content
            # split out the thinking part
            if prompt.startwith("</think>"):
                return prompt.split('</think>')[-1] 
            else:
                return prompt



    async def generate_multiple_prompts(self, user_prompt, temp = 0.4, n_output = 1):
        
        tasks = [
            asyncio.create_task(self.generate_prompt(user_prompt=user_prompt, temp=temp))
            for i in range(n_output)
        ]
        start_t = time.perf_counter()
        results = await asyncio.gather(*tasks, return_exceptions=True)
        end_t = time.perf_counter()
        print(f'Duration(Temp={temp}, n_output = {n_output}) = {round(end_t - start_t, 2)}s ({round((end_t - start_t) / n_output, 2)}s/output)')
        return results

   

