import json

from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1/",api_key="ollama")

print(client.models.list())
print(type(client))


result = client.responses.create(
    model="llama3.2",
    input="what is the last date u know of?",
)

print(json.dumps(result.to_dict(), indent=2))


# result = client.responses.create(
#     model="llama3.2",
#     instructions="you are a helpful assistant",
#     input="What is square of 7?",
#     temperature=0.7,
#     max_output_tokens=100
# )
# print(result.output_text)
# print("Input Tokens: ",result.usage.input_tokens)
# print("Output Tokens: ",result.usage.output_tokens)
# print("Total Tokens: ",result.usage.total_tokens)


# result = client.chat.completions.create(
#     model="llama3.2",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant who explains answers in funny way."
#         },
#         {
#             "role": "user",
#             "content": "Write me a poem on Python programming?"
#         }
#     ],
#     temperature=0.7,
#     max_tokens=1000,
#     stream=True
# )
# # prints(result)
# # print(result.choices[0].message.content)

# for chunk in result:
#     if chunk.choices:
#         content = chunk.choices[0].delta.content

#         if content is not None:
#             print(content, end="", flush=True)

#     if chunk.usage:
#         print("\nInput Tokens:", chunk.usage.prompt_tokens)
#         print("Output Tokens:", chunk.usage.completion_tokens)
#         print("Total Tokens:", chunk.usage.total_tokens)