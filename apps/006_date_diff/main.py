#!/usr/bin/env python3

import sys
from datetime import datetime, timedelta

def calculate_date_diff(date1_str, date2_str):
    """日付差分を計算"""
    try:
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
        
        # 差分計算
        diff = abs(date2 - date1)
        days = diff.days
        
        # より小さい日付と大きい日付を決定
        earlier = min(date1, date2)
        later = max(date1, date2)
        
        # 年月日での差分計算
        years = later.year - earlier.year
        months = later.month - earlier.month
        day_diff = later.day - earlier.day
        
        if day_diff < 0:
            months -= 1
            # 前月の日数を取得
            if later.month == 1:
                prev_month_days = 31
            else:
                prev_month = datetime(later.year, later.month - 1, 1)
                next_month = datetime(later.year, later.month, 1)
                prev_month_days = (next_month - prev_month).days
            day_diff += prev_month_days
        
        if months < 0:
            years -= 1
            months += 12
        
        # 週数とその他の情報
        weeks = days // 7
        remaining_days = days % 7
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        
        return {
            "date1": date1.date(),
            "date2": date2.date(),
            "earlier": earlier.date(),
            "later": later.date(),
            "total_days": days,
            "years": years,
            "months": months,
            "days": day_diff,
            "weeks": weeks,
            "remaining_days": remaining_days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }
        
    except ValueError:
        return "エラー: 日付形式が正しくありません (YYYY-MM-DD形式で入力してください)"
    except Exception as e:
        return f"エラー: {str(e)}"

def main():
    if len(sys.argv) == 3:
        date1, date2 = sys.argv[1], sys.argv[2]
        result = calculate_date_diff(date1, date2)
        
        if isinstance(result, dict):
            print(f"開始日: {result['earlier']}")
            print(f"終了日: {result['later']}")
            print(f"期間: {result['years']}年{result['months']}ヶ月{result['days']}日")
            print(f"総日数: {result['total_days']:,}日")
            print(f"週数: {result['weeks']}週{result['remaining_days']}日")
            print(f"時間: {result['hours']:,}時間")
            print(f"分: {result['minutes']:,}分")
            print(f"秒: {result['seconds']:,}秒")
        else:
            print(result)
    else:
        print("📆 日付差分計算")
        print("使い方: python main.py <日付1> <日付2>")
        print("例: python main.py 2020-01-01 2023-12-31")
        print("日付形式: YYYY-MM-DD")
        print()
        
        # インタラクティブモード
        while True:
            try:
                date1_input = input("1つ目の日付を入力してください (YYYY-MM-DD) または 'q' で終了: ").strip()
                if date1_input.lower() == 'q':
                    break
                
                date2_input = input("2つ目の日付を入力してください (YYYY-MM-DD): ").strip()
                
                result = calculate_date_diff(date1_input, date2_input)
                
                if isinstance(result, dict):
                    print()
                    print("=" * 50)
                    print(f"開始日: {result['earlier']}")
                    print(f"終了日: {result['later']}")
                    print(f"期間: {result['years']}年{result['months']}ヶ月{result['days']}日")
                    print(f"総日数: {result['total_days']:,}日")
                    print(f"週数: {result['weeks']}週{result['remaining_days']}日")
                    print(f"時間: {result['hours']:,}時間")
                    print(f"分: {result['minutes']:,}分")
                    print(f"秒: {result['seconds']:,}秒")
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