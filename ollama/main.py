from promtGeneration import promptGenerator

user_input = 'weather of hong kong today'

p = promptGenerator()

print(p.generate_prompt(user_prompt=user_input)[0])
print(str(p.generate_prompt(user_prompt=user_input)[1]) + 's')