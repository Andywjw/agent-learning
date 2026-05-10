from openai import OpenAI
from Hello_Client import HelloClient

def cot_prompt(question: str) -> str:
    prompt = f"""
你是一个擅长逻辑推理的助手，请按照步骤逐步思考并给出最终答案。

问题：
{question}

请按照以下格式回答：
1. 分析问题
2. 逐步推理
3. 得出最终答案

开始：
"""
    return prompt.strip()


def ask_llm(question: str):
    prompt = cot_prompt(question)
    client = HelloClient()

    response = client.client.chat.completions.create(
        model="doubao-seed-1.6",
        messages=[
            {"role": "system", "content": "你是一个严谨的推理助手"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    q = "一个商店卖苹果，每个苹果3元，买5个多少钱？"
    answer = ask_llm(q)
    print(answer)