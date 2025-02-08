import numpy as np
import struct

def process_mnist_data(image_filename, label_filename):
    """
    MNISTデータセットの画像とラベルを読み込む関数
    
    Parameters:
        image_filename (str): 画像ファイルのパス
        label_filename (str): ラベルファイルのパス
        
    Returns:
        tuple: (画像データ配列, ラベル配列)
    """
    # 画像データの読み込み
    with open(image_filename, 'rb') as f:
        # マジックナンバーの読み込み
        magic_number = struct.unpack('>i', f.read(4))[0]
        if magic_number == 2051:
            print('\nMNIST画像データを読み込んでいます...')
        
        # 画像数、行数、列数の読み込み
        num_images = struct.unpack('>i', f.read(4))[0]
        num_rows = struct.unpack('>i', f.read(4))[0]
        num_cols = struct.unpack('>i', f.read(4))[0]
        
        print(f'データセット内の画像数: {num_images} ...')
        print(f'各画像は {num_rows} x {num_cols} ピクセルです...')
        
        # 画像データの読み込みと整形
        buffer = f.read()
        X = np.frombuffer(buffer, dtype=np.uint8)
        X = X.reshape(num_images, num_rows, num_cols)
        X = X.reshape(num_images, num_rows * num_cols)
        
        print(f'画像データを {X.shape[0]} x {X.shape[1]} の行列として読み込みました...')
        print('画像データの読み込みが完了しました。')

    # ラベルデータの読み込み
    with open(label_filename, 'rb') as f:
        magic_number = struct.unpack('>i', f.read(4))[0]
        if magic_number == 2049:
            print('\nMNISTラベルデータを読み込んでいます...')
        
        num_items = struct.unpack('>i', f.read(4))[0]
        print(f'データセット内のラベル数: {num_items} ...')
        
        buffer = f.read()
        L = np.frombuffer(buffer, dtype=np.uint8)
        
        print(f'ラベルデータを {L.shape[0]} x 1 の行列として読み込みました...')
        print('ラベルデータの読み込みが完了しました。')

    return X, L

# 使用例
if __name__ == "__main__":
    # mojiData.pyからダウンロードしたファイルのパスを使用
    from mojiData import train_images as image_file
    from mojiData import train_labels as label_file
    
    X, L = process_mnist_data(image_file, label_file)
    
    # データの形状を確認
    print(f"\nデータセットの最終形状:")
    print(f"画像データ (X): {X.shape}")
    print(f"ラベルデータ (L): {L.shape}")
