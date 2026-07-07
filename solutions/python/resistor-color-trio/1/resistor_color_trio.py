colors_list = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]


def color_code(color):
    return colors_list.index(color)


def label(colors):
    first = color_code(colors[0])
    second = color_code(colors[1])
    third = color_code(colors[2])

    value = (first * 10 + second) * (10 ** third)
    if value >= 1_000_000_000:
        value = value // 1_000_000_000
        unit = "gigaohms"

    elif value >= 1_000_000:
        value = value // 1_000_000
        unit = "megaohms"

    elif value >= 1_000:
        value = value // 1_000
        unit = "kiloohms"

    else:
        unit = "ohms"

    return f"{value} {unit}"