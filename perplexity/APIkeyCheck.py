import os

if "PERPLEXITY_API_KEY" in os.environ:
    print("Key is set:", os.environ["PERPLEXITY_API_KEY"])
else:
    print("PERPLEXITY_API_KEY not found in environment")
