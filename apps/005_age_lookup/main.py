#!/usr/bin/env python3

import sys
from datetime import datetime, date

def calculate_age(birth_date_str, reference_date_str=None):
    """年齢を計算"""
    try:
        # 生年月日をパース
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        
        # 基準日を設定（指定がなければ今日）
        if reference_date_str:
            reference_date = datetime.strptime(reference_date_str, "%Y-%m-%d").date()
        else:
            reference_date = date.today()
        
        # 年齢計算
        age = reference_date.year - birth_date.year
        
        # 誕生日が来ていない場合は1歳引く
        if (reference_date.month, reference_date.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        # 詳細情報
        total_days = (reference_date - birth_date).days
        years = age
        months = reference_date.month - birth_date.month
        if months < 0:
            months += 12
        
        return {
            "birth_date": birth_date,
            "reference_date": reference_date,
            "age_years": years,
            "age_months": months,
            "total_days": total_days
        }
        
    except ValueError as e:
        return f"エラー: 日付形式が正しくありません (YYYY-MM-DD形式で入力してください)"
    except Exception as e:
        return f"エラー: {str(e)}"

def main():
    if len(sys.argv) >= 2:
        birth_date = sys.argv[1]
        reference_date = sys.argv[2] if len(sys.argv) >= 3 else None
        
        result = calculate_age(birth_date, reference_date)
        
        if isinstance(result, dict):
            print(f"生年月日: {result['birth_date']}")
            print(f"基準日: {result['reference_date']}")
            print(f"年齢: {result['age_years']}歳{result['age_months']}ヶ月")
            print(f"生まれてから: {result['total_days']:,}日")
        else:
            print(result)
    else:
        print("📅 年齢早見")
        print("使い方: python main.py <生年月日> [基準日]")
        print("例: python main.py 1990-01-01")
        print("例: python main.py 1990-01-01 2023-12-31")
        print("日付形式: YYYY-MM-DD")
        print()
        
        # インタラクティブモード
        while True:
            try:
                birth_input = input("生年月日を入力してください (YYYY-MM-DD) または 'q' で終了: ").strip()
                if birth_input.lower() == 'q':
                    break
                
                reference_input = input("基準日を入力してください (YYYY-MM-DD, 空白で今日): ").strip()
                reference_date = reference_input if reference_input else None
                
                result = calculate_age(birth_input, reference_date)
                
                if isinstance(result, dict):
                    print()
                    print("=" * 40)
                    print(f"生年月日: {result['birth_date']}")
                    print(f"基準日: {result['reference_date']}")
                    print(f"年齢: {result['age_years']}歳{result['age_months']}ヶ月")
                    print(f"生まれてから: {result['total_days']:,}日")
                    
                    # 特別な年齢
                    age = result['age_years']
                    if age == 20:
                        print("🎉 成人年齢です！")
                    elif age == 60:
                        print("🎉 還暦です！")
                    elif age == 70:
                        print("🎉 古稀です！")
                    elif age == 80:
                        print("🎉 傘寿です！")
                    elif age == 90:
                        print("🎉 卒寿です！")
                    elif age == 100:
                        print("🎉 百寿です！")
                    
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