# from flask import Flask, render_template, Response
# import cv2
# from ultralytics import YOLO

# app = Flask(__name__)

# # Load YOLO model
# src = 'best2.pt'
# model = YOLO(src)

# # Open video file
# video_path = 'cam.mp4'
# cap = cv2.VideoCapture(video_path)

# def detect_fruits():
#     frame_count = 0
#     so_luong_tao = 0
#     so_luong_chuoi = 0
#     so_luong_nho = 0
#     so_luong_cam = 0
#     so_luong_khom = 0
#     so_luong_duahau= 0
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         results = model(frame)

#         frame_count += 1  # Increment frame count

#         for result in results:
#             for box in result.boxes.data:
#                 xmin, ymin, xmax, ymax = map(int, box[:4])

#                 if box[5] == 0:
#                     so_luong_tao += 1
#                     label = f"Táo: {box[4] * 100:.2f}%"
#                     color = (72, 72, 208)
#                 elif box[5] == 1:
#                     so_luong_chuoi += 1
                    
#                     label = f"Chuối: {box[4] * 100:.2f}%"
#                     color = (74, 201, 255)
#                 elif box[5] == 2:
#                     so_luong_nho += 1
                    
#                     label = f"Nho: {box[4] * 100:.2f}%"
#                     color = (156, 70, 134)
#                 elif box[5] == 3:
#                     so_luong_cam += 1
                    
#                     label = f"Cam: {box[4] * 100:.2f}%"
#                     color = (0, 152, 255)
#                 elif box[5] == 4:
#                     so_luong_khom +=1
                    
#                     label = f"Khóm: {box[4] * 100:.2f}%"
#                     color = (67, 152, 255)
#                 elif box[5] == 5:
#                     so_luong_duahau += 1
                    
#                     label = f"Dưa Hấu: {box[4] * 100:.2f}%"
#                     color = (85, 38, 175)

#                 cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
#                 cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n' +
#                b'apple: ' + str(so_luong_tao).encode() + b'\r\n' +
#                b'banana: ' + str(so_luong_chuoi).encode() + b'\r\n' +
#                b'grape: ' + str(so_luong_nho).encode() + b'\r\n' +
#                b'orange: ' + str(so_luong_cam).encode() + b'\r\n' +
#                b'pineapple: ' + str(so_luong_khom).encode() + b'\r\n' +
#                b'Watermelon: ' + str(so_luong_duahau).encode() + b'\r\n')
        

               
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(detect_fruits(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, Response
# import cv2
# from ultralytics import YOLO

# app = Flask(__name__)

# # Load YOLO model
# src = 'best2.pt'
# model = YOLO(src)

# # Open video file
# video_path = 'cam.mp4'
# cap = cv2.VideoCapture(video_path)

# def detect_fruits():
#     so_luong_tao = 0
#     so_luong_chuoi = 0
#     so_luong_nho = 0
#     so_luong_cam = 0
#     so_luong_khom = 0
#     so_luong_duahau= 0
#     frame_count = 0
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         results = model(frame)

#         frame_count += 1  # Tăng số lượng frame

#         for result in results:
#             for box in result.boxes.data:
#                 xmin, ymin, xmax, ymax = map(int, box[:4])

#                 if box[5] == 0:
#                     so_luong_tao += 1
#                     label = f"Táo: {box[4] * 100:.2f}%"
#                     color = (72, 72, 208)
#                 elif box[5] == 1:
#                     so_luong_chuoi += 1
                    
#                     label = f"Chuối: {box[4] * 100:.2f}%"
#                     color = (74, 201, 255)
#                 elif box[5] == 2:
#                     so_luong_nho += 1
                    
#                     label = f"Nho: {box[4] * 100:.2f}%"
#                     color = (156, 70, 134)
#                 elif box[5] == 3:
#                     so_luong_cam += 1
                    
#                     label = f"Cam: {box[4] * 100:.2f}%"
#                     color = (0, 152, 255)
#                 elif box[5] == 4:
#                     so_luong_khom += 1
                    
#                     label = f"Khóm: {box[4] * 100:.2f}%"
#                     color = (67, 152, 255)
#                 elif box[5] == 5:
#                     so_luong_duahau += 1
                    
#                     label = f"Dưa Hấu: {box[4] * 100:.2f}%"
#                     color = (85, 38, 175)

#                 cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
#                 cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
#                )
               
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(detect_fruits(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, Response, request, redirect, session, url_for
# import cv2
# import os
# import requests
# from ultralytics import YOLO

# app = Flask(__name__)
# app.secret_key = 'dgdfgfdhghtryeqfhghghtyui'
# # Khởi tạo đối tượng YOLO
# src = 'best2.pt'
# model = YOLO(src)

# # Biến global để lưu đường dẫn của video
# video_path = None
# cap = None
# so_luong_cam = 0
# frame_count = 0
# # Hàm xử lý phát hiện trái cây
# def detect_fruits():
#     global cap, so_luong_cam, frame_count
#     if video_path is None:
#         return

#     if cap is None:
#         cap = cv2.VideoCapture(video_path)
   
    
#     so_luong_tao = 0
#     so_luong_chuoi = 0
#     so_luong_nho = 0
#     # so_luong_cam = 0
#     so_luong_khom = 0
#     so_luong_duahau = 0
    
    
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         results = model(frame)

#         frame_count += 1

#         for result in results:
#             for box in result.boxes.data:
#                 xmin, ymin, xmax, ymax = map(int, box[:4])

#                 if box[5] == 0:
#                     so_luong_tao += 1
#                     label = f"Táo: {box[4] * 100:.2f}%"
#                     color = (72, 72, 208)
#                 elif box[5] == 1:
#                     so_luong_chuoi += 1
#                     label = f"Chuối: {box[4] * 100:.2f}%"
#                     color = (74, 201, 255)
#                 elif box[5] == 2:
#                     so_luong_nho += 1
#                     label = f"Nho: {box[4] * 100:.2f}%"
#                     color = (156, 70, 134)
#                 elif box[5] == 3:
#                     so_luong_cam += 1
#                     label = f"Cam: {box[4] * 100:.2f}%"
#                     color = (0, 152, 255)
                    
#                 elif box[5] == 4:
#                     so_luong_khom += 1
#                     label = f"Khóm: {box[4] * 100:.2f}%"
#                     color = (67, 152, 255)
#                 elif box[5] == 5:
#                     so_luong_duahau += 1
#                     label = f"Dưa Hấu: {box[4] * 100:.2f}%"
#                     color = (85, 38, 175)

#                 cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
#                 cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
        
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#     return so_luong_cam, frame_count

# # Route cho trang chính
# @app.route('/')
# def index():
#     if frame_count == 0:
#         return render_template('index.html', so_luong_cam=so_luong_cam)
#     return render_template('index.html', so_luong_cam=round(so_luong_cam/frame_count))



# # Route cho video feed
# @app.route('/video_feed')
# def video_feed():
#     return Response(detect_fruits(), mimetype='multipart/x-mixed-replace; boundary=frame')


# # Route cho upload video
# @app.route('/upload', methods=['POST'])
# def upload_video():
#     global video_path, so_luong_cam
#     if 'video' not in request.files:
#         return redirect(request.url)
#     file = request.files['video']
#     if file.filename == '':
#         return redirect(request.url)
#     if file:
#         # Lưu video vào thư mục hiện tại hoặc thư mục bạn chọn
#         video_path = 'uploaded_video.mp4'
#         file.save(video_path)
#         so_luong_cam = 0
#         return redirect(url_for('index'))
# @app.route('/cancel', methods=['POST'])
# def cancel_upload():
#     global video_path, cap, so_luong_cam 
#     if cap is not None:
#         if cap.isOpened():
#             cap.release()
#         cap = None
#     if video_path:
#         os.remove(video_path)
#         video_path = None
#         so_luong_cam = 0
#     return redirect(url_for('index'))
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, Response, request, redirect, jsonify, url_for
import cv2
import os
from numpy import mean
from ultralytics import YOLO

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Khởi tạo đối tượng YOLO
src = 'best2.pt'
model = YOLO(src)

# Biến global để lưu đường dẫn của video
video_path = None
cap = None
check = False
frame_count = 0
#cam
so_luong_cam = 0
so_luong_cam_frame = 0
so_luong_cam_frame_array = []

#táo
so_luong_tao = 0
so_luong_tao_frame = 0
so_luong_tao_frame_array = []

#Chuối
so_luong_chuoi = 0
so_luong_chuoi_frame = 0
so_luong_chuoi_frame_array = []

#nho
so_luong_nho = 0
so_luong_nho_frame = 0
so_luong_nho_frame_array = []

#khớm
so_luong_khom = 0
so_luong_khom_frame = 0
so_luong_khom_frame_array = []

#duahau
so_luong_duahau = 0
so_luong_duahau_frame = 0
so_luong_duahau_frame_array = []

# Hàm xử lý phát hiện trái cây
def detect_fruits():
    global cap, so_luong_cam, frame_count, so_luong_cam_frame, so_luong_cam_frame_array,check, so_luong_tao, so_luong_tao_frame, so_luong_tao_frame_array, \
        so_luong_chuoi, so_luong_chuoi_frame, so_luong_chuoi_frame_array, \
        so_luong_nho, so_luong_nho_frame, so_luong_nho_frame_array, \
        so_luong_khom, so_luong_khom_frame, so_luong_khom_frame_array, \
        so_luong_duahau, so_luong_duahau_frame, so_luong_duahau_frame_array

    if video_path is None:
        return

    if cap is None:
        cap = cv2.VideoCapture(video_path)
   
    
    #so_luong_tao = 0
    #so_luong_chuoi = 0
   # so_luong_nho = 0
    # so_luong_cam = 0
    #so_luong_khom = 0
    #so_luong_duahau = 0
    
    
    while True:
        ret, frame = cap.read()
        if not ret:
            check = True
            break
        
        results = model(frame)

        so_luong_cam_frame = 0 #cam
        so_luong_tao_frame = 0 #táo
        so_luong_chuoi_frame = 0 #chuối
        so_luong_nho_frame = 0 #nho
        so_luong_khom_frame = 0 #khớm
        so_luong_duahau_frame = 0 #duahau
        frame_count += 1
        for result in results:
            for box in result.boxes.data:
                xmin, ymin, xmax, ymax = map(int, box[:4])
                
                if box[5] == 0:
                    so_luong_tao += 1
                    so_luong_tao_frame += 1
                    so_luong_tao_frame_array.append(so_luong_tao_frame) #táo
                    
                    label = f"Táo: {box[4] * 100:.2f}%"
                    color = (72, 72, 208)
                elif box[5] == 1:
                    so_luong_chuoi += 1
                    so_luong_chuoi_frame += 1
                    so_luong_chuoi_frame_array.append(so_luong_chuoi_frame) #chuối
                    
                    label = f"Chuối: {box[4] * 100:.2f}%"
                    color = (74, 201, 255)
                elif box[5] == 2:
                    so_luong_nho += 1
                    so_luong_nho_frame += 1
                    so_luong_nho_frame_array.append(so_luong_nho_frame) #nho
                    
                    label = f"Nho: {box[4] * 100:.2f}%"
                    color = (156, 70, 134)
                elif box[5] == 3:
                    so_luong_cam += 1
                    so_luong_cam_frame += 1
                    so_luong_cam_frame_array.append(so_luong_cam_frame) #cam
                    
                    label = f"Cam: {box[4] * 100:.2f}%"
                    color = (0, 152, 255)
                    
                elif box[5] == 4:
                    so_luong_khom += 1
                    so_luong_khom_frame += 1
                    so_luong_khom_frame_array.append(so_luong_khom_frame) #khớm
                    
                    label = f"Khóm: {box[4] * 100:.2f}%"
                    color = (67, 152, 255)
                elif box[5] == 5:
                    so_luong_duahau += 1
                    so_luong_duahau_frame += 1
                    so_luong_duahau_frame_array.append(so_luong_duahau_frame) #duahau
                    
                    label = f"Dưa Hấu: {box[4] * 100:.2f}%"
                    color = (85, 38, 175)

                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
                cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return so_luong_cam, frame_count, check, so_luong_tao, so_luong_chuoi, so_luong_nho, so_luong_khom, so_luong_duahau, so_luong_tao_frame_array, so_luong_chuoi_frame_array, so_luong_nho_frame_array, so_luong_cam_frame_array, so_luong_khom_frame_array, so_luong_duahau_frame_array
# Route cho trang chính
@app.route('/')
def index():
    global so_luong_cam, so_luong_tao
    
    return render_template('index.html',so_luong_cam=so_luong_cam, so_luong_cam_frame=so_luong_cam_frame, so_luong_tao=so_luong_tao, so_luong_tao_frame=so_luong_tao_frame, 
                        so_luong_chuoi=so_luong_chuoi, so_luong_chuoi_frame=so_luong_chuoi_frame, so_luong_nho=so_luong_nho, so_luong_nho_frame=so_luong_nho_frame,
                        so_luong_khom=so_luong_khom, so_luong_khom_frame=so_luong_khom_frame, so_luong_duahau=so_luong_duahau, so_luong_duahau_frame=so_luong_duahau_frame, frame_count=frame_count)

# Route cho video feed
@app.route('/video_feed')
def video_feed():
    return Response(detect_fruits(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route cho API trả về số lượng cam
@app.route('/count')
def count():
    global  so_luong_cam, frame_count, so_luong_cam_frame, so_luong_cam_frame_array, check, so_luong_tao, so_luong_tao_frame, so_luong_tao_frame_array, \
        so_luong_chuoi, so_luong_chuoi_frame, so_luong_chuoi_frame_array, \
        so_luong_nho, so_luong_nho_frame, so_luong_nho_frame_array, \
        so_luong_khom, so_luong_khom_frame, so_luong_khom_frame_array, \
        so_luong_duahau, so_luong_duahau_frame, so_luong_duahau_frame_array
    
    if(so_luong_tao_frame_array == []):
        so_luong_tao_frame_array.append(0)
        
    if(so_luong_chuoi_frame_array == []):
        so_luong_chuoi_frame_array.append(0)
        
    if(so_luong_nho_frame_array == []):
        so_luong_nho_frame_array.append(0)
        
    if(so_luong_cam_frame_array == []):
        so_luong_cam_frame_array.append(0)
        
    if(so_luong_khom_frame_array == []):
        so_luong_khom_frame_array.append(0)
        
    if(so_luong_duahau_frame_array == []):
        so_luong_duahau_frame_array.append(0)
    
    return jsonify(
        {   
            'check': check,
            'frame_count':frame_count,
            #cam
            'max_cam': max(so_luong_cam_frame_array),
            'so_luong_cam': round(mean(so_luong_cam_frame_array),2),
            'so_luong_cam_frame': so_luong_cam_frame,
            
            #táo
            'max_tao': max(so_luong_tao_frame_array),
            'so_luong_tao': round(mean(so_luong_tao_frame_array),2),
            'so_luong_tao_frame': so_luong_tao_frame,

            #chuối
            'max_chuoi': max(so_luong_chuoi_frame_array),
            'so_luong_chuoi': round(mean(so_luong_chuoi_frame_array),2),
            'so_luong_chuoi_frame': so_luong_chuoi_frame,

            #nho
            'max_nho': max(so_luong_nho_frame_array),
            'so_luong_nho': round(mean(so_luong_nho_frame_array),2),
            'so_luong_nho_frame': so_luong_nho_frame,

            #khớm
            'max_khom': max(so_luong_khom_frame_array),
            'so_luong_khom': round(mean(so_luong_khom_frame_array),2),
            'so_luong_khom_frame': so_luong_khom_frame,
            
            #duahau
            'max_duahau': max(so_luong_duahau_frame_array),
            'so_luong_duahau': round(mean(so_luong_duahau_frame_array),2),
            'so_luong_duahau_frame' :so_luong_duahau_frame
          
        }
    )

# Route cho upload video
@app.route('/upload', methods=['POST'])
def upload_video():
    global video_path, so_luong_cam, cap,so_luong_cam_frame, frame_count, so_luong_cam_frame_array, check, so_luong_tao, so_luong_tao_frame, so_luong_tao_frame_array, \
        so_luong_chuoi, so_luong_chuoi_frame, so_luong_chuoi_frame_array, \
        so_luong_nho, so_luong_nho_frame, so_luong_nho_frame_array, \
        so_luong_khom, so_luong_khom_frame, so_luong_khom_frame_array, \
        so_luong_duahau, so_luong_duahau_frame, so_luong_duahau_frame_array

    if 'video' not in request.files:
        return redirect(request.url)
    file = request.files['video']
    if file.filename == '':
        return redirect(request.url)
    if file:
        # Lưu video vào thư mục hiện tại hoặc thư mục bạn chọn
        video_path = 'uploaded_video.mp4'
        file.save(video_path)
        frame_count = 0
        #cam
        so_luong_cam = 0
        so_luong_cam_frame = 0
        so_luong_cam_frame_array = []

        #táo
        so_luong_tao = 0
      
        so_luong_tao_frame = 0
        so_luong_tao_frame_array = []

        #chuối
        so_luong_chuoi = 0
       
        so_luong_chuoi_frame = 0
        so_luong_chuoi_frame_array = []

        #nho
        so_luong_nho = 0
       
        so_luong_nho_frame = 0
        so_luong_nho_frame_array = []

        #khớm  
        so_luong_khom = 0
       
        so_luong_khom_frame = 0
        so_luong_khom_frame_array = []
        
        #duahau
        so_luong_duahau = 0
     
        so_luong_duahau_frame = 0
        so_luong_duahau_frame_array = []
      
        cap = None
        check = False
        return redirect(url_for('index'))

@app.route('/cancel', methods=['POST'])
def cancel_upload():
    global video_path, cap, so_luong_cam, so_luong_cam_frame, frame_count, so_luong_cam_frame_array,check, so_luong_tao, so_luong_tao_frame, so_luong_tao_frame_array, \
        so_luong_chuoi, so_luong_chuoi_frame, so_luong_chuoi_frame_array, \
        so_luong_nho, so_luong_nho_frame, so_luong_nho_frame_array, \
        so_luong_khom, so_luong_khom_frame, so_luong_khom_frame_array, \
        so_luong_duahau, so_luong_duahau_frame, so_luong_duahau_frame_array
    if cap is not None:
        if cap.isOpened():
            cap.release()
        cap = None
    if video_path:
        os.remove(video_path)
        video_path = None
        check = False
        frame_count = 0
        #cam
        so_luong_cam = 0
        so_luong_cam_frame = 0
        so_luong_cam_frame_array = []

        #táo
        so_luong_tao = 0
        so_luong_tao_frame = 0
        so_luong_tao_frame_array = []

        #chuối
        so_luong_chuoi = 0
        so_luong_chuoi_frame = 0
        so_luong_chuoi_frame_array = []

        #nho
        so_luong_nho = 0
        so_luong_nho_frame = 0
        so_luong_nho_frame_array = []

        #khớm
        so_luong_khom = 0
        so_luong_khom_frame = 0
        so_luong_khom_frame_array = []

        #duahau
        so_luong_duahau = 0
        so_luong_duahau_frame = 0
        so_luong_duahau_frame_array = []
      
    return redirect(url_for('index'))
       
if __name__ == '__main__':
    app.run(debug=True)
