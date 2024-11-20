import tkinter as tk
from tkinter import filedialog, messagebox
from processor.file_loader import load_file
from processor.data_processor import process_data
from processor.file_saver import save_file

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("表格处理工具")
        self.setup_ui()

    def setup_ui(self):
        self.drop_area = tk.Label(self.root, text="将表格文件拖拽到此处", width=40, height=10, bg="lightgray")
        self.drop_area.pack(pady=20)

        self.select_btn = tk.Button(self.root, text="选择文件", command=self.select_file)
        self.select_btn.pack(pady=10)

    def select_file(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("CSV文件", "*.csv"), ("Excel文件", "*.xlsx")]
        )
        if filepath:
            self.process_file(filepath)

    def process_file(self, filepath):
        try:
            data = load_file(filepath)
            processed_data = process_data(data)
            output_file = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV文件", "*.csv"), ("Excel文件", "*.xlsx")],
            )
            if output_file:
                save_file(processed_data, output_file)
                messagebox.showinfo("成功", f"文件已保存到：{output_file}")
        except Exception as e:
            messagebox.showerror("错误", f"处理文件时出错：{e}")

