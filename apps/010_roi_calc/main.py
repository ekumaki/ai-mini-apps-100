#!/usr/bin/env python3

import sys

def calculate_roi(initial_investment, final_value, period_years=None):
    """ROI（投資利益率）を計算"""
    try:
        initial = float(initial_investment)
        final = float(final_value)
        
        if initial <= 0:
            return "エラー: 初期投資額は正の値である必要があります"
        
        # 基本的なROI計算
        gain_loss = final - initial
        roi_percent = (gain_loss / initial) * 100
        
        result = {
            "initial_investment": initial,
            "final_value": final,
            "gain_loss": gain_loss,
            "roi_percent": roi_percent
        }
        
        # 期間が指定されている場合は年利換算も計算
        if period_years:
            try:
                period = float(period_years)
                if period > 0:
                    # 年率換算（複利）
                    annual_return = ((final / initial) ** (1 / period) - 1) * 100
                    result["period_years"] = period
                    result["annual_return"] = annual_return
                else:
                    result["period_error"] = "期間は正の値である必要があります"
            except ValueError:
                result["period_error"] = "期間は有効な数値である必要があります"
        
        return result
        
    except ValueError:
        return "エラー: 無効な数値です"
    except Exception as e:
        return f"エラー: {str(e)}"

def main():
    if len(sys.argv) >= 3:
        initial = sys.argv[1]
        final = sys.argv[2]
        period = sys.argv[3] if len(sys.argv) >= 4 else None
        
        result = calculate_roi(initial, final, period)
        
        if isinstance(result, dict):
            print(f"初期投資額: ¥{result['initial_investment']:,.0f}")
            print(f"最終価値: ¥{result['final_value']:,.0f}")
            print(f"損益: ¥{result['gain_loss']:,.0f}")
            print(f"ROI: {result['roi_percent']:.2f}%")
            
            if "annual_return" in result:
                print(f"期間: {result['period_years']}年")
                print(f"年率: {result['annual_return']:.2f}%")
            elif "period_error" in result:
                print(f"期間エラー: {result['period_error']}")
        else:
            print(result)
    else:
        print("📈 ROI（投資利益率）計算")
        print("使い方: python main.py <初期投資額> <最終価値> [期間(年)]")
        print("例: python main.py 1000000 1200000 2")
        print()
        
        # インタラクティブモード
        while True:
            try:
                initial_input = input("初期投資額(円)を入力してください (または 'q' で終了): ").strip()
                if initial_input.lower() == 'q':
                    break
                
                final_input = input("最終価値(円)を入力してください: ").strip()
                period_input = input("期間(年)を入力してください (空白で省略): ").strip()
                
                period = period_input if period_input else None
                result = calculate_roi(initial_input, final_input, period)
                
                if isinstance(result, dict):
                    print()
                    print("=" * 40)
                    print("【ROI計算結果】")
                    print(f"初期投資額: ¥{result['initial_investment']:,.0f}")
                    print(f"最終価値: ¥{result['final_value']:,.0f}")
                    
                    if result['gain_loss'] >= 0:
                        print(f"利益: ¥{result['gain_loss']:,.0f}")
                    else:
                        print(f"損失: ¥{abs(result['gain_loss']):,.0f}")
                    
                    print(f"ROI: {result['roi_percent']:.2f}%")
                    
                    if "annual_return" in result:
                        print(f"期間: {result['period_years']}年")
                        print(f"年率: {result['annual_return']:.2f}%")
                    elif "period_error" in result:
                        print(f"期間エラー: {result['period_error']}")
                    
                    # パフォーマンス評価
                    if "annual_return" in result:
                        annual_rate = result['annual_return']
                        if annual_rate > 10:
                            print("📊 評価: 優秀な投資成果")
                        elif annual_rate > 5:
                            print("📊 評価: 良好な投資成果")
                        elif annual_rate > 0:
                            print("📊 評価: プラスの投資成果")
                        else:
                            print("📊 評価: マイナスの投資成果")
                    
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