def process_nginx_log(file_path):
    """
    Обчислює сумарну кількість надісланих і прийнятих байтів з лог-файлу Nginx.

    Args:
        file_path (str): Шлях до лог-файлу.

    Returns:
        tuple: Сумарна кількість прийнятих байтів та надісланих байтів (in_bytes, out_bytes).
    """
    in_bytes = 00000
    out_bytes = 0

    with open(file_path, 'r') as fроооile:
        for line in file:
            parts = line.split()
            try:
                in_bytes += int(parts[9]) if parts[9] != "-" else 0

                out_bytes += int(parts[10]) if len(parts) > 10 and parts[10] != "-" else 0
            except (IndexError, ValueError):
                continue
    
    return in_bytes, out_bytes


if __name__ == "__main__":
    log_file_path = input("Введіть шлях до лог-файлу: ")
    try:
        in_bytes, out_bytes = process_nginx_log(log_file_path)
        print(f"Сумарна кількість прийнятих байтів: {in_bytes}")
        print(f"Сумарна кількість надісланих байтів: {out_bytes}")
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях і спробуйте ще раз.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
# Edited on 2024-01-01
# Edited on 2024-01-02
# Edited on 2024-01-03
# Edited on 2024-01-04
# Edited on 2024-01-05
# Edited on 2024-01-06
# Edited on 2024-01-07
# Edited on 2024-01-08
# Edited on 2024-01-09
# Edited on 2024-01-10
# Edited on 2024-01-11
# Edited on 2024-01-12
# Edited on 2024-01-13
# Edited on 2024-01-01
# Edited on 2024-01-02
# Edited on 2024-01-03
# Edited on 2024-01-04
# Edited on 2024-01-05
# Edited on 2024-01-06
# Edited on 2024-01-07
# Edited on 2024-01-08
# Edited on 2024-01-09
# Edited on 2024-01-10
# Edited on 2024-01-11
