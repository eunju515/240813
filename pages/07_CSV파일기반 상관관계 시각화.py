import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 제목 설정
st.title('CSV 파일 업로드를 통한 상관관계 시각화 📊')

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드 해주세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)

    # 데이터프레임 표시
    st.write("업로드된 데이터:")
    st.write(df)

    # 상관관계 행렬 계산
    corr_matrix = df.corr()

    # 상관관계 행렬 시각화
    st.write("상관관계 행렬:")
    st.write(corr_matrix)

    # 상관관계 히트맵 그리기
    st.write("상관관계 히트맵:")
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    st.pyplot(plt)
else:
    st.write("CSV 파일을 업로드해주세요.")
