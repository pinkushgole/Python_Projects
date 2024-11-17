import qrcode

qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

# data="https://www.youtube.com/"
data={
    "name":"xyz",
   }
qr.add_data(data)
qr.make(fit=True)
imag=qr.make_image(fill="black",back_color="white")
imag.save('p1.png')
