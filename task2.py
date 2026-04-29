import numpy as np
import cv2 as cv

cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Cannot open camera")
    exit()

fw = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
fh = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

k = 3

# load background once
bg = cv.imread("background.jpg")
bg = cv.resize(bg,(160,120))

while True:

    ret, frame = cam.read()
    if not ret:
        break

    frame = cv.flip(frame,1)

    # resize for faster clustering
    small = cv.resize(frame,(160,120))

    data = np.float32(small.reshape(-1,3))

    ret,label,center = cv.kmeans(
        data,
        k,
        None,
        (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER,10,1.0),
        5,
        cv.KMEANS_RANDOM_CENTERS
    )

    center = np.uint8(center)

    clustered = center[label.flatten()]
    clustered = clustered.reshape(small.shape)

    # find background cluster (largest one)
    counts = np.bincount(label.flatten())
    background_cluster = np.argmax(counts)

    # create mask
    mask = (label.flatten() != background_cluster)
    mask = mask.reshape((120,160))
    mask = mask.astype(np.uint8)*255

    # clean mask
    kernel = np.ones((5,5),np.uint8)

    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

    mask = cv.GaussianBlur(mask,(7,7),0)
    _,mask = cv.threshold(mask,127,255,cv.THRESH_BINARY)

    mask_inv = cv.bitwise_not(mask)

    fg = cv.bitwise_and(small, small, mask=mask)
    bg_part = cv.bitwise_and(bg, bg, mask=mask_inv)

    result = cv.add(fg, bg_part)

    # upscale to original webcam size
    frame = cv.resize(frame,(fw,fh))
    result = cv.resize(result,(fw,fh))
    clustered = cv.resize(clustered,(fw,fh))

    cv.imshow("Webcam", frame)
    cv.imshow("Virtual Background", result)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()