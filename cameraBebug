import cv2

def list_available_cameras():
    """
    利用可能なカメラデバイスのIDを列挙して表示する関数
    """
    available_cameras = []
    # 試行するIDの最大値や、連続失敗回数の閾値を設定
    max_id_to_try = 10  # 例えばID 0から9までを試す
    consecutive_failures = 0
    failure_threshold = 5 # 連続で5回失敗したら探索を終了

    print("利用可能なカメラデバイスIDを探索中...")

    for i in range(max_id_to_try):
        cap = cv2.VideoCapture(i)

        if cap.isOpened():
            # カメラが正常に開けたら、利用可能としてリストに追加
            print(f"ID {i}: 利用可能です。")
            available_cameras.append(i)
            consecutive_failures = 0 # 成功したので失敗カウンタをリセット
            cap.release() # 開いたカメラはすぐに閉じる
        else:
            # カメラが開けなかった場合
            # print(f"ID {i}: 利用できませんでした。") # デバッグ用にコメント解除しても良い
            consecutive_failures += 1

            # 連続失敗回数が閾値を超えたら探索を終了
            if consecutive_failures >= failure_threshold:
                print(f"連続で {failure_threshold} 回カメラを開けませんでした。探索を終了します。")
                break

    print("\n--- 探索終了 ---")
    if available_cameras:
        print("見つかった利用可能なカメラデバイスID:", available_cameras)
    else:
        print("利用可能なカメラデバイスは見つかりませんでした。")

    return available_cameras

if __name__ == "__main__":
    list_available_cameras()
