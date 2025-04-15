import streamlit as st 
import datetime
from myanmar_news import MyanmarNews
from streamlit_folium import st_folium
import re
import folium
import pydeck as pdk
import pandas as pd

weather_news, weather_forecast = st.tabs(["Weather News",'Weather Forecast'])

with weather_news:
    st.markdown(" **Earthquake data is updated every 6 hours.** Check back regularly for the latest seismic activity in Myanmar and nearby regions.")
    
    now = datetime.datetime.now().strftime("%B %d, %Y – %I:%M %p")

    st.markdown(f"""⏰ **Last updated:** {now}  
    _This page refreshes with new data every 6 hours._""")
    
    time_now = datetime.datetime.now().strftime("%H")
    st.markdown(
        """
        <style>
            .news-box {
                background-color: #f0f8ff;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                font-family: 'Arial', sans-serif;
                color: #333;
                font-size: 18px;
                line-height: 1.6;
            }
            .headline {
                font-size: 22px;
                font-weight: bold;
                color: #2e8b57;
                margin-bottom: 10px;
            }
            .timestamp {
                font-size: 14px;
                color: #888;
                margin-top: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    #st.write(time_now)
    def generate_weather_news():
        return MyanmarNews.get_news("Myanmar Weather Disaster News in Every LOCATION (LATITUDE, and LONGITUDE), and DATE and TIME")
    st.markdown(
        """
        <style>
            .news-box {
                background-color: #f0f8ff;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                font-family: 'Arial', sans-serif;
                color: #333;
                font-size: 18px;
                line-height: 1.6;
            }
            .headline {
                font-size: 22px;
                font-weight: bold;
                color: #2e8b57;
                margin-bottom: 10px;
            }
            .timestamp {
                font-size: 14px;
                color: #888;
                margin-top: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    if 'news' not in st.session_state:
        st.session_state.news = None
        st.session_state.last_updated = None

    time_now = datetime.datetime.now().strftime("%H")
    #st.write(time_now)
    response_placeholder = st.empty()

    if time_now in ["6", "12", "18", "00"]:
        with st.spinner("Generating latest data..."):
            try:
                if st.session_state.news is None:
                    response = generate_weather_news()
                    st.session_state.news = response
                    st.session_state.last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if "<tool_call>" in st.session_state.news or "</tool_call>" in st.session_state.news:
                    st.warning("Please refresh the page.")
                elif "duckduckgo_search" in st.session_state.news or "weather_search" in st.session_state.news:
                    st.warning("Please refresh the page.")
                else:
                    response_placeholder.markdown(
                        f"""
                        <div class="news-box">
                            <div class="headline">Latest Weather Update</div>
                            <p>{st.session_state.news}</p>
                            <div class="timestamp">Last updated: {st.session_state.last_updated}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            except Exception as e:
                st.error("Server is busy. Please try again later.")
    else:
        if st.session_state.news:
            response_placeholder.markdown(
                f"""
                <div class="news-box">
                    <div class="headline">Latest Weather Update</div>
                    <p>{st.session_state.news}</p>
                    <div class="timestamp">Last updated: {st.session_state.last_updated}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.info("No weather summary available yet. Please check back at the scheduled update times.")

    if st.session_state.news:
        pattern = r"latitude:\s*([\d.]+°\s?[Nn]),\s*longitude:\s*([\d.]+°\s?[Ee])"
        matches = re.findall(pattern, st.session_state.news)

        coordinates = []
        for lat, lon in matches:
            try:
                clean_lat = float(re.sub(r"[^\d.]", "", lat))
                clean_lon = float(re.sub(r"[^\d.]", "", lon))
                coordinates.append((clean_lat, clean_lon))
            except ValueError:
                print(f"Skipping invalid coordinates: {lat}, {lon}")

        if coordinates:
            df = pd.DataFrame(coordinates, columns=["Latitude", "Longitude"])

            st.subheader("📍 Earthquake Locations in Myanmar")

            layer = pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position='[Longitude, Latitude]',
                get_color='[255, 0, 0, 160]',  
                get_radius=10000,
                pickable=True,
            )

            view_state = pdk.ViewState(
                latitude=df["Latitude"].mean(),
                longitude=df["Longitude"].mean(),
                zoom=5,
                pitch=0,
            )

            st.pydeck_chart(pdk.Deck(
                map_style="mapbox://styles/mapbox/dark-v10",
                initial_view_state=view_state,
                layers=[layer],
            ))

with weather_forecast:
    st.markdown("""
    <style>
    .weather-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        font-size: 16px;
    }
    .weather-table th, .weather-table td {
        text-align: left;
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }
    .weather-table th {
        background-color: #f3f3f3;
        color: black;  /* Make the text black */
    }
    </style>

    <h4>🌤️ On-Demand Weather Forecasts</h4>

    <p>This agent delivers accurate, location-based weather forecasts — <b>only when you ask</b>.</p>

    <table class="weather-table">
    <tr>
        <th>🧾 How it works</th>
        <td>Type a message like <b>“Weather in Yangon”</b></td>
    </tr>
    <tr>
        <th>⚠️ Note</th>
        <td>Weather information is <b>not shown automatically</b> on this site</td>
    </tr>
    <tr>
        <th>📲 Ask Anytime</th>
        <td>You can ask your weather question in anytime</td>
    </tr>
    </table>
    """, unsafe_allow_html=True)

    chat_input = st.chat_input("Enter your weather question")
    if chat_input:
        with st.spinner("Generating response...", show_time=True):
            try:
                response = MyanmarNews.get_news(chat_input)
                if "<tool_call>" in response or "</tool_call>" in response:
                    #st.warning("Some tool_call content was detected and hidden.")
                    st.warning("Please try again later or please change the question.")       
                else:
                    st.markdown(response)
            except Exception as e:
                st.error(f"Server is Busy. Please try again later or change the question")