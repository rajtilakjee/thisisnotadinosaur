import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
import PIL.Image


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

st.set_page_config(
    page_title="This is Not a Dinosaur",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.image('static/dino-logo.png',width=100)
st.header("THIS :green[IS] :orange[NOT] A :blue[DINOSAUR]", divider='rainbow')
st.markdown(':green[_Jurassic or Just-a-pic? Let our Dino-Detective decide!_]')

with st.sidebar:
    st.header("What's this?!", divider='rainbow')
    st.write("This is a simple app that accepts an image from the user and detects if any Dinosaus are present in that image.")
    st.header("But why!", divider='rainbow')
    st.write("For fun! ... err, not really. I am a Machine Learning Engineer with around 20 years of work experience. I have created a number of apps but I am too afraid to release them. It's because I have been searching for a job but not finding any, which made me think do I really know coding at all. So I thought about starting simple, and that's how this was created. [Here's where I go the inspiration from](https://www.reddit.com/r/AskReddit/comments/bg8vc/comment/c0mmeos/).")
    st.header("Noice! What can I do?", divider='rainbow')
    st.write("Simple. Let me know what do you think about this on the GitHub repository for this app; whether you like it, had fun with it, anything. It would work as a moral booster for me. Feel free to contribute if you want. If you are feeling generous, consider donating so that I can continue to create more apps like this.")

file = st.file_uploader("Upload the photo or image you want to check for any hidden Dinosaurs.", type=["jpg", "jpeg", "png"])
img, result = st.columns(2)

with img:
    st.info('Here is your uploaded photograph.', icon="ℹ️")
    if file is not None:
        image = PIL.Image.open(file)
        st.image(file,width=350)

with result:
    st.info('Is this a Dinosaur?', icon="ℹ️")
    if file is not None:
        model = genai.GenerativeModel('gemini-pro-vision',safety_settings=safety_settings)
        response = model.generate_content(["Observe the image and reply with a funny note about whether a Dinosaur is present in the image or not.", image], stream=True)
        response.resolve()
        for candidate in response.candidates:
            st.write(part.text for part in candidate.content.parts)

st.link_button('Report Feedback, Issues, or Contribute!', "https://github.com/rajtilakjee/thisisnotadinosaur/issues", use_container_width=True)
