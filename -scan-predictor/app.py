
import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
from fpdf import FPDF
import uuid
import os

model = tf.keras.models.load_model("ct_cnn_model.h5")
os.makedirs("pdf_reports", exist_ok=True)

def preprocess(img):
    img = img.convert("L")
    img = img.resize((150, 150))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 150, 150, 1)
    return img_array

def predict_contrast_with_pdf(img):
    img_array = preprocess(img)
    pred = model.predict(img_array)[0][0]
    label = "Dengan Kontras (1)" if pred > 0.5 else "Tanpa Kontras (0)"
    confidence = f"{pred:.2f}"
    result = f"{label} - Confidence: {confidence}"

    temp_img_path = f"temp_{uuid.uuid4().hex[:6]}.jpg"
    img.save(temp_img_path)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Hasil Prediksi Kontras CT Scan", ln=True, align="C")
    pdf.ln(10)
    pdf.image(temp_img_path, x=30, y=30, w=150)
    pdf.ln(100)
    pdf.set_font("Arial", size=12)
    pdf.ln(100)
    pdf.multi_cell(0, 10, f"Hasil Prediksi: {label}\nConfidence Score: {confidence}")

    filename = f"pdf_reports/hasil_prediksi_{uuid.uuid4().hex[:6]}.pdf"
    pdf.output(filename)

    os.remove(temp_img_path)

    return result, filename

interface = gr.Interface(
    fn=predict_contrast_with_pdf,
    inputs=gr.Image(type="pil"),
    outputs=["text", "file"],
    title="Prediksi Kontras CT Scan",
    description="Upload gambar CT scan. Sistem akan memprediksi apakah menggunakan kontras atau tidak, dan hasilnya dapat diunduh dalam bentuk PDF."
)

interface.launch()
