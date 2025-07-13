#!/usr/bin/env python3

import sys

def calculate_tax(price, tax_rate):
    """消費税込み価格を計算"""
    try:
        price = float(price)
        tax_rate = float(tax_rate)
        
        if price < 0:
            return "エラー: 価格は0以上である必要があります"
        if tax_rate < 0:
            return "エラー: 税率は0以上である必要があります"
        
        tax_amount = price * (tax_rate / 100)
        total_price = price + tax_amount
        
        return {
            "price": price,
            "tax_rate": tax_rate,
            "tax_amount": tax_amount,
            "total_price": total_price
        }
    except ValueError:
        return "エラー: 無効な数値です"

def main():
    if len(sys.argv) == 3:
        price, tax_rate = sys.argv[1], sys.argv[2]
        result = calculate_tax(price, tax_rate)
        
        if isinstance(result, dict):
            print(f"本体価格: ¥{result['price']:,.0f}")
            print(f"税率: {result['tax_rate']}%")
            print(f"消費税額: ¥{result['tax_amount']:,.0f}")
            print(f"税込価格: ¥{result['total_price']:,.0f}")
        else:
            print(result)
    else:
        print("💰 消費税計算機")
        print("使い方: python main.py <価格> <税率>")
        print("例: python main.py 1000 10")
        print()
        
        # インタラクティブモード
        while True:
            try:
                price_input = input("本体価格を入力してください (または 'q' で終了): ").strip()
                if price_input.lower() == 'q':
                    break
                
                tax_rate_input = input("税率(%)を入力してください (デフォルト: 10): ").strip()
                if not tax_rate_input:
                    tax_rate_input = "10"
                
                result = calculate_tax(price_input, tax_rate_input)
                
                if isinstance(result, dict):
                    print()
                    print("=" * 30)
                    print(f"本体価格: ¥{result['price']:,.0f}")
                    print(f"税率: {result['tax_rate']}%")
                    print(f"消費税額: ¥{result['tax_amount']:,.0f}")
                    print(f"税込価格: ¥{result['total_price']:,.0f}")
                    print("=" * 30)
                    print()
                else:
                    print(f"エラー: {result}")
                    print()
                
            except KeyboardInterrupt:
                print("\n終了します。")
                break
            except EOFError:
                break

if __name__ == "__main__":
    main()