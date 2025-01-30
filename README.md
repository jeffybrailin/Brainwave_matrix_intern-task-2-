# Text-to-Image Generation App  

This is a **Streamlit-based AI application** that generates images from text prompts using the **Stable Diffusion v1.5** model.  

---

## Features  
- **AI-powered image generation** using Stable Diffusion  
- **Interactive Streamlit UI** for seamless user experience  
- **Efficient model caching** to optimize performance  
- **Lightweight and easy-to-use interface**  

---

## Installation  

### Prerequisites  
Ensure you have Python installed, then install the required dependencies:  

```bash
pip install streamlit diffusers torch torchvision
```

### 🔹 Running the App  

```bash
streamlit run app.py
```

---

## How It Works  

The **Stable Diffusion v1.5 model** is loaded using `diffusers`.  
The user **enters a text prompt** into the input field.  
Clicking the **"Generate Image"** button runs the AI model to create an image.  
The generated image is displayed in the **Streamlit app**.  

---

## Sample Output  

 **Example Prompt:** `"A futuristic city at sunset"`  
 **Output:** An AI-generated image based on the prompt  


## Notes  
- This project utilizes **Stable Diffusion v1.5** for generating images from text prompts.  
- The `@st.cache_resource` decorator **optimizes performance** by caching the model.  
- Created as part of an **AIML Internship**.  


## License  
This project is **open-source** and available for modification.  

