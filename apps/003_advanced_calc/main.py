#!/usr/bin/env python3

import sys
import math

def calculate_advanced(expression):
    """高機能計算を実行"""
    try:
        parts = expression.split()
        
        if len(parts) == 2:
            # 単項演算（sqrt, log等）
            operator, value = parts[0], float(parts[1])
            
            if operator == "sqrt":
                if value < 0:
                    return "エラー: 負の数の平方根は計算できません"
                return math.sqrt(value)
            elif operator == "log":
                if value <= 0:
                    return "エラー: 0以下の数の対数は計算できません"
                return math.log10(value)
            elif operator == "ln":
                if value <= 0:
                    return "エラー: 0以下の数の自然対数は計算できません"
                return math.log(value)
            elif operator == "sin":
                return math.sin(math.radians(value))
            elif operator == "cos":
                return math.cos(math.radians(value))
            elif operator == "tan":
                return math.tan(math.radians(value))
            else:
                return f"エラー: 無効な単項演算子 '{operator}'"
        
        elif len(parts) == 3:
            # 二項演算
            num1_str, operator, num2_str = parts
            num1, num2 = float(num1_str), float(num2_str)
            
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                if num2 == 0:
                    return "エラー: ゼロ除算はできません"
                return num1 / num2
            elif operator == '^' or operator == '**':
                return num1 ** num2
            elif operator == '%':
                return num1 % num2
            elif operator == 'percent':
                return (num1 * num2) / 100
            else:
                return f"エラー: 無効な二項演算子 '{operator}'"
        
        else:
            return "エラー: 無効な式形式です"
            
    except ValueError:
        return "エラー: 無効な数値です"
    except Exception as e:
        return f"エラー: {str(e)}"

def main():
    if len(sys.argv) > 1:
        expression = " ".join(sys.argv[1:])
        result = calculate_advanced(expression)
        print(f"計算結果: {result}")
    else:
        print("🔢 電卓 Pro (√ % ^)")
        print("使い方:")
        print("  二項演算: python main.py <数値1> <演算子> <数値2>")
        print("  単項演算: python main.py <演算子> <数値>")
        print()
        print("対応演算子:")
        print("  基本: + - * / ^ % percent")
        print("  単項: sqrt log ln sin cos tan")
        print()
        print("例:")
        print("  python main.py 2 ^ 3     # 2の3乗")
        print("  python main.py sqrt 16   # 16の平方根")
        print("  python main.py 20 percent 50  # 50の20%")
        print()
        
        # インタラクティブモード
        while True:
            try:
                expr = input("計算式を入力してください (例: sqrt 16) または 'q' で終了: ").strip()
                if expr.lower() == 'q':
                    break
                
                if not expr:
                    continue
                
                result = calculate_advanced(expr)
                print(f"結果: {result}")
                print()
                
            except KeyboardInterrupt:
                print("\n終了します。")
                break
            except EOFError:
                break

if __name__ == "__main__":
    main()