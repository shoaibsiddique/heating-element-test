
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(page_title="Analyze Data", page_icon="📈")

# ... (your existing code)

# Display images from the "patterns" folder
pattern_folder = "patterns"
pattern_images = os.listdir(pattern_folder)

if pattern_images:
    st.header("Pattern Images")
    
    num_images_to_display = 5
    selected_images = pattern_images[:num_images_to_display]

    for image_filename in selected_images:
        image_path = os.path.join(pattern_folder, image_filename)
        st.image(image_path, caption=f"Pattern Image: {image_filename}", use_column_width=True)

        # Display title below each image
        image_title = st.text_input(f"Title for {image_filename}:", key=image_filename)
        #st.write(f"Title: {image_title}")

else:
    st.warning("No images found in the 'patterns' folder.")
