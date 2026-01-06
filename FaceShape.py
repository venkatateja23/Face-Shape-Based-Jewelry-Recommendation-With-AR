def detectFaceShape(imagepath):
    import numpy as np
    import cv2
    import dlib
    from sklearn.cluster import KMeans
    face_cascade_path = "haarcascade_frontalface_default.xml"
    datFile = "shape_predictor_81_face_landmarks.dat"
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)
    predictor = dlib.shape_predictor(datFile)
    image = cv2.imread(imagepath)
    image = cv2.resize(image, (500, 500))
    original = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray, (3, 3), 0)
    faces = faceCascade.detectMultiScale(
        gauss,
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print("found {0} faces!".format(len(faces)))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
        detected_landmarks = predictor(image, dlib_rect).parts()
        landmarks = np.matrix([[p.x, p.y] for p in detected_landmarks])
    results = original.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(results, (x, y), (x + w, y + h), (0, 255, 0), 2)
        temp = original.copy()
        forehead = temp[y:y + int(0.25 * h), x:x + w]
        rows, cols, bands = forehead.shape
        X = forehead.reshape(rows * cols, bands)
    kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)
    for i in range(0, rows):
        for j in range(0, cols):
            if y_kmeans[i * cols + j] == True:
                forehead[i][j] = [255, 255, 255]
            if y_kmeans[i * cols + j] == False:
                forehead[i][j] = [0, 0, 0]
    forehead_mid = [int(cols / 2), int(rows / 2)]
    lef = 0
    pixel_value = forehead[forehead_mid[1], forehead_mid[0]]
    for i in range(0, cols):
        if forehead[forehead_mid[1], forehead_mid[0] - i].all() != pixel_value.all():
            lef = forehead_mid[0] - i
            break;
    left = [lef, forehead_mid[1]]
    rig = 0
    for i in range(0, cols):
        if forehead[forehead_mid[1], forehead_mid[0] + i].all() != pixel_value.all():
            rig = forehead_mid[0] + i
            break;
    right = [rig, forehead_mid[1]]
    line1 = np.subtract(right + y, left + x)[0]
    cv2.line(results, tuple(x + left), tuple(y + right), color=(0, 255, 0), thickness=2)
    cv2.putText(results, ' Line 1', tuple(x + left), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0),
                thickness=2)
    cv2.circle(results, tuple(x + left), 5, color=(255, 0, 0), thickness=-1)
    cv2.circle(results, tuple(y + right), 5, color=(255, 0, 0), thickness=-1)
    linepointleft = (landmarks[1, 0], landmarks[1, 1])
    linepointright = (landmarks[15, 0], landmarks[15, 1])
    line2 = np.subtract(linepointright, linepointleft)[0]
    cv2.line(results, linepointleft, linepointright, color=(0, 255, 0), thickness=2)
    cv2.putText(results, ' Line 2', linepointleft, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0),
                thickness=2)
    cv2.circle(results, linepointleft, 5, color=(255, 0, 0), thickness=-1)
    cv2.circle(results, linepointright, 5, color=(255, 0, 0), thickness=-1)
    linepointleft = (landmarks[3, 0], landmarks[3, 1])
    linepointright = (landmarks[13, 0], landmarks[13, 1])
    line3 = np.subtract(linepointright, linepointleft)[0]
    cv2.line(results, linepointleft, linepointright, color=(0, 255, 0), thickness=2)
    cv2.putText(results, ' Line 3', linepointleft, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0),
                thickness=2)
    cv2.circle(results, linepointleft, 5, color=(255, 0, 0), thickness=-1)
    cv2.circle(results, linepointright, 5, color=(255, 0, 0), thickness=-1)
    linepointbottom = (landmarks[8, 0], landmarks[8, 1])
    linepointtop = (landmarks[8, 0], y)
    line4 = np.subtract(linepointbottom, linepointtop)[1]
    cv2.line(results, linepointtop, linepointbottom, color=(0, 255, 0), thickness=2)
    cv2.putText(results, ' Line 4', linepointbottom, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0),
                thickness=2)
    cv2.circle(results, linepointtop, 5, color=(255, 0, 0), thickness=-1)
    cv2.circle(results, linepointbottom, 5, color=(255, 0, 0), thickness=-1)
    similarity = np.std([line1, line2, line3])
    ovalsimilarity = np.std([line2, line4])
    ax, ay = landmarks[3, 0], landmarks[3, 1]
    bx, by = landmarks[4, 0], landmarks[4, 1]
    cx, cy = landmarks[5, 0], landmarks[5, 1]
    dx, dy = landmarks[6, 0], landmarks[6, 1]
    import math
    from math import degrees
    alpha0 = math.atan2(cy - ay, cx - ax)
    alpha1 = math.atan2(dy - by, dx - bx)
    alpha = alpha1 - alpha0
    angle = abs(degrees(alpha))
    angle = 180 - angle
    for i in range(1):
        if similarity < 10:
            if angle < 160:
                print('squared shape.Jawlines are more angular')
                break
            else:
                print('round shape.Jawlines are not that angular')
                break
        if line3 > line1:
            if angle < 160:
                print('triangle shape.Forehead is more wider')
                break
        if ovalsimilarity < 10:
            print('diamond shape. line2 & line4 are similar and line2 is slightly larger')
            break
        if line4 > line2:
            if angle < 160:
                print('rectangular. face length is largest and jawline are angular ')
                break;
            else:
                print('oblong. face length is largest and jawlines are not angular')
                break;
        print("Failed to detect face shape!")
    output = np.concatenate((original, results), axis=1)
    cv2.imshow('FaceShape Detection', output)
    cv2.waitKey(0)

