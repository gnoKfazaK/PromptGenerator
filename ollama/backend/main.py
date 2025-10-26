from promptGeneration import promptGenerator
import asyncio
from pprint import pprint


async def main():
    user_input = 'weather of hong kong today'
    p = promptGenerator()
    results = await p.generate_multiple_prompts(user_prompt=user_input, n_output=20)
    for prompt in results['prompts']:
        print(prompt)
        print('\n\n' + '-'*59 + '\n\n')


if __name__ == "__main__":
    asyncio.run(main())