# CT Scan Contrast Prediction System  

---

## Project Steps  

### 1. Project Initialization    
Defining the topic: Predicting the use of contrast in CT Scans.  
Menentukan topik: Prediksi penggunaan kontras pada CT Scan.  
Setting up the project structure: Problem → Data → EDA → Modeling → Deployment → Documentation.  
Menetapkan struktur proyek: Problem → Data → EDA → Modeling → Deployment → Dokumentasi.  

### 2. Data Collection   
Downloading data from The Cancer Imaging Archive (TCIA).  
Mendownload data dari The Cancer Imaging Archive (TCIA).  
Image files in `.png`/`.jpg` format with labels in filenames (`T1` / `T0`).  
File gambar berformat `.png`/`.jpg` dengan nama mengandung label (`T1` / `T0`).  

### 3. Data Preparation  
Extracting labels from filenames and removing corrupted images.  
Mengekstrak label dari nama file dan menghapus gambar rusak.  
Organizing data into a DataFrame.  
Menyusun data numerik dalam bentuk DataFrame.  
Combining image paths and labels for training.  
Menggabungkan citra dan label untuk pelatihan model.  

### 4. Exploratory Data Analysis (EDA)   
Visualizing label distribution and image samples.  
Melihat distribusi label dan contoh gambar dari tiap kelas.  
Ensuring data quality through visual validation.  
Memastikan kualitas data melalui validasi visual.  

### 5. Feature Engineering   
Preprocessing images: grayscale, resize 150x150, normalize 0–1.  
Preprocessing gambar: grayscale, resize 150x150, normalisasi 0–1.  

### 6. Model Development   
Building a CNN using TensorFlow/Keras with Conv2D and Dense layers.  
Membangun CNN dengan TensorFlow/Keras menggunakan layer Conv2D dan Dense.  
Using Binary Crossentropy and Adam Optimizer.  
Menggunakan Binary Crossentropy dan Adam Optimizer.  

### 7. Model Training & Evaluation  
Training on train/val split and evaluating accuracy & confusion matrix.  
Melatih model dengan data train/val dan evaluasi dengan akurasi & confusion matrix.  
Saving model as `ct_cnn_model.h5`.  
Menyimpan model sebagai `ct_cnn_model.h5`.  

### 8. Gradio App Implementation    
Building prediction function + PDF export with FPDF.  
Membuat fungsi prediksi dan export PDF dengan FPDF.  
Designing `app.py` for deployment.  
Menyusun `app.py` untuk keperluan deployment.  

### 9. Deployment 
Deploying interactive Gradio app on Hugging Face Spaces.  
Mendeploy aplikasi interaktif Gradio di Hugging Face Spaces.  
Live demo link: [https://huggingface.co/spaces/Apil31/ct-scan-predictor](https://huggingface.co/spaces/Apil31/ct-scan-predictor)  
Link demo langsung: [https://huggingface.co/spaces/Apil31/ct-scan-predictor](https://huggingface.co/spaces/Apil31/ct-scan-predictor)  
Users can try the model directly via browser.  
Pengguna dapat mencoba model langsung melalui browser.  

### 10. GitHub Publication   
Uploaded Jupyter Notebook (`.ipynb`) version to GitHub.  
Mengunggah versi Notebook (`.ipynb`) ke GitHub.  
Excluded `.h5` model (size >25MB), provided via Hugging Face.  
Tidak mengunggah file `.h5` karena >25MB, tersedia melalui Hugging Face.  

### 11. Final Documentation   
Provided user instructions and demo usage notes.  
Memberikan instruksi pengguna dan catatan penggunaan demo.  
**WARNING: This project is not intended for official medical diagnosis.**  
**PERINGATAN: Proyek ini tidak ditujukan untuk diagnosis medis resmi.**

---

## Created by: Havilz 

**Contact:** havilzlating31@gmail.com | WhatsApp: +62-8138-0100-865  
