from openai import OpenAI
from typing import Generator
from .prompts import SYSTEM_PROMPT, PROMPT_TEMPLATES, EXAMPLE_REFERENCE_PROMPT
from .example_loader import load_example

class LLMService:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API Key is required")
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )

    def generate_draft_stream(self, template_type: str, data: dict, context: str = "") -> Generator[str, None, None]:
        # Get template or default
        user_prompt_template = PROMPT_TEMPLATES.get(template_type)
        if not user_prompt_template:
            user_prompt_template = f"""
            场景：{template_type}
            
            关键要素：
            - 主题：{{topic}}
            - 时间：{{time}}
            - 地点：{{location}}
            - 关键人物：{{people}}
            - 核心内容：{{content}}

            请撰写一篇关于{template_type}的宣传稿。
            """

        # Format user prompt
        try:
            user_content = user_prompt_template.format(
                topic=data.get("topic", "未指定"),
                time=data.get("time", "未指定"),
                location=data.get("location", "未指定"),
                people=data.get("people", "未指定"),
                content=data.get("content", "未指定")
            )
        except KeyError:
             user_content = user_prompt_template # Fallback if format fails

        # Format system prompt
        system_content = SYSTEM_PROMPT.format(context=context if context else "无参考素材")
        
        # 加载范文内容
        example_content = load_example(template_type)
        
        # 如果有范文，添加范文参考提示
        if example_content:
            system_content += EXAMPLE_REFERENCE_PROMPT.format(example_content=example_content)
        
        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ]

        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                stream=True,
                temperature=0.7
            )
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"[Error: {str(e)}]"



