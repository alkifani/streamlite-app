# Project Menggunakan Streamlite (Belajar Analisis Data dengan Python)

## Project Analisis Data

Repository ini berisi proyek data analytics yang saya kerjakan. Deployment in **Streamlit**

## Deskripsi

Proyek ini bertujuan untuk menganalisis data pada Bike Sharing Dataset. Tujuan akhirnya adalah untuk menghasilkan wawasan dan informasi yang berguna dari data yang dianalisis.

## Struktur Direktori

- **/data**: Direktori ini berisi data mentah yang digunakan dalam proyek, dalam format .csv .
- **/dashboard**: Direktori ini berisi main.py yang digunakan untuk membuat dashboard hasil analisis data.
- **notebook.ipynb**: File ini yang digunakan untuk melakukan analisis data.

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir streamlite-app
cd streamlite-app
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Instalasi

1. Clone repository ini ke komputer lokal Anda menggunakan perintah berikut:

   ```shell
   git clone https://github.com/alkifani/streamlite-app.git
   ```

2. Pastikan Anda memiliki lingkungan Python yang sesuai dan pustaka-pustaka yang diperlukan. Anda dapat menginstal pustaka-pustaka tersebut dengan menjalankan perintah berikut:

    ```shell
    pip install streamlit
    pip install -r requirements.txt
    ```

## Penggunaan
1. Masuk ke direktori proyek (Local):

    ```shell
    cd bike-sharing/dashboard/
    streamlit run dashboard.py
    ```
    Atau bisa dengan kunjungi website ini [Project Data Analytics](https://test/)

## Kontribusi
Anda dapat berkontribusi pada proyek ini dengan melakukan pull request. Pastikan untuk menjelaskan perubahan yang Anda usulkan secara jelas dan menyeluruh.

