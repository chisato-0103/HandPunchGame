import cv2
import mediapipe as mp

# MediaPipe Handsの初期化
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# 描画用のユーティリティ初期化
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# カメラキャプチャの開始
cap = cv2.VideoCapture(1) # 0は通常内蔵カメラ

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("カメラからの映像を読み込めませんでした。")
        continue

    # MediaPipeで処理するために画像をRGBに変換
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # MediaPipeによる手の検出と追跡処理の実行
    results = hands.process(image)

    # 描画のために画像を書き込み可能に戻し、BGRに戻す
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 検出結果（ランドマーク）の描画
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            # ★ ここで hand_landmarks の情報を使って何かをする ★
            # 今はこのままでOKです。動くことを確認できたら次に進みます。

    # 結果の表示
    cv2.imshow('MediaPipe Hands', image)

    # 'q'キーを押すとループを抜ける
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 後処理
hands.close()
cap.release()
cv2.destroyAllWindows()
