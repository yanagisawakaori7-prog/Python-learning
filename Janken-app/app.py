import random

# ============================
# じゃんけんのメイン関数群
# ============================

def get_player_hand():
    """ユーザーに手を入力してもらう"""
    print("あなたの手を選んでください：")
    print("0: グー, 1: チョキ, 2: パー")
    while True:
        try:
            choice = int(input("番号で入力："))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("0〜2の数字で選んでください。")
        except ValueError:
            print("数字を入力してください。")


def get_computer_hand():
    """コンピュータの手をランダムで選ぶ"""
    return random.randint(0, 2)


def judge(player, computer):
    """勝敗を判定して文字列を返す"""
    if player == computer:
        return "あいこ"
    elif (player == 0 and computer == 1) or \
         (player == 1 and computer == 2) or \
         (player == 2 and computer == 0):
        return "勝ち"
    else:
        return "負け"


def hand_to_string(num):
    """数字を手の名前に変換"""
    hands = ["グー", "チョキ", "パー"]
    return hands[num]


def show_statistics(results):
    """これまでの戦績を表示"""
    total = len(results)
    wins = results.count("勝ち")
    losses = results.count("負け")
    draws = results.count("あいこ")

    if total == 0:
        win_rate = 0
    else:
        win_rate = round(wins / total * 100, 1)

    print("\n--- 現在の戦績 ---")
    print(f"試合数：{total}")
    print(f"勝ち：{wins} / 負け：{losses} / あいこ：{draws}")
    print(f"勝率：{win_rate}%")
    print("-------------------\n")


# ============================
# メインの流れ
# ============================

def main():
    print("=== じゃんけんアナライザーへようこそ！ ===")
    results = []

    while True:
        player = get_player_hand()
        computer = get_computer_hand()

        result = judge(player, computer)
        results.append(result)

        print(f"\nあなた：{hand_to_string(player)}")
        print(f"コンピュータ：{hand_to_string(computer)}")
        print(f"結果：{result}\n")

        show_statistics(results)

        again = input("もう一度やりますか？ (y/n)：")
        if again.lower() != "y":
            print("対戦ありがとうございました！")
            break


# ============================
# 実行
# ============================

if __name__ == "__main__":
    main()
