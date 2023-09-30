import cv2
def cam_capture():
    video = cv2.VideoCapture()
    ip = "https://ipexterno:8080/video"
    video.open(ip)

    while True:
        check, img = video.read()
        cv2.imshow("img", img)
        cv2.waitKey(1) 

if __name__ == '__main__':
    cam_capture()