import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from processMNISTdata import process_mnist_data
from mojiData import train_images, train_labels
import time

def visualize_with_tsne(X, L, n_samples=5000, perplexity=30):
    """
    t-SNEを使用してMNISTデータを2次元に削減し可視化する
    
    Parameters:
        X: 画像データ (n_samples x 784)
        L: ラベルデータ (n_samples,)
        n_samples: 使用するサンプル数
        perplexity: t-SNEのパープレキシティパラメータ
    """
    # データのサブセットを取得
    indices = np.random.permutation(X.shape[0])[:n_samples]
    X_subset = X[indices]
    L_subset = L[indices]
    
    print(f"\n{n_samples}個のサンプルでt-SNE処理を開始...")
    start_time = time.time()
    
    # データの正規化
    X_normalized = X_subset / 255.0
    
    # t-SNE実行
    tsne = TSNE(n_components=2, perplexity=perplexity, random_state=42)
    X_tsne = tsne.fit_transform(X_normalized)
    
    print(f"t-SNE処理完了 (所要時間: {time.time() - start_time:.2f}秒)")
    
    # 可視化
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], 
                         c=L_subset, cmap='tab10', 
                         alpha=0.6, s=10)
    plt.colorbar(scatter)
    plt.title('t-SNE visualization of MNIST data')
    plt.xlabel('t-SNE feature 1')
    plt.ylabel('t-SNE feature 2')
    
    # 凡例を追加
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                                 markerfacecolor=plt.cm.tab10(i/10), 
                                 label=f'Digit {i}', markersize=10)
                      for i in range(10)]
    plt.legend(handles=legend_elements, title='Digits')
    
    plt.savefig('mnist_tsne.png', dpi=300, bbox_inches='tight')
    print("\n可視化結果を'mnist_tsne.png'として保存しました")
    plt.show()

if __name__ == "__main__":
    # 必要なパッケージのインストール確認
    try:
        import sklearn
        import matplotlib
    except ImportError:
        print("必要なパッケージをインストールしています...")
        import subprocess
        subprocess.check_call(["pip", "install", "scikit-learn", "matplotlib"])
    
    # データの読み込み
    print("MNISTデータを読み込んでいます...")
    X, L = process_mnist_data(train_images, train_labels)
    
    # t-SNEによる可視化
    visualize_with_tsne(X, L, n_samples=5000, perplexity=30)
