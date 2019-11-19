import os
import cv2 as cv


def main():
    rtsp_stream = 'rtsp://admin:region18@192.168.30.25:554/av0_0'
    example_rtsp = 'rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa'

    record_video_from_rtsp = 'ffmpeg -i rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa -c copy -map 0 -f segment -segment_time 1 -segment_format mp4 "capture-%03d.mp4"'
    show_json = 'ffprobe -v quiet -print_format json -show_format -show_streams capture-000.mp4 > 1.json'

    cap = cv.VideoCapture(rtsp_stream)
    if not cap.isOpened():
        print('can`t open file')
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print('can`t receive frame. Exiting ...')
        cv.imshow('video', frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

    """img = cv.imread('1.jpg', 0)

    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()"""

    """vcap = cv.VideoCapture(rtsp_stream)
    while True:
        ret, frame = vcap.read()
        cv.imshow('VIDEO', frame)
        cv.waitKey(1)
    vcap.release()
    vcap.destroyallwindows()"""


if __name__ == '__main__':
    main()
