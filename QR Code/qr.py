
import qrcode


qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data("https://www.example.com")
qr.make(fit=True)
img = qr.make_image(fill_color="yellow", back_color="white")
img.save("qrcode.png")
