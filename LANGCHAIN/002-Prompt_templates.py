import os
from langchain import PromptTemplate
from constants import openai_key
from langchain.llms import OpenAI
from langchain.chains import LLMChain
os.environ["OPENAI_API_KEY"] = openai_key

llm = OpenAI(temperature=0.7)

template_1 = '''I want you to act as a acting financial advisor for people.
                In an easy wasy, explain the basics of {financial_concept}.'''

prompt = PromptTemplate(
    input_variables=['financial_concept'],
    template=template_1
)

print(prompt.format(financial_concept='income tax'))
chain1 = LLMChain(llm=llm, prompt=prompt)

# print(chain1.run('GDP'))

# Language Translation
template_2 = '''In an easy way translate the following sentence '{input_sentence}' into {target_language} '''
language_prompt = PromptTemplate(
    input_variables=["input_sentence", 'target_language'],
    template=template_2
)
print(language_prompt.format(input_sentence="How are you", target_language="hindi"))
chain2 = LLMChain(llm=llm, prompt=language_prompt)

# when having more than 1 parameters then use dictionary...
print(chain2({'input_sentence': "How are you?", "target_language": "bengali"}))
