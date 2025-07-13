#!/usr/bin/env python3

import sys

def calculate(num1, operator, num2):
    """四則演算を実行"""
    try:
        n1, n2 = float(num1), float(num2)
        
        if operator == '+':
            return n1 + n2
        elif operator == '-':
            return n1 - n2
        elif operator == '*':
            return n1 * n2
        elif operator == '/':
            if n2 == 0:
                return "エラー: ゼロ除算はできません"
            return n1 / n2
        else:
            return "エラー: 無効な演算子です (+, -, *, / のみ対応)"
    except ValueError:
        return "エラー: 無効な数値です"

def main():
    if len(sys.argv) == 4:
        num1, operator, num2 = sys.argv[1], sys.argv[2], sys.argv[3]
        result = calculate(num1, operator, num2)
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("📱 4則電卓")
        print("使い方: python main.py <数値1> <演算子> <数値2>")
        print("例: python main.py 10 + 5")
        print("対応演算子: + - * /")
        print()
        
        # インタラクティブモード
        while True:
            try:
                expr = input("計算式を入力してください (例: 10 + 5) または 'q' で終了: ").strip()
                if expr.lower() == 'q':
                    break
                
                parts = expr.split()
                if len(parts) != 3:
                    print("形式: 数値1 演算子 数値2")
                    continue
                
                result = calculate(parts[0], parts[1], parts[2])
                print(f"結果: {result}")
                print()
                
            except KeyboardInterrupt:
                print("\n終了します。")
                break
            except EOFError:
                break

if __name__ == "__main__":
    main()