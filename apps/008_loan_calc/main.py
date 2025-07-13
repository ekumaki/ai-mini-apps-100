#!/usr/bin/env python3

import sys

def calculate_loan_payment(principal, annual_rate, years):
    """ローン返済額を計算"""
    try:
        principal = float(principal)
        annual_rate = float(annual_rate)
        years = float(years)
        
        if principal <= 0 or annual_rate < 0 or years <= 0:
            return "エラー: 元本は正の値、金利は0以上、期間は正の値である必要があります"
        
        # 月利と返済回数
        monthly_rate = annual_rate / 100 / 12
        num_payments = years * 12
        
        if monthly_rate == 0:
            # 無利息の場合
            monthly_payment = principal / num_payments
        else:
            # 元利均等返済の計算
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
        
        # 総返済額と利息
        total_payment = monthly_payment * num_payments
        total_interest = total_payment - principal
        
        return {
            "principal": principal,
            "annual_rate": annual_rate,
            "years": years,
            "monthly_rate": monthly_rate * 100,
            "num_payments": int(num_payments),
            "monthly_payment": monthly_payment,
            "total_payment": total_payment,
            "total_interest": total_interest
        }
        
    except ValueError:
        return "エラー: 無効な数値です"
    except Exception as e:
        return f"エラー: {str(e)}"

def main():
    if len(sys.argv) == 4:
        principal, annual_rate, years = sys.argv[1], sys.argv[2], sys.argv[3]
        result = calculate_loan_payment(principal, annual_rate, years)
        
        if isinstance(result, dict):
            print(f"借入元本: ¥{result['principal']:,.0f}")
            print(f"年利: {result['annual_rate']}%")
            print(f"返済期間: {result['years']}年 ({result['num_payments']}回)")
            print(f"月利: {result['monthly_rate']:.3f}%")
            print(f"月々返済額: ¥{result['monthly_payment']:,.0f}")
            print(f"総返済額: ¥{result['total_payment']:,.0f}")
            print(f"利息総額: ¥{result['total_interest']:,.0f}")
        else:
            print(result)
    else:
        print("🏦 ローン返済額計算")
        print("使い方: python main.py <元本> <年利(%)> <期間(年)>")
        print("例: python main.py 3000000 2.5 30")
        print()
        
        # インタラクティブモード
        while True:
            try:
                principal_input = input("借入元本(円)を入力してください (または 'q' で終了): ").strip()
                if principal_input.lower() == 'q':
                    break
                
                rate_input = input("年利(%)を入力してください: ").strip()
                years_input = input("返済期間(年)を入力してください: ").strip()
                
                result = calculate_loan_payment(principal_input, rate_input, years_input)
                
                if isinstance(result, dict):
                    print()
                    print("=" * 50)
                    print("【ローン返済計算結果】")
                    print(f"借入元本: ¥{result['principal']:,.0f}")
                    print(f"年利: {result['annual_rate']}%")
                    print(f"返済期間: {result['years']}年 ({result['num_payments']}回)")
                    print(f"月利: {result['monthly_rate']:.3f}%")
                    print("-" * 50)
                    print(f"月々返済額: ¥{result['monthly_payment']:,.0f}")
                    print(f"総返済額: ¥{result['total_payment']:,.0f}")
                    print(f"利息総額: ¥{result['total_interest']:,.0f}")
                    print(f"利息割合: {(result['total_interest']/result['principal']*100):.1f}%")
                    print("=" * 50)
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