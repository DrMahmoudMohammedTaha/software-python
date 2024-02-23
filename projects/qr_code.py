

# pip install qrcode[pil]

import qrcode

text = "محمد احمد حسن \n رواية حفص عن عاصم"
qr_text = qrcode.make(text)
qr_text.save("H:\\text_qr_code.png")

