import pandas as pd
import streamlit as st

st.title("勉強会用Udemy講座一覧")

st.write("")

names = [
    "React",
    "FastAPI",
    "NestJS",
    "AWS CLF",
    "Linux + Docker",
    "Terraform",
    "機械学習",
    "物体検知AI",
    "Streamlit",
]

descriptions = [
    "モダンJSとReactでTODOアプリ",
    "会議室予約API",
    "CRUD中心の実装入門",
    "CLF資格範囲のハンズオン",
    "Linux基礎とDockerで開発環境構築",
    "Cloud9でTerraform実装",
    "機械学習に必要な数学と単回帰分析",
    "Google Colabで物体検知AI導入",
    "CNN画像分類Webアプリ",
]

df = pd.DataFrame(
    {
        "no": list(range(1, len(names) + 1)),
        "name": names,
        "description": descriptions,
        "background": [
            "HTML/CSS/JS基礎",
            "Python基礎",
            "TypeScript基礎",
            "ネットワーク基礎",
            "CLI基礎",
            "AWS基礎",
            "なし",
            "Googleアカウント",
            "Google, GitHub",
        ],
        "stars": [4.7, 4.5, 4.2, 4.2, 4.5, 4.2, 4.4, 4.5, 4.4],
        "times": [7, 10, 5, 15, 5, 4, 4, 4, 3],
        "url": [
            "https://www.udemy.com/course/modern_javascipt_react_beginner/",
            "https://www.udemy.com/course/python-fastapi/",
            "https://www.udemy.com/course/nestjs-t/",
            "https://www.udemy.com/course/ok-aws-e/",
            "https://www.udemy.com/course/docker-from-linux-and-networking/",
            "https://www.udemy.com/course/terraform-with-aws/",
            "https://www.udemy.com/course/kikagaku_blackbox_1/",
            "https://www.udemy.com/course/tetsumag-objectdetection/",
            "https://www.udemy.com/course/ai-web-app/",
        ],
    }
)


st.dataframe(
    df,
    column_config={
        "no": "No.",
        "name": "App name",
        "description": "Description",
        "stars": st.column_config.NumberColumn(
            "Stars",
            help="Number of stars on Udemy",
            format="%1f ⭐",
        ),
        "times": st.column_config.NumberColumn(
            "Times",
            help="Time of movies on GitHub",
            format="%1f h",
        ),
        "url": st.column_config.LinkColumn(
            "Udemy URL", display_text="https://www.udemy.com/course/(.*?)/"
        ),
    },
    hide_index=True,
)
