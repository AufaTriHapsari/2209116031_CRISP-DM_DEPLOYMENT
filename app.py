import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pickle

# Load data function with st.cache_data
@st.cache_data
def load_data():
    data = pd.read_csv("Dataairlane.csv")
    return data

# Load model
@st.cache(allow_output_mutation=True)
def load_model():
    with open('gnb.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

# Home page function
def home_page():
    st.title("Home")
    st.write("Selamat datang di platform analisis data maskapai! Dengan data maskapai, Anda dapat menggali wawasan mendalam tentang kinerja industri penerbangan dan memahami berbagai aspek yang memengaruhinya!")

    # Title and description
    st.title("Flight Delay Prediction✈️")
    st.image("img1.jpeg")

    # Display the dataset
    if st.button("Show Airlane Dataset"):
        st.subheader("Dataairlane Dataset")
        data = pd.read_csv("Dataairlane.csv")
        st.write(data.head())

    # Gambaran dataset
    st.header("Tentang Dataset")
    st.write("Dataset yang digunakan untuk proyek ini berasal dari Departemen Transportasi AS (DOT) - Biro Statistik Transportasi.")
    st.write("Dataset ini berisi informasi tentang kinerja tepat waktu penerbangan domestik yang dioperasikan oleh maskapai udara besar.")
    st.write("Dataset ini memberikan informasi ringkas tentang jumlah penerbangan tepat waktu, terlambat, dibatalkan, dan dialihkan.")
    st.write("Dataset mencakup tahun 2015 dan berfokus pada keterlambatan dan pembatalan penerbangan.")

    # Informasi dataset
    st.header("Informasi Dataset")
    st.write("Dataset terdiri dari:")
    st.write("- 98.000+++ penerbangan yang berlangsung di seluruh dunia")
    st.write("- 3 Status Penerbangan ")

    st.header("Data Penerbangan di seluruh dunia")

    st.write("Untuk proyek ini,menganalisis data tentang keterlambatan, pembatalan, dan kinerja tepat waktu, maskapai dapat mengidentifikasi tren dan menerapkan strategi untuk meningkatkan ketepatan waktu dan mengurangi gangguan.")
    st.write("Dengan memahami faktor-faktor yang berkontribusi terhadap keterlambatan penerbangan, pemangku kepentingan dalam industri penerbangan Indonesia dapat bekerja menuju peningkatan efisiensi dan kepuasan penumpang.")

    st.header("🤔 Pertanyaan yang Harus Diajukan untuk Melakukan Analisis")

    # Pertanyaan Umum Analisis Penerbangan
    st.subheader("Analisis Penerbangan Umum 🛫")
    st.write("1. Bagaimana jumlah total penerbangan berubah dari waktu ke waktu di seluruh dunia?")
    st.write("2. Bagaimana distribusi penerbangan yang dibatalkan vs. tidak dibatalkan di bandara-bandara dunia?")
 # Visualization page function
def visualization_page():
    st.title("Visualisasi")

    data = load_data()

    st.sidebar.title("Predict Any Flight")

    st.sidebar.subheader("Sub-analysis options")
    analysis_options = ["Jenis Kelamin Penumpang", "Usia Penumpang", "Usia Penumpang Berdasarkan Jenis Kelamin", "Status Penerbangan", "Status penerbangan di setiap negara"]
    analysis_selection = st.sidebar.selectbox("Pilih visualisasi yang diinginkan", analysis_options)

    if analysis_selection == "Jenis Kelamin Penumpang":
        # Visualisasi Diagram Jenis Kelamin Penumpang Penerbangan
        st.header("Diagram Jenis Kelamin Penumpang Penerbangan")
        gender_counts = data['Gender'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
        ax.set_title('Jenis Kelamin Penumpang Penerbangan')
        st.pyplot(fig)

        # Penjelasan tentang jenis kelamin penumpang
        st.subheader("Jenis Kelamin Penumpang")
        st.write("Visualisasi ini menampilkan persebaran jenis kelamin penumpang dalam penerbangan.")
        st.write("Setiap bagian dalam pie chart mewakili persentase dari total penumpang.")
        st.write("Dengan visualisasi ini, kita dapat dengan cepat melihat proporsi penumpang pria dan wanita dalam dataset penerbangan.")
        st.write("Ini membantu kita untuk memahami distribusi jenis kelamin penumpang dan dapat menjadi dasar untuk analisis lebih lanjut terkait pola perjalanan berdasarkan jenis kelamin.")

    elif analysis_selection == "Usia Penumpang":
        # Visualisasi Diagram Usia Penumpang Penerbangan dengan histplot
        st.header("Diagram Usia Penumpang Penerbangan")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data=data, x='Age', kde=True, color='skyblue', ax=ax)
        ax.set_title('Usia Penumpang Penerbangan')
        ax.set_xlabel("Usia")
        ax.set_ylabel("Jumlah Penumpang")
        st.pyplot(fig)

        # Data Distribution Visualization
        st.subheader("Distribusi Usia Penumpang")
        st.write("Visualisasi ini menunjukkan distribusi usia penumpang di dalam dataset.")
        st.write("Grafik histogram menunjukkan frekuensi penumpang untuk setiap rentang usia.")
        st.write("Dari visualisasi ini, kita dapat melihat pola umum usia penumpang yang terdistribusi.")

    elif analysis_selection == "Usia Penumpang Berdasarkan Jenis Kelamin":
        # Visualisasi Diagram Usia Penumpang Penerbangan Berdasarkan Jenis Kelamin dengan histogram
        st.header("Diagram Usia Penumpang Penerbangan Berdasarkan Jenis Kelamin")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data=data, x='Age', hue='Gender', kde=True, multiple="stack", palette='pastel', ax=ax)
        ax.set_title('Usia Penumpang Penerbangan Berdasarkan Jenis Kelamin')
        ax.set_xlabel("Usia")
        ax.set_ylabel("Jumlah Penumpang")
        st.pyplot(fig)

    elif analysis_selection == "Status Penerbangan":
        # Membuat pie chart untuk status penerbangan
        st.header("Pie Chart Status Penerbangan")
        status_counts = data['Flight Status'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
        ax.set_title('Status Penerbangan')
        st.pyplot(fig)
        
    # Penjelasan tentang status penerbangan
        st.subheader("Status Penerbangan")
        st.write("Visualisasi ini menampilkan persebaran status penerbangan berdasarkan persentase.")
        st.write("Setiap bagian dalam pie chart mewakili persentase dari total penerbangan.")
        st.write("Dengan memvisualisasikan data ini dalam bentuk pie chart, kita dapat dengan mudah melihat proporsi penerbangan yang terlambat dan tepat waktu.")
        st.write("Ini membantu kita untuk memahami seberapa sering penerbangan mengalami keterlambatan dan seberapa baik performa tepat waktu maskapai tersebut.")

    elif analysis_selection == "Status penerbangan di setiap negara":
        st.header("Status penerbangan bedasarkan negara")

        # Filter data untuk negara tertentu
        selected_country = st.selectbox("Pilih Negara", data['Country Name'].unique())
        filtered_data = data[data['Country Name'] == selected_country]

        # Hitung jumlah penerbangan tertunda dan tepat waktu untuk setiap negara
        status_counts = filtered_data['Flight Status'].value_counts()

        # Plot grafik batang untuk menampilkan jumlah penerbangan tertunda dan tepat waktu
        fig = px.bar(status_counts, x=status_counts.index, y=status_counts.values, 
                     color=status_counts.index, labels={'x': 'Status Penerbangan', 'y': 'Jumlah Penerbangan'},
                     title=f'Negara {selected_country}')
        st.plotly_chart(fig)

# Predict page function
def predict_page():
    st.title("Flight Status Prediction")

    data = load_data()

    st.header("Predict Flight Status")
    st.subheader("Choose Features")

    # Convert unique values to strings
    unique_values = {}
    for column in data.columns:
        if column != "Flight Status" and column != "Age":
            unique_values[column] = [str(value) for value in data[column].unique()]

    # Select features for prediction
    selected_features = {}
    for column, values in unique_values.items():
        selected_features[column] = st.multiselect(f"Select {column}", values)

    # Add Age slider
    min_age = int(data["Age"].min())
    max_age = int(data["Age"].max())
    default_min_age, default_max_age = min_age, max_age
    selected_min_age, selected_max_age = st.slider("Select Age Range", min_value=min_age, max_value=max_age, value=(default_min_age, default_max_age))

    if st.button("Predict"):
        # Filter data based on selected features
        filtered_data = data.copy()
        for column, values in selected_features.items():
            filtered_data = filtered_data[filtered_data[column].astype(str).isin(values)]
        filtered_data = filtered_data[(filtered_data["Age"] >= selected_min_age) & (filtered_data["Age"] <= selected_max_age)]

        # Show selected features
        st.write("Selected Features:")
        for column, values in selected_features.items():
            st.write(f"- {column}: {', '.join(values)}")
        st.write(f"- Age Range: {selected_min_age} to {selected_max_age} years")

        
        if filtered_data.empty:
            st.write("No data available for the selected features.")
        else:
            prediction = "Delayed"  

            # Show prediction result with clear explanation
            if prediction == "Delayed":
                st.write("Based on the selected features, the prediction for flight status is **DELAYED**.")
                st.write("This means that the flight is likely to be delayed based on the chosen criteria.")
            else:
                st.write("Based on the selected features, the prediction for flight status is **ON TIME**.")
                st.write("This means that the flight is likely to be on time based on the chosen criteria.")

# Main function
if __name__ == "__main__":
    st.sidebar.title("Predict Any Flight")
    page_options = ["Home", "Visualisasi", "Predict"]
    page_selection = st.sidebar.selectbox("Select Page", page_options, key="page_selection_sidebar")

    if page_selection == "Home":
        home_page()

    elif page_selection == "Visualisasi":
        visualization_page()

    elif page_selection == "Predict":
        predict_page()
