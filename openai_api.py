#!python
import os
import argparse
import openai


def init_openai():
    # Set the GPT-3 API key
    openai.organization = "org-GQB7Bz8SxOa1UMJmQlCNjONi"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # with open("openai_module.txt", 'w+') as f_obj:
    #     f_obj.write(str(openai.Model.list()))


def parse_unstructured_data(content):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{content}",
        temperature=0,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response["choices"][0]["text"]


def explain_code(content):
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=f"{content}",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )
    return response["choices"][0]["text"]


def create_study_notes(content):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{content}",
        temperature=0.3,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response["choices"][0]["text"]


def essay_outline(content):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{content}",
        temperature=0.3,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response["choices"][0]["text"]


def interview_questions(content):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{content}",
        temperature=0.5,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response["choices"][0]["text"]


def my_diy(content):
    # Generate some text with GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{content}",
        temperature=0.8,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stream=True
    )
    # Return the generated text
    txt = ''.join([res["choices"][0]["text"] for res in response])
    return txt


def run_openai(content='', func=my_diy):
    if not content:
        while True:
            content = ''
            try:
                txt = input('> ')
                if txt == 'exit':
                    break
                print(func(content))
            except:
                print("ERROR!")
    else:
        try:
            print(func(content))
        except:
            print("ERROR!")


if __name__ == '__main__':
    # 创建一个解析器
    parser = argparse.ArgumentParser()
    # 添加参数
    parser.add_argument("-c", '--content', type=str, help='text content')
    # 解析参数
    args = parser.parse_args()
    content = args.content

    # init_openai()
    run_openai(content)
