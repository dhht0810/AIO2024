def levenshtein_distance(s1, s2):
    # Tạo ma trận với kích thước (len(s1)+1) x (len(s2)+1)
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Khởi tạo hàng đầu tiên và cột đầu tiên của ma trận
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Tính toán các giá trị trong ma trận dựa trên các thao tác chỉnh sửa
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i]
                                   [j - 1], dp[i - 1][j - 1])

    # Giá trị ở ô cuối cùng của ma trận là khoảng cách Levenshtein giữa s1 và s2
    return dp[m][n]


# Ví dụ sử dụng
s1 = "hola"
s2 = "hello"
print(f"Khoảng cách Levenshtein giữa '{s1}' và '{
      s2}' là: {levenshtein_distance(s1, s2)}")
