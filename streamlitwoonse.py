import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

st.title("오늘의 운세")
st.divider()

name = st.text_input("사용자의 이름")
year = st.text_input("태어난 연도")
month = st.text_input("태어난 월")
day = st.text_input("태어난 일")

submit = st.button("운세 보기")

if submit:
    if name == "":
        st.markdown(":red[이름을 입력하세요]")
    elif year == "":
        st.markdown(":red[연도를 입력하세요]")
    elif month == "":
        st.markdown(":red[월을 입력하세요]")
    elif day == "":
        st.markdown(":red[일을 입력하세요]")
    else:
        st.write(f"{name}님의 운세는 다음과 같습니다.")
        example_prompt = "#예시\n입력 : 2001년 2월 4일\n 출력:꿈을 믿지 않던 사람도 다시 한번 꿈의 위력에 대해 생각해 보게 되는 날입니다. 간밤의 좋은 꿈이 행운을 불러들이는 듯 좋은 일들이 일어나는 하루이기 때문입니다. 꿈인지 생시인지 구별이 안 갈 정도로 단꿈에 빠져있는 기분이 들 수 있습니다. 좋은 꿈의 영향으로 자신의 하루가 기분 좋게 시작할 수 있습니다. 아침부터 좋은 일이 생겨 기분도 한결 밝아지고, 자연스럽게 의욕이 생깁니다. 자신이 하고 있는 일에 대해 자신감을 얻을 수 있으며 하루를 웃음으로 마무리할 수 있습니다.\n"

        prompt = PromptTemplate.from_template("예시를 참고해서 유저의 운세를 출력해주세요" + example_prompt + "\n#입력문\n입력 : {nyeon}년 {wol}월 {il}일")

        go = prompt.format(nyeon=year,wol=month,il=day)

        llm = ChatOpenAI(max_tokens=700,
                        temperature=0.6,
                        model_name='gpt-3.5-turbo',
                        openai_api_key='')

        st.write(llm.predict(go))