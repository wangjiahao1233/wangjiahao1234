import cv2
import numpy as np

# 读取视频文件
cap = cv2.VideoCapture('D:/桌面/test_blue.mp4')
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

while cap.isOpened():
    # 逐帧读取视频
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    max_contour = max(contours, key=cv2.contourArea)

    M = cv2.moments(max_contour)
    center_x = int(M['m10'] / M['m00'])
    center_y = int(M['m01'] / M['m00'])

    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)  # 中心点坐标
    for i in range(5):
        point_x = int(center_x + 50 * np.cos(i * 2 * np.pi / 5))
        point_y = int(center_y + 50 * np.sin(i * 2 * np.pi / 5))
        cv2.circle(frame, (point_x, point_y), 5, (0, 0, 255), -1)

    cv2.imshow('Video', frame)
cap.release()
cv2.destroyAllWindows()