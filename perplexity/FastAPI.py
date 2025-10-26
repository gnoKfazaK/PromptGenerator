from fastapi import FastAPI
from promptGeneration import promptGenerator

app = FastAPI()
p = promptGenerator()


@app.get("/")
def read_root():
    string =  'This is roooooooooooot... Jenny <3'
    return string

@app.get("/generation/{user_prompt}")
async def generation(user_prompt):
    print("Requesting...")
    result = await p.generate_prompt(user_prompt=user_prompt)
    print("Returned:\n" + result)
    return result

@app.get("/test")
def test(para: str, item: str):
    return f"This is {para} {item}"





