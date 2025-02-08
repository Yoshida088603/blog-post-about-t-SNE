import kagglehub
import os
import shutil
import sys

print("Python バージョン:", sys.version)
print("作業ディレクトリ:", os.getcwd())

try:
    print("\nデータセットのダウンロードを開始...")
    path = kagglehub.dataset_download("hojjatk/mnist-dataset")
    print(f"ダウンロード成功: {path}")
    
    # ダウンロードされたファイルの確認
    files = os.listdir(path)
    print("\nダウンロードされたファイル:")
    for file in files:
        print(f"- {file}")
        print(f"  サイズ: {os.path.getsize(os.path.join(path, file))} bytes")

    # 作業ディレクトリにデータをコピー
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, "mnist_data")
    os.makedirs(data_dir, exist_ok=True)

    # ファイル名のマッピング
    file_mapping = {
        'train-images.idx3-ubyte': 'train-images-idx3-ubyte',
        'train-labels.idx1-ubyte': 'train-labels-idx1-ubyte',
        't10k-images.idx3-ubyte': 't10k-images-idx3-ubyte',
        't10k-labels.idx1-ubyte': 't10k-labels-idx1-ubyte'
    }

    # ファイルをコピー
    print("\nファイルのコピーを開始...")
    for src_name, dst_name in file_mapping.items():
        src = os.path.join(path, src_name)
        dst = os.path.join(data_dir, dst_name)
        if os.path.exists(src):
            try:
                shutil.copy2(src, dst)
                print(f"コピー成功: {src_name} -> {dst_name}")
            except Exception as e:
                print(f"コピー失敗: {src_name} -> {dst_name}")
                print(f"エラー: {str(e)}")
        else:
            print(f"ソースファイルが見つかりません: {src_name}")

    # ファイルパスの設定
    train_images = os.path.join(data_dir, "train-images-idx3-ubyte")
    train_labels = os.path.join(data_dir, "train-labels-idx1-ubyte")
    test_images = os.path.join(data_dir, "t10k-images-idx3-ubyte")
    test_labels = os.path.join(data_dir, "t10k-labels-idx1-ubyte")

    print("\nコピー後のファイル確認:")
    print(f"訓練用画像 ({os.path.exists(train_images)}): {train_images}")
    if os.path.exists(train_images):
        print(f"  サイズ: {os.path.getsize(train_images)} bytes")
    print(f"訓練用ラベル ({os.path.exists(train_labels)}): {train_labels}")
    if os.path.exists(train_labels):
        print(f"  サイズ: {os.path.getsize(train_labels)} bytes")
    print(f"テスト用画像 ({os.path.exists(test_images)}): {test_images}")
    if os.path.exists(test_images):
        print(f"  サイズ: {os.path.getsize(test_images)} bytes")
    print(f"テスト用ラベル ({os.path.exists(test_labels)}): {test_labels}")
    if os.path.exists(test_labels):
        print(f"  サイズ: {os.path.getsize(test_labels)} bytes")

except Exception as e:
    print(f"\nエラーが発生しました: {str(e)}")
    import traceback
    print(traceback.format_exc())