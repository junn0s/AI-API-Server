from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini", model_provider="openai")


from langchain_core.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

# print(model.invoke(messages))

#for token in model.stream(messages):
#    print(token.content, end="|")

from langchain_core.prompts import ChatPromptTemplate

'''system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Korean", "text": "my name is milo!"})
response = model.invoke(prompt)
print(response.content)'''


ambiance = input("미로의 분위기를 입력하세요 (예: 어두운): ")
location = input("미로의 장소를 입력하세요 (예: 고대 성 지하): ")

system_template = "미로 스토리 생성 요청"
user_template = "{ambiance} 분위기의 {location} 장소 미로를 원해. 위 조건에 맞는 흥미로운 미로 스토리를 작성해줘."

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", user_template)
    ]
)

prompt = prompt_template.invoke({"ambiance": ambiance, "location": location})

response = model.invoke(prompt)
print(response.content)