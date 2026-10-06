import streamlit as st
import joblib

# Load model


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "final_rev_data.pkl")

model = joblib.load(model_path)


# Page
st.title("🍽️ Restaurant Review Sentiment Analysis")
st.write("Enter a restaurant review below to analyze its sentiment:")

# ---------------- SIDEBAR ----------------

st.sidebar.image(
    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800"
)

st.sidebar.title("About Us")
st.sidebar.write(
    "This app uses a Machine Learning model to analyze "
    "the sentiment of restaurant reviews. It can classify "
    "reviews as positive, negative, or neutral."
)

st.sidebar.title("How to Use")

st.sidebar.write("1. Enter a restaurant review in Hinglish and English.")
st.sidebar.write("2. Click the 'Analyze Sample Review' button.")
st.sidebar.write("3. View the predicted sentiment.")

st.sidebar.title("Tech Stack")

st.sidebar.write("🐍 Python")
st.sidebar.write("🎈 Streamlit")
st.sidebar.write("🤖 Scikit-learn")
st.sidebar.write("📦 Joblib")


# ---------------- INPUT ----------------

sam = st.text_input(
    "Enter a sample review in Hinglish and English:",
    placeholder="Example: The food was amazing and the service was excellent!"
)


# ---------------- ANALYSIS ----------------

if st.button("🔍 Analyze Sample Review"):

    if sam.strip() == "":
        st.warning("⚠️ Please enter a review first.")

    else:

        prediction = model.predict([sam])[0]
        prediction = str(prediction).lower()

        # -------- POSITIVE --------

        if prediction == "positive":

            st.success("😊 Positive Review")

            st.write("Sentiment:", prediction.capitalize())

            # Normal Streamlit celebration
            st.balloons()


        # -------- NEGATIVE --------

        elif prediction == "negative":

            st.error("😞 Negative Review")

            st.write("Sentiment:", prediction.capitalize())

            # Red balloon animation
            st.markdown("""
            <style>

            .balloon-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: 9999;
            }

            .red-balloon {
                position: absolute;
                bottom: -150px;
                width: 55px;
                height: 70px;
                background: red;
                border-radius: 50%;
                animation: floatUp 5s linear infinite;
            }

            .red-balloon::after {
                content: "";
                position: absolute;
                bottom: -80px;
                left: 27px;
                width: 2px;
                height: 80px;
                background: #555;
            }

            .b1 {
                left: 10%;
                animation-delay: 0s;
            }

            .b2 {
                left: 30%;
                animation-delay: 1s;
            }

            .b3 {
                left: 50%;
                animation-delay: 2s;
            }

            .b4 {
                left: 70%;
                animation-delay: 0.5s;
            }

            .b5 {
                left: 90%;
                animation-delay: 1.5s;
            }

            @keyframes floatUp {

                0% {
                    transform: translateY(0);
                    opacity: 1;
                }

                100% {
                    transform: translateY(-110vh);
                    opacity: 0;
                }

            }

            </style>

            <div class="balloon-container">

                <div class="red-balloon b1"></div>
                <div class="red-balloon b2"></div>
                <div class="red-balloon b3"></div>
                <div class="red-balloon b4"></div>
                <div class="red-balloon b5"></div>

            </div>
            """, unsafe_allow_html=True)


        # -------- NEUTRAL --------

        else:

            st.info("😐 Neutral Review")

            st.write(
                "Sentiment:",
                prediction.capitalize()
            )
