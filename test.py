import openai
# from apikey import APIKEY

openai.api_key = "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"
# Let's chatr
output = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    #system, user, assistant
    messages =[{"role": "user", "content":"can you give me a breakfast recommendateion this is high protein and delicious?"}]
)

# print out the chat
print(output['choices'][0]['message']['content'])