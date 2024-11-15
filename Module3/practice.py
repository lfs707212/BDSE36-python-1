# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

secrect_num = 50


while True:
    num = int(input("請輸入數字1-100:"))
    if num > secrect_num:
        print("猜錯了,數字比較大")
        
    elif num < secrect_num:
        print("猜錯了,數字比較小")
        
    else:
        print("數字正確")
        break








