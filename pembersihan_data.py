import re
import pandas as pd

def clean_text(text):
    """
    Menghapus timestamp, nama pengirim, dan karakter selain angka, huruf, dan tanda baca umum.
    """
    # Menghapus timestamp (format [DD/MM/YY HH:MM:SS])
    text = re.sub(r'\[\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\]', '', text)

    # Menghapus nama pengirim (format: nama pengirim diikuti dengan tanda ':')
    text = re.sub(r'^[^:]+:', '', text)

    # Hanya mengambil angka, huruf, dan tanda baca umum
    text = re.sub(r'[^a-zA-Z0-9 .,!?]', '', text)

    return text.strip()

# Membaca file CSV tanpa header, misalnya data_group.csv
data = pd.read_csv('data_group.csv', header=None, names=['message'])

# Membersihkan data pesan
data['cleaned_message'] = data['message'].apply(clean_text)

# Menghapus baris yang mengandung kata-kata "omitted" atau nama file yang di-omit
data_cleaned = data[~data['cleaned_message'].str.contains(r'omitted|\.pdf', na=False)]

# Menyimpan hasil pembersihan ke CSV baru
data_cleaned[['cleaned_message']].to_csv('cleaned_data.csv', index=False)
print("Data telah dibersihkan dan disimpan ke 'cleaned_data.csv'.")
