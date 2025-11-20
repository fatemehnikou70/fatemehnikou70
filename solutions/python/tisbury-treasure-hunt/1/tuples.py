def get_coordinate(record):
    # record شکل: ("Gold", "A4")
    # ما باید فقط "A4" را برگردانیم
    return record[1]


def convert_coordinate(coordinate):
    # "A4" را تبدیل می‌کنیم به ('A', '4')
    # tuple("A4") → ('A', '4')
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    # آزارا مختصات را به صورت رشته دارد مثل "A4"
    # روی مختصات را به صورت ('A', '4') دارد
    # پس باید هر دو را به یک فرمت بیاوریم
    azara_coord = convert_coordinate(get_coordinate(azara_record))
    rui_coord = rui_record[1]
    return azara_coord == rui_coord


def create_record(azara_record, rui_record):
    # اگر مختصات برابر نباشد:
    if not compare_records(azara_record, rui_record):
        return "not a match"

    # اگر برابر باشند، دو رکورد را یکجا می‌کنیم
    # مثال:
    # ('Silver', 'A4') + ('Beach', ('A','4'), 'NW')
    return azara_record + rui_record


def clean_up(records):
    cleaned_records = []

    for record in records:
        # داده ورودی 5 تایی است، پس باید 5 مقدار بگیریم
        name, card_code, location, _, color = record

        # card_code مانند "2A"، "4B" و ... است و باید تبدیل شود به ('2','A')
        rank_suit = (card_code[0], card_code[1])

        # ساختار خروجی: (name, location, (rank, suit), color)
        cleaned_records.append((name, location, rank_suit, color))

    # خروجی باید رشته باشد و هر رکورد در یک خط
    return "\n".join(str(r) for r in cleaned_records) + "\n"


