# QR Code Generator
# PyQRCodeNG version https://github.com/pyqrcode/pyqrcodeNG

import streamlit as st
import pyqrcodeng as pyqrcode
from PIL import Image

QR_FILE = 'qrcode.png'
QR_CODE_COLOR = (80, 20, 80, 255)
BACKGROUND_COLOR = (245, 245, 245, 255)

st.title('QR Code Generator App')
st.subheader('You can generate a QR code from a string or URL.')
st.text('PyQRCodeNG version')
qr_url = st.text_input('Enter a string or URL to generate a QR code:', value='https://code2create.club/')

name = st.text_input('Size', 0)
