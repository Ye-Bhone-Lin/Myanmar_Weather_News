import streamlit as st


st.markdown("<h1 style='text-align: center;'>Myanmar Weather News</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
        .nav-container {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 2rem;
        }
        .nav-card {
            background-color: #f0f8ff;
            border-radius: 12px;
            padding: 1.5rem 2rem;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transition: all 0.2s ease;
            width: 250px;
        }
        .nav-card:hover {
            background-color: #e0f2fe;
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        }
        .nav-card a {
            text-decoration: none;
            color: #1f77b4;
            font-size: 18px;
            font-weight: 600;
        }
    </style>

    <div class="nav-container">
        <div class="nav-card">
            <a href="/About" target="_self">📘 About This Project</a>
        </div>
        <div class="nav-card">
            <a href="/Get_Weather_News" target="_self">🌤 Get Weather News</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<p style='text-align: center; margin-top: 3rem;'>Welcome to the live weather update center. Stay informed with the latest conditions and alerts across Myanmar.</p>", unsafe_allow_html=True)


