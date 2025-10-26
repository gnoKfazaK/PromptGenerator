from promptGeneration import promptGenerator
import asyncio

user_prompt = "weather of hong kong today"
TESTS_PER_TEMPERATURE = 3
FOLDER = "tempTest"    


# Rate are limited for all parallel
# Used Semaphore in generate_prompt
async def main():
    p = promptGenerator()
    tasks = [
        asyncio.create_task(p.generate_multiple_prompts(user_prompt=user_prompt,temp=round(0.1 * i, 1), n_output=TESTS_PER_TEMPERATURE))
        for i in range(11)
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for i in range(11):
        temp = round(0.1 * i, 1)
        with open(f'{FOLDER}/{temp}temp.txt', 'w') as f:
            for prompt in results[i]:
                f.write(prompt)
                f.write("\n\n"+"-" * 59+"\n\n")
        print(f'temp={temp}.txt done...')
    print("Tests are done...")

# async def main():
#     for i in range(11):
#         temp = round(i * 0.1, 1)
#         await generate_multiple_prompts(temp)
#         print(f'{temp}temp.txt done...')
            
        

if __name__ == "__main__":
    asyncio.run(main())