import streamlit as st
import parser_test
import pandas as pd
import plotly.express as px


def main():
    st.title("UITM News Streamlit Web-Scraping Project")

    if st.button("Start parsing"):
        data = parser_test.get_news(parser_test.get_pages())
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
        st.subheader("Data description")
        st.write(df.describe(include='all'))
        st.subheader("Data")
        st.write(df)

        fig = px.bar(df["date"], text_auto=True, title='Visualization of date')
        st.plotly_chart(fig, use_container_width=True, theme="streamlit")


if __name__ == '__main__':
    main()
