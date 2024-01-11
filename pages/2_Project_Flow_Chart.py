import streamlit as st
import streamlit.components.v1 as components
import base64

st.title('🎈 Project Flow Chart')

# File path to your PDF
pdf_file_path = 'flowchart.pdf'

# Read the PDF file as a binary file
with open(pdf_file_path, "rb") as f:
    pdf_data = f.read()

# Encode the PDF file as base64
pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

# Embed the PDF using an iframe
#st.markdown(f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="1000" style="border: none;"></iframe>', unsafe_allow_html=True)

# Embedding PDF in HTML
pdf_display = F'<embed src="data:application/pdf;base64,{pdf_base64}" width="720" height="1480" type="application/pdf">'

# Displaying File
st.markdown(pdf_display, unsafe_allow_html=True)
#pdf_display = F'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="1000" type="application/pdf"></iframe>'