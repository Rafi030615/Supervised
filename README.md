# Menjalankan Streamlit

Berikut adalah langkah-langkah untuk menjalankan aplikasi Streamlit:

1. Jika Anda belum menginstal `virtualenv`, instal terlebih dahulu dengan perintah berikut:
   ```bash
   pip install virtualenv
   ```

2. Jika Anda sudah menginstal `virtualenv` sebelumnya, buat virtual environment dengan nama `myenv` dengan perintah berikut:
   ```bash
   python -m virtualenv myenv
   ```

3. Aktifkan virtual environment yang telah dibuat:
   
   Windows
   ```bash
   myenv\Scripts\activate
   ```

   MacOS / Linux
   ```bash
   source myenv\Scripts\activate
   ```

4. Install semua dependensi yang diperlukan dari file `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. Jalankan aplikasi Streamlit dengan perintah berikut:
   ```bash
   streamlit run app.py
   ```

