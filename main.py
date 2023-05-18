import qrcode

#img = qrcode.make("Hello world, this is Abood")
#img.save("mycode.png")

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=50,
                   border=10)

qr.add_data("https://www.a2fim.com")
qr.make(fit=True)

imp = qr.make_image(fill_color="black", back_color="white")
imp.save("advanced.png")