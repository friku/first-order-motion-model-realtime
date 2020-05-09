import cv2
 
camera = cv2.VideoCapture(0)                               # カメラCh.(ここでは0)を指定
 
# 動画ファイル保存用の設定
fps = int(camera.get(cv2.CAP_PROP_FPS))                    # カメラのFPSを取得
w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter('video.mp4', fourcc, fps, (480, h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
 
# 撮影＝ループ中にフレームを1枚ずつ取得（qキーで撮影終了）
while True:
    ret, frame = camera.read()                             # フレームを取得
    frame = frame[:,:480,:]
    cv2.imshow('camera', frame)                            # フレームを画面に表示
    video.write(frame)                                     # 動画を1フレームずつ保存する
 
    # キー操作があればwhileループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# 撮影用オブジェクトとウィンドウの解放
camera.release()
cv2.destroyAllWindows()