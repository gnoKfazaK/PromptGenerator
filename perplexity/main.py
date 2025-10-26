from promptGeneration import promptGenerator
import asyncio



async def main():
    p = promptGenerator()
    print("What do you need?")
    # user_prompt can be "generate prompt for user input"
    user_prompt = input()
    print("How many output you want?")
    number_of_output = int(input())
    results = await p.generate_multiple_prompts(user_prompt=user_prompt, n_output=number_of_output)
    for result in results:
        print(result)
        print("-" * 100)

if __name__ == "__main__":
    asyncio.run(main())