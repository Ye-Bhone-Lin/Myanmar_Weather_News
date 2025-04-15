# Myanmar Weather News

A real-time weather and earthquake information platform for Myanmar, providing localized updates and forecasts.

## 🌦️ Features

- **Real-time Weather Updates**: Get current weather conditions and forecasts for cities across Myanmar
- **Earthquake Alerts**: Receive instant updates about significant earthquakes in Myanmar and surrounding regions
- **Interactive Maps**: Visualize earthquake locations on an interactive map
- **Localized Information**: Weather and news tailored specifically for Myanmar

## Demonstration

![433768301-f144c74b-c96d-4e3c-97c5-79a8a7d2d8cc](https://github.com/user-attachments/assets/7ee6ef93-ffd3-423c-acf5-40aa0c704ae8)

The earthquake data and all about disaster news are updated every 6 hours.

![433768484-9e997b5f-94b8-425e-8988-4a00e8f627a5](https://github.com/user-attachments/assets/6d6efbd6-39c1-46e0-a73b-fef37b9975ba)

If the output includes the locations, we can clearly see where the earthquakes occurred on the map.

![433768878-0a03fafc-2095-4f19-b4a4-f009b4077fab](https://github.com/user-attachments/assets/29cc4856-a46a-41f4-80b9-bf65e14ca71d)

You can ask weather conditions in Weather Forecasts session.

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/Myanmar_Weather_News.git
   cd Myanmar_Weather_News
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv myvenv
   # On Windows
   myvenv\Scripts\activate
   # On macOS/Linux
   source myvenv/bin/activate
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
   ```

## 💻 Usage

1. Start the Streamlit application:

   ```
   streamlit run src/Home.py
   ```

2. Open your browser and navigate to the URL displayed in the terminal (typically )

3. Use the navigation menu to access different features:
   - **Home**: Overview of the application
   - **Get Weather News**: Access weather forecasts and earthquake information
   - **About**: Learn more about the project

## 📁 Project Structure

```
Myanmar_Weather_News/
├── src/
│   ├── Home.py                  # Main application entry point
│   ├── myanmar_news.py          # Core functionality for weather and news
│   ├── pages/
│   │   ├── About.py             # About page
│   │   └── Get_Weather_News.py  # Weather and news page
│   └── new.ipynb                # Development notebook
├── .env                         # Environment variables (API keys)
├── requirements.txt              # Project dependencies
└── README.md                    # Project documentation
```

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **LangChain**: Framework for LLM applications
- **Groq**: LLM provider
- **Folium**: Interactive map visualization
- **PyDeck**: 3D map visualization

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

Ye Bhone Lin - yebhonelin10@gmail.com

Project Link: [https://github.com/Ye-Bhone-Lin/Myanmar_Weather_News](https://github.com/Ye-Bhone-Lin/Myanmar_Weather_News)
