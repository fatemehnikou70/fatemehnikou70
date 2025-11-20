def annotate(garden):
    if not garden:
        return []

    # همه‌ی ردیف‌ها باید طول یکسان داشته باشند
    if any(len(row) != len(garden[0]) for row in garden):
        raise ValueError("The board is invalid with current input.")

    # فقط کاراکترهای معتبر: space و *
    if any(ch not in " *" for row in garden for ch in row):
        raise ValueError("The board is invalid with current input.")

    rows, cols = len(garden), len(garden[0])

    def count(r, c):
        return sum(
            0 <= r+dr < rows and 0 <= c+dc < cols and garden[r+dr][c+dc] == "*"
            for dr in (-1, 0, 1) for dc in (-1, 0, 1)
            if (dr, dc) != (0, 0)
        )

    return [
        "".join(
            "*" if garden[r][c] == "*" else (str(n) if (n := count(r, c)) else " ")
            for c in range(cols)
        )
        for r in range(rows)
    ]
