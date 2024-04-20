# imports
import os
import ast  # for converting embeddings saved as strings back to arrays
import openai  # for calling the OpenAI API
import pandas as pd  # for storing text and embeddings data
import tiktoken  # for counting tokens
from scipy import spatial  # for calculating vector similarities for search
from flask import Flask, request, jsonify

app = Flask(__name__)

# models
EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"

def convert_to_list(string):
    """Convert a string representation of a list to an actual list."""
    return ast.literal_eval(string)

df = pd.read_csv("data/code_search_openai-python.csv", converters={'code_embedding': convert_to_list})

openai.api_key = 'OPENAI_API_KEY'

def strings_ranked_by_relatedness(
    query,
    df,
    relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y),
    top_n=100
):
    """Returns a list of strings and relatednesses, sorted from most related to least."""
    query_embedding_response = openai.Embedding.create(
        model=EMBEDDING_MODEL,
        input=query,
    )
    query_embedding = query_embedding_response["data"][0]["embedding"]
    strings_and_relatednesses = [
        (row["data"], relatedness_fn(query_embedding, row["code_embedding"]))
        for i, row in df.iterrows()
    ]
    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    strings, relatednesses = zip(*strings_and_relatednesses)
    return strings[:top_n], relatednesses[:top_n]

def num_tokens(text: str, model: str = GPT_MODEL) -> int:
    """Return the number of tokens in a string."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def query_message(
    query: str,
    df: pd.DataFrame,
    model: str,
    token_budget: int
) -> str:
    """Return a message for GPT, with relevant source texts pulled from a dataframe."""
    strings, relatednesses = strings_ranked_by_relatedness(query, df)
    introduction = "Below are some articles that may help answer your question. If you cannot find the information you're looking for, please let me know and I'll do my best to assist you further. You can also ask follow-up questions related to the article sections provided."
    
    question = f"\n\nQuestion: {query}"
    message = introduction
    for string in strings:
        next_article = f'\n\ article section:\n"""\n{string}\n"""'
        if (
            num_tokens(message + next_article + question, model=model)
            > token_budget
        ):
            break
        else:
            message += next_article
    return message + question

def ask(
    query: str,
    df: pd.DataFrame = df,
    model: str = GPT_MODEL,
    token_budget: int = 4096 - 500,
    print_message: bool = False,
) -> str:
    """Answers a query using GPT and a dataframe of relevant texts and embeddings."""
    print(query)
    message = query_message(query, df, model=model, token_budget=token_budget)
    if print_message:
        print(message)
    messages = [
        {"role": "system", "content": "In this section, you will find information on how to manage users and set permissions on our platform. If you can't find the answer you're looking for, feel free to ask us a question."},
        {"role": "user", "content": message},
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    response_message = response["choices"][0]["message"]["content"]
    return response_message


@app.route('/test')
def hello():
    name = request.args.get('query')
    if name:
        return jsonify(Reply = ask(name))
    else:
        return 'Hello, world!'


if __name__ == '__main__':
    app.run()



