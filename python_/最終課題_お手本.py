import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

class SalesAnalysisApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("売上分析アプリ")
        self.geometry("800x600")
        
        # データの保持用
        self.df = None
        
        # フォント設定 (Windows/Macで日本語表示を安定させるための簡易設定)
        # 実際の授業では 'Japanize-matplotlib' の使用を推奨
        import matplotlib
        if os.name == 'nt': # Windows
            matplotlib.rc('font', family='MS Gothic')
        else: # Mac/Linux
            matplotlib.rc('font', family='AppleGothic')

        self.create_widgets()

    def create_widgets(self):
        # --- 上部コントロールエリア ---
        frame_top = ttk.Frame(self, padding=10)
        frame_top.pack(fill=tk.X)
        
        # ファイル選択ボタン
        self.btn_load = ttk.Button(frame_top, text="CSVファイルを開く", command=self.load_csv)
        self.btn_load.pack(side=tk.LEFT, padx=5)
        
        # ファイル名表示ラベル
        self.lbl_file = ttk.Label(frame_top, text="ファイル未選択")
        self.lbl_file.pack(side=tk.LEFT, padx=5)
        
        # グラフ描画ボタン
        self.btn_plot = ttk.Button(frame_top, text="グラフ表示", command=self.plot_graph, state=tk.DISABLED)
        self.btn_plot.pack(side=tk.LEFT, padx=20)

        # --- メインエリア（グラフ表示部） ---
        self.frame_graph = ttk.Frame(self, padding=10, relief="sunken")
        self.frame_graph.pack(fill=tk.BOTH, expand=True)
        
        # Matplotlibの初期化
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_graph)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def load_csv(self):
        """CSVファイルを読み込む処理"""
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        
        if file_path:
            try:
                # CSV読み込み
                self.df = pd.read_csv(file_path)
                
                # 簡単なデータチェック（授業のレベルに合わせて調整）
                if '商品名' not in self.df.columns or '売上' not in self.df.columns:
                    raise ValueError("CSVには'商品名'と'売上'列が必要です。")
                
                self.lbl_file.config(text=os.path.basename(file_path))
                self.btn_plot.config(state=tk.NORMAL)
                messagebox.showinfo("成功", "読み込みに成功しました")
                
            except Exception as e:
                messagebox.showerror("エラー", f"読み込み失敗:\n{e}")

    def plot_graph(self):
        """集計してグラフを描画する処理"""
        if self.df is None:
            return
            
        try:
            # データの集計：商品ごとの売上合計
            summary = self.df.groupby('商品名')['売上'].sum()
            
            # グラフ描画
            self.ax.clear() # 前のグラフを消す
            summary.plot(kind='bar', ax=self.ax, color='skyblue')
            
            self.ax.set_title("商品別売上合計")
            self.ax.set_xlabel("商品名")
            self.ax.set_ylabel("売上金額")
            self.fig.tight_layout()
            
            # キャンバスの更新
            self.canvas.draw()
            
        except Exception as e:
            messagebox.showerror("描画エラー", f"グラフ作成中にエラーが発生しました:\n{e}")

if __name__ == "__main__":
    app = SalesAnalysisApp()
    app.mainloop()