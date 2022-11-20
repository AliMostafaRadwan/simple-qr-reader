import glob
import cv2
import webbrowser


# def qr_reader(file):
#     try:
#         img=cv2.imread(file)
#         detect = cv2.QRCodeDetector()
#         value,points,straight_qrcode = detect.detectAndDecode(img)
#         return value
#     except:
#         return
    
# print(qr_reader('unknown-1.png'))


cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()


while True:
    _,img = cap.read()
    data,bbox,_ =detector.detectAndDecode(img)
    

    cv2.imshow('qr',img)
    print(str(data))
    if cv2.waitKey(1) == ord('q'):
        break
    
