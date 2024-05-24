import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', img)

# capture = cv.VideoCapture('Video/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
    
#     if cv.waitKey(20) & 0xFF==ord('q'):
#         break

# capture.release()
# cv.destroyAllWindows()

cv.waitKey(0)

