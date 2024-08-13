import openai
from prompts import *


class GptApi:
    def __init__(self):
        self.API_KEY = "OPENAI_TOKEN"

    def crete_seo(self, name, words):
        openai.api_key = self.API_KEY

        query = SEO_PROMPT.format(product_name=name, seo_words=words)

        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {
                "role": "user",
                "content": query
            }
          ]
        )

        result = completion.choices[0].message.content
        return result

    def random_query(self, query):
        openai.api_key = self.API_KEY

        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          # stream=True,
          messages=[
            {
                "role": "user",
                "content": query
            }
          ]
        )

        result = completion.choices[0].message.content
        return result

    # def improve_seo(self, seo):
    #     openai.api_key = self.API_KEY
    #
    #     query = IMPROVE_SEO_PROMPT.format(seo_improved=seo)
    #     completion = openai.ChatCompletion.create(
    #       model="gpt-3.5-turbo",
    #       messages=[
    #         {
    #             "role": "user",
    #             "content": query
    #         }
    #       ]
    #     )
    #
    #     result = completion.choices[0].message.content
    #     return result

    def mark_answer_create(self, mark_text: str, mark_type: str):
        openai.api_key = self.API_KEY
        print(mark_type)
        if mark_type == "true":
            query = MARK_PROMPT_FALSE.format(mark_text=mark_text)
        else:
            query = MARK_PROMPT_TRUE.format(mark_text=mark_text)

        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {
                "role": "user",
                "content": query
            }
          ]
        )

        result = completion.choices[0].message.content
        return result

    def image_create(self):
        openai.api_key = self.API_KEY

        response = openai.Image.create(
            model='dall-e-3',
            image=open('Screenshot_1.png', 'rb'),
            prompt="напиши любоей текст на картинке",
        )
        print(response)

    def create_logo(self, lolo_prompt: str):
        openai.api_key = self.API_KEY
        response = openai.Image.create(
            model="dall-e-3",
            prompt=lolo_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        return response.data[0].url


