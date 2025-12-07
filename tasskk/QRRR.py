
from tkinter import *
from PIL import Image, ImageTk
import qrcode

#  QR Code

def generate_qr():
    text = entry.get()
    if text == "":
        result_label.config(text=" Enter text first", fg="red")
        return

    qr = qrcode.QRCode( version=1,box_size=10,border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save("qr_code.png")

    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    result_label.config(text="QR code was created successfully and saved", fg="green")


# إنشاء نافذة الـ Gui

qr_app= Tk()
qr_app.title("QR Code Generator")
qr_app.geometry("450x550")
qr_app.configure(bg="#FA97A4") 

# ال  run   

Label(qr_app, text="QR Code Generator", font=("Arial", 20, "bold"), bg="#FD5F6C", fg="#820016").pack(pady=15)

entry = Entry(qr_app, font=("Arial", 14), width=30)
entry.pack(pady=10)
Button(qr_app, text="Generate QR code", font=("Arial", 14, "bold"),  bg="#B32141", fg="white", command=generate_qr).pack(pady=10)

qr_label = Label(qr_app, bg="#F56068")
qr_label.pack(pady=10)

result_label = Label(qr_app, text="", font=("Arial", 12), bg="#F3E4E8")
result_label.pack(pady=10)

qr_app.mainloop()
