import re
from collections import Counter


def parse_pattern(orders_list):
    def replace_letters_and_digits(match):
        if match.group().isalpha():
            return '{L}' * len(match.group())
        elif match.group().isdigit():
            return '{D}' * len(match.group())

    parsed_list = []
    pattern = r'([A-Za-z]+|[0-9]+)'

    for order in orders_list:
        result = re.sub(pattern, replace_letters_and_digits, order)
        parsed_list.append(result)

    return parsed_list


def analyze_patterns(parsed_list):
    counter = Counter(parsed_list)
    analysis = [(pattern, count, sum(char == '{L}' or char == '{D}' for char in pattern)) for pattern, count in
                counter.items()]
    sorted_analysis = sorted(analysis, key=lambda x: (-x[1], x[2]))
    return sorted_analysis


def generate_report(analysis, original_orders):
    report_lines = ["Отчет об анализе шаблонов заказов"]
    report_lines.append("=" * 30)
    report_lines.append(f"Обработано заказов: {len(original_orders)}")
    report_lines.append(f"Найдено уникальных шаблонов: {len(analysis)}")
    report_lines.append("\nТоп шаблонов:")

    examples_map = {}
    for i, original_order in enumerate(original_orders):
        example_pattern = parse_pattern([original_order])[0]
        if example_pattern not in examples_map:
            examples_map[example_pattern] = original_order

    index = 1
    for pattern, count, complexity in analysis:
        report_lines.append(f"{index}. Пример: '{examples_map[pattern]}'")
        report_lines.append(f"   Шаблон:  {pattern}")
        report_lines.append(f"   Встречается: {count} раз(а)")
        report_lines.append(f"   Сложность: {complexity}\n")
        index += 1

    report_lines.append("Примечание: {L} - буквы, {D} - цифры")
    return "\n".join(report_lines)


# Тестируем полный сценарий
orders = [
    "AB-1234-XY",
    "CD-5678-ZW",
    "1234/AB/567",
    "ZZ-9999-FL"
]
parsed = parse_pattern(orders)
analysis = analyze_patterns(parsed)
report = generate_report(analysis, orders)
print(report)