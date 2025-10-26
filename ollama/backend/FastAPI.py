from fastapi import FastAPI
from promptGeneration import promptGenerator
import uvicorn
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

p = promptGenerator()


@app.get("/")
def read_root():
    string =  'This is roooooooooooot...'
    return string

@app.get("/gen")
async def generation(user_prompt: str, n_output: int = 1):
    print("Requesting...")
    results = await p.generate_multiple_prompts(user_prompt=user_prompt, n_output=n_output)
    print("Returned:\n")
    for prompt in results['prompts']:
        print(prompt)
        print('\n\n' + '-' * 59 + '\n\n')
    
    return results

@app.get("/test")
def test(para: str, item: str = 'hey'):
    return f"This is {para} {item}"




def main():
    uvicorn.run(app, host = '0.0.0.0', port = 8000)

if __name__ == "__main__":
    main()

