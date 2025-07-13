#!/usr/bin/env python3

import sys

def calculate_bmi(height_cm, weight_kg):
    """BMIを計算し判定"""
    try:
        height = float(height_cm)
        weight = float(weight_kg)
        
        if height <= 0 or weight <= 0:
            return "エラー: 身長と体重は正の値である必要があります"
        
        # BMI計算（身長をmに変換）
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        
        # BMI判定
        if bmi < 18.5:
            category = "低体重"
            advice = "体重を増やすことを検討してください"
        elif bmi < 25:
            category = "普通体重"
            advice = "理想的な体重です"
        elif bmi < 30:
            category = "肥満(1度)"
            advice = "体重管理に注意しましょう"
        elif bmi < 35:
            category = "肥満(2度)"
            advice = "医師に相談することをお勧めします"
        else:
            category = "肥満(3度)"
            advice = "医師の指導のもと体重管理が必要です"
        
        # 標準体重計算
        standard_weight = 22 * (height_m ** 2)
        weight_diff = weight - standard_weight
        
        return {
            "height_cm": height,
            "weight_kg": weight,
            "bmi": bmi,
            "category": category,
            "advice": advice,
            "standard_weight": standard_weight,
            "weight_diff": weight_diff
        }
        
    except ValueError:
        return "エラー: 無効な数値です"
    except Exception as e:
        return f"エラー: {str(e)}"

def main():
    if len(sys.argv) == 3:
        height, weight = sys.argv[1], sys.argv[2]
        result = calculate_bmi(height, weight)
        
        if isinstance(result, dict):
            print(f"身長: {result['height_cm']:.1f}cm")
            print(f"体重: {result['weight_kg']:.1f}kg")
            print(f"BMI: {result['bmi']:.1f}")
            print(f"判定: {result['category']}")
            print(f"アドバイス: {result['advice']}")
            print(f"標準体重: {result['standard_weight']:.1f}kg")
            if result['weight_diff'] > 0:
                print(f"標準体重より: +{result['weight_diff']:.1f}kg")
            else:
                print(f"標準体重より: {result['weight_diff']:.1f}kg")
        else:
            print(result)
    else:
        print("⚖️ BMI計算")
        print("使い方: python main.py <身長(cm)> <体重(kg)>")
        print("例: python main.py 170 65")
        print()
        
        # インタラクティブモード
        while True:
            try:
                height_input = input("身長(cm)を入力してください (または 'q' で終了): ").strip()
                if height_input.lower() == 'q':
                    break
                
                weight_input = input("体重(kg)を入力してください: ").strip()
                
                result = calculate_bmi(height_input, weight_input)
                
                if isinstance(result, dict):
                    print()
                    print("=" * 40)
                    print(f"身長: {result['height_cm']:.1f}cm")
                    print(f"体重: {result['weight_kg']:.1f}kg")
                    print(f"BMI: {result['bmi']:.1f}")
                    print(f"判定: {result['category']}")
                    print(f"アドバイス: {result['advice']}")
                    print(f"標準体重: {result['standard_weight']:.1f}kg")
                    if result['weight_diff'] > 0:
                        print(f"標準体重より: +{result['weight_diff']:.1f}kg")
                    else:
                        print(f"標準体重より: {result['weight_diff']:.1f}kg")
                    
                    # BMIスケール表示
                    print()
                    print("BMI基準:")
                    print("18.5未満: 低体重")
                    print("18.5-25未満: 普通体重")
                    print("25-30未満: 肥満(1度)")
                    print("30-35未満: 肥満(2度)")
                    print("35以上: 肥満(3度)")
                    print("=" * 40)
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