import os
import streamlit as st
from transformers import pipeline

# Set cache directory
os.environ["TRANSFORMERS_CACHE"] = "/tmp/cache"

# Judul Web
st.title("Bot Bangun Ruang AI")

# Load model GPT-2 dari Hugging Face
try:
    generator = pipeline("text-generation", model="distilgpt2")
except Exception as e:
    st.error(f"Gagal memuat model: {e}")

# Baca materi dari file
try:
    with open("materi.txt", "r") as file:
        materi = file.read()
except Exception as e:
    st.error(f"Gagal membaca file materi: {e}")

# Input pengguna
user_input = st.text_input("Apa yang ingin Anda tanyakan tentang bangun ruang?")

# Generate jawaban
if user_input:
    try:
        # Gabungkan pertanyaan dengan konteks materi
        prompt = f"Berikut adalah materi bangun ruang:\n\n{materi}\n\nPertanyaan: {user_input}\nJawaban:"
        
        # Potong input jika terlalu panjang
        prompt = prompt[:500]  # Batasi input menjadi 500 karakter
        
        # Generate jawaban dengan max_new_tokens dan truncation
        response = generator(prompt, max_new_tokens=100, truncation=True)
        st.write(response[0]['generated_text'])
    except Exception as e:
        st.error(f"Gagal menghasilkan jawaban: {e}")