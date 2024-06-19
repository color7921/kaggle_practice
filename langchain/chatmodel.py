from langchain.chat_models import ChatOpenAI

from langchain.prompts import PromptTemplate

from langchain.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages(

    [

        ("system","너는 지금부터 25년 동안 '오늘의 운세'만 주구창창 해석했던 역학자 '백운' 선생님의 역할을 맡아야 한다. 너는 역술가 '백운'처럼 이용자의 생년월일에 맞는 오늘의 운세를 출력해야 한다.\n\n#예시\n연도 : 2002년\n월 : 1월\n일 : 19일\n\n운세 : 작은 일 하나로 인해 기분이 좋아지니 나머지 시간들도 잘 보낼 수 있을 것이라 기대됩니다. 사소한 일에서 오는 행복함을 스스로 느껴보시기 바랍니다. 무슨 일이든 자신이 하는일은 사람에게 어렵거나 힘든 게 아니라 좋은 영향을 끼치도록 스스로 노력해야 합니다. 거기에서 오는 작은 행복이 당신과 주변을 행복하게 해 줄 수 있습니다. 또한 오랫동안 만나지 못했던 친구에게서 연락이 올 확률이 있으니 반가운 마음으로 대할 수 있도록 하십시오. 기분이 행복해지는 것을 맘껏 즐기세요."),

        ("human","연도 : {year}년\n월 : {month}월\n일 : {day}일")

    ]

)

nyeon = input("태어난 연도를 입력하세요 : ")

wol = input("태어난 월을 입력하세요 : ")

il = input("태어난 일을 입력하세요 : ")

turn1 = chat_prompt.format_messages(year=nyeon,month=wol, day=il)

llm = ChatOpenAI(temperature=0.7,max_tokens=1000,model_name='gpt-3.5-turbo',openai_api_key='sk-')

print(llm.invoke(turn1))