import qrcode

url = input("Enter the url>>>").strip()#Strip unecessary white space '.strip()' function is used
file_path = "C:\\Users\\DELL\\Desktop\\qrcode.png"

#Genrating a QR code python object

qr = qrcode.QRCode()
qr.add_data(url) # adding our data

img = qr.make_image() #To generate qrcode image
img.save(file_path) #To save qrcode image

print("Your QRCode image is generated successfully")
