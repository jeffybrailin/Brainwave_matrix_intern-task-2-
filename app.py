import streamlit as st
from diffusers import StableDiffusionPipeline

# Load the model
@st.cache_resource  # Cache model to save time
def load_model():
    return StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to("cpu")

pipe = load_model()

# App title
st.title("Text-to-Image Generation App")

# Input text
text_input = st.text_input("Enter your text:")

# Generate button
if st.button("Generate Image"):
    if text_input:
        st.write("Generating image, please wait...")
        # Generate image
        image = pipe(text_input).images[0]
        st.image(image, caption="Generated Image")
    else:
        st.warning("Please enter some text to generate an image!")

# Footer
st.markdown("Created for AIML Internship ✨")
