#!/usr/bin/env python3

import sys

def convert_interest_rate(rate, from_period, to_period):
    """金利を異なる期間で換算"""
    try:
        rate = float(rate)
        
        if rate < 0:
            return "エラー: 金利は0以上である必要があります"
        
        # 期間の定義（年を基準とした倍数）
        period_multipliers = {
            "日": 365,
            "週": 52,
            "月": 12,
            "四半期": 4,
            "半年": 2,
            "年": 1
        }
        
        if from_period not in period_multipliers or to_period not in period_multipliers:
            return f"エラー: 無効な期間です。対応期間: {list(period_multipliers.keys())}"
        
        # 年利換算
        from_multiplier = period_multipliers[from_period]
        to_multiplier = period_multipliers[to_period]
        
        # 複利計算での正確な換算
        annual_rate = ((1 + rate/100/from_multiplier) ** from_multiplier - 1) * 100
        converted_rate = ((1 + annual_rate/100) ** (1/to_multiplier) - 1) * to_multiplier * 100
        
        # 単利計算での近似
        simple_annual = rate * from_multiplier
        simple_converted = simple_annual / to_multiplier
        
        return {
            "original_rate": rate,
            "from_period": from_period,
            "to_period": to_period,
            "annual_rate": annual_rate,
            "converted_rate": converted_rate,
            "simple_annual": simple_annual,
            "simple_converted": simple_converted
        }
        
    except ValueError:
        return "エラー: 無効な数値です"
    except Exception as e:
        return f"エラー: {str(e)}"

def main():
    if len(sys.argv) == 4:
        rate, from_period, to_period = sys.argv[1], sys.argv[2], sys.argv[3]
        result = convert_interest_rate(rate, from_period, to_period)
        
        if isinstance(result, dict):
            print(f"元の金利: {result['original_rate']}% ({result['from_period']}利)")
            print(f"年利換算: {result['annual_rate']:.4f}%")
            print(f"換算後: {result['converted_rate']:.4f}% ({result['to_period']}利)")
            print()
            print("【参考: 単利計算】")
            print(f"年利換算: {result['simple_annual']:.2f}%")
            print(f"換算後: {result['simple_converted']:.4f}% ({result['to_period']}利)")
        else:
            print(result)
    else:
        print("📊 金利→年利換算")
        print("使い方: python main.py <金利> <元の期間> <変換先期間>")
        print("例: python main.py 0.1 日 年")
        print("対応期間: 日, 週, 月, 四半期, 半年, 年")
        print()
        
        # インタラクティブモード
        periods = ["日", "週", "月", "四半期", "半年", "年"]
        while True:
            try:
                rate_input = input("金利(%)を入力してください (または 'q' で終了): ").strip()
                if rate_input.lower() == 'q':
                    break
                
                print(f"対応期間: {', '.join(periods)}")
                from_period_input = input("元の期間を入力してください: ").strip()
                to_period_input = input("変換先期間を入力してください: ").strip()
                
                result = convert_interest_rate(rate_input, from_period_input, to_period_input)
                
                if isinstance(result, dict):
                    print()
                    print("=" * 50)
                    print("【金利換算結果】")
                    print(f"元の金利: {result['original_rate']}% ({result['from_period']}利)")
                    print(f"年利換算: {result['annual_rate']:.4f}%")
                    print(f"換算後: {result['converted_rate']:.4f}% ({result['to_period']}利)")
                    print()
                    print("【参考: 単利計算での近似】")
                    print(f"年利換算: {result['simple_annual']:.2f}%")
                    print(f"換算後: {result['simple_converted']:.4f}% ({result['to_period']}利)")
                    print()
                    print("※複利計算による正確な換算を上段に、単利による近似を下段に表示")
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