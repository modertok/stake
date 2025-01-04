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

    with open(file_path, 'r') as file:
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
