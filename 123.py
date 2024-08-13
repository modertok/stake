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
# Edited on 2024-01-10v
# Edited on 2024-01-11
# Edited on 2024-01-12
# Edited on 2024-01-13
# Edited on 2024-01-14
# Edited on 2024-01-15
# Edited on 2024-01-16
# Edited on 2024-01-17
# Commit 1 on 2024-01-01
# Commit 2 on 2024-01-01
# Commit 1 on 2024-01-02
# Commit 2 on 2024-01-02
# Commit 1 on 2024-01-03
# Commit 2 on 2024-01-03
# Commit 1 on 2024-01-04
# Commit 2 on 2024-01-04
# Commit 1 on 2024-01-05
# Commit 2 on 2024-01-05
# Commit 1 on 2024-01-06
# Commit 2 on 2024-01-06
# Commit 1 on 2024-01-07
# Commit 2 on 2024-01-07
# Commit 1 on 2024-01-08
# Commit 2 on 2024-01-08
# Commit 1 on 2024-01-09
# Commit 2 on 2024-01-09
# Commit 1 on 2024-01-10
# Commit 2 on 2024-01-10
# Commit 1 on 2024-01-11
# Commit 2 on 2024-01-11
# Commit 1 on 2024-01-12
# Commit 2 on 2024-01-12
# Commit 1 on 2024-01-01
# Commit 2 on 2024-01-01
# Commit 1 on 2024-01-02
# Commit 2 on 2024-01-02
# Commit 1 on 2024-01-03
# Commit 2 on 2024-01-03
# Commit 1 on 2024-01-04
# Commit 1 on 2024-01-01
# Commit 2 on 2024-01-01
# Commit 1 on 2024-01-01
# Commit 2 on 2024-01-01
# Commit 1 on 2024-01-02
# Commit 2 on 2024-01-02
# Commit 1 on 2024-01-03
# Commit 2 on 2024-01-03
# Commit 1 on 2024-01-04
# Commit 2 on 2024-01-04
# Commit 1 on 2024-01-05
# Commit 2 on 2024-01-05
# Commit 1 on 2024-01-06
# Commit 2 on 2024-01-06
# Commit 1 on 2024-01-07
# Commit 2 on 2024-01-07
# Commit 1 on 2024-01-08
# Commit 2 on 2024-01-08
# Commit 1 on 2024-01-09
# Commit 2 on 2024-01-09
# Commit 1 on 2024-01-10
# Commit 2 on 2024-01-10
# Commit 1 on 2024-01-11
# Commit 2 on 2024-01-11
# Commit 1 on 2024-01-12
# Commit 2 on 2024-01-12
# Commit 1 on 2024-01-13
# Commit 1 on 2024-01-01
# Commit 2 on 2024-01-01
# Commit 1 on 2024-01-02
# Commit 2 on 2024-01-02
# Commit 1 on 2024-01-03
# Commit 2 on 2024-01-03
# Commit 1 on 2024-01-04
# Commit 2 on 2024-01-04
# Commit 1 on 2024-01-05
# Commit 2 on 2024-01-05
# Commit 1 on 2024-01-06
# Commit 2 on 2024-01-06
# Commit 1 on 2024-01-07
# Commit 2 on 2024-01-07
# Commit 1 on 2024-01-08
# Commit 2 on 2024-01-08
# Commit 1 on 2024-01-09
# Commit 2 on 2024-01-09
# Commit 1 on 2024-01-10
# Commit 2 on 2024-01-10
# Commit 1 on 2024-01-11
# Commit 2 on 2024-01-11
# Commit 1 on 2024-01-12
# Commit 2 on 2024-01-12
# Commit 1 on 2024-01-13
# Commit 2 on 2024-01-13
# Commit 1 on 2024-01-14
# Commit 2 on 2024-01-14
# Commit 1 on 2024-01-15
# Commit 2 on 2024-01-15
# Commit 1 on 2024-01-16
# Commit 2 on 2024-01-16
# Commit 1 on 2024-01-17
# Commit 2 on 2024-01-17
# Commit 1 on 2024-01-18
# Commit 2 on 2024-01-18
# Commit 1 on 2024-01-19
# Commit 2 on 2024-01-19
# Commit 1 on 2024-01-20
# Commit 2 on 2024-01-20
# Commit 1 on 2024-01-21
# Commit 2 on 2024-01-21
# Commit 1 on 2024-01-22
# Commit 2 on 2024-01-22
# Commit 1 on 2024-01-23
# Commit 2 on 2024-01-23
# Commit 1 on 2024-01-24
# Commit 2 on 2024-01-24
# Commit 1 on 2024-01-25
# Commit 2 on 2024-01-25
# Commit 1 on 2024-01-26
# Commit 2 on 2024-01-26
# Commit 1 on 2024-01-27
# Commit 2 on 2024-01-27
# Commit 1 on 2024-01-28
# Commit 2 on 2024-01-28
# Commit 1 on 2024-01-29
# Commit 2 on 2024-01-29
# Commit 1 on 2024-01-30
# Commit 2 on 2024-01-30
# Commit 1 on 2024-01-31
# Commit 2 on 2024-01-31
# Commit 1 on 2024-02-01
# Commit 2 on 2024-02-01
# Commit 1 on 2024-02-02
# Commit 2 on 2024-02-02
# Commit 1 on 2024-02-03
# Commit 2 on 2024-02-03
# Commit 1 on 2024-02-04
# Commit 2 on 2024-02-04
# Commit 1 on 2024-02-05
# Commit 2 on 2024-02-05
# Commit 1 on 2024-02-06
# Commit 2 on 2024-02-06
# Commit 1 on 2024-02-07
# Commit 2 on 2024-02-07
# Commit 1 on 2024-02-08
# Commit 2 on 2024-02-08
# Commit 1 on 2024-02-09
# Commit 2 on 2024-02-09
# Commit 1 on 2024-02-10
# Commit 2 on 2024-02-10
# Commit 1 on 2024-02-11
# Commit 2 on 2024-02-11
# Commit 1 on 2024-02-12
# Commit 2 on 2024-02-12
# Commit 1 on 2024-02-13
# Commit 2 on 2024-02-13
# Commit 1 on 2024-02-14
# Commit 2 on 2024-02-14
# Commit 1 on 2024-02-15
# Commit 2 on 2024-02-15
# Commit 1 on 2024-02-16
# Commit 2 on 2024-02-16
# Commit 1 on 2024-02-17
# Commit 2 on 2024-02-17
# Commit 1 on 2024-02-18
# Commit 2 on 2024-02-18
# Commit 1 on 2024-02-19
# Commit 2 on 2024-02-19
# Commit 1 on 2024-02-20
# Commit 2 on 2024-02-20
# Commit 1 on 2024-02-21
# Commit 2 on 2024-02-21
# Commit 1 on 2024-02-22
# Commit 2 on 2024-02-22
# Commit 1 on 2024-02-23
# Commit 2 on 2024-02-23
# Commit 1 on 2024-02-24
# Commit 2 on 2024-02-24
# Commit 1 on 2024-02-25
# Commit 2 on 2024-02-25
# Commit 1 on 2024-02-26
# Commit 2 on 2024-02-26
# Commit 1 on 2024-02-27
# Commit 2 on 2024-02-27
# Commit 1 on 2024-02-28
# Commit 2 on 2024-02-28
# Commit 1 on 2024-02-29
# Commit 2 on 2024-02-29
# Commit 1 on 2024-03-01
# Commit 2 on 2024-03-01
# Commit 1 on 2024-03-02
# Commit 2 on 2024-03-02
# Commit 1 on 2024-03-03
# Commit 2 on 2024-03-03
# Commit 1 on 2024-03-04
# Commit 2 on 2024-03-04
# Commit 1 on 2024-03-05
# Commit 2 on 2024-03-05
# Commit 1 on 2024-03-06
# Commit 2 on 2024-03-06
# Commit 1 on 2024-03-07
# Commit 2 on 2024-03-07
# Commit 1 on 2024-03-08
# Commit 2 on 2024-03-08
# Commit 1 on 2024-03-09
# Commit 2 on 2024-03-09
# Commit 1 on 2024-03-10
# Commit 2 on 2024-03-10
# Commit 1 on 2024-03-11
# Commit 2 on 2024-03-11
# Commit 1 on 2024-03-12
# Commit 2 on 2024-03-12
# Commit 1 on 2024-03-13
# Commit 2 on 2024-03-13
# Commit 1 on 2024-03-14
# Commit 2 on 2024-03-14
# Commit 1 on 2024-03-15
# Commit 2 on 2024-03-15
# Commit 1 on 2024-03-16
# Commit 2 on 2024-03-16
# Commit 1 on 2024-03-17
# Commit 2 on 2024-03-17
# Commit 1 on 2024-03-18
# Commit 2 on 2024-03-18
# Commit 1 on 2024-03-19
# Commit 2 on 2024-03-19
# Commit 1 on 2024-03-20
# Commit 2 on 2024-03-20
# Commit 1 on 2024-03-21
# Commit 2 on 2024-03-21
# Commit 1 on 2024-03-22
# Commit 2 on 2024-03-22
# Commit 1 on 2024-03-23
# Commit 2 on 2024-03-23
# Commit 1 on 2024-03-24
# Commit 2 on 2024-03-24
# Commit 1 on 2024-03-25
# Commit 2 on 2024-03-25
# Commit 1 on 2024-03-26
# Commit 2 on 2024-03-26
# Commit 1 on 2024-03-27
# Commit 2 on 2024-03-27
# Commit 1 on 2024-03-28
# Commit 2 on 2024-03-28
# Commit 1 on 2024-03-29
# Commit 2 on 2024-03-29
# Commit 1 on 2024-03-30
# Commit 2 on 2024-03-30
# Commit 1 on 2024-03-31
# Commit 2 on 2024-03-31
# Commit 1 on 2024-04-01
# Commit 2 on 2024-04-01
# Commit 1 on 2024-04-02
# Commit 2 on 2024-04-02
# Commit 1 on 2024-04-03
# Commit 2 on 2024-04-03
# Commit 1 on 2024-04-04
# Commit 2 on 2024-04-04
# Commit 1 on 2024-04-05
# Commit 2 on 2024-04-05
# Commit 1 on 2024-04-06
# Commit 2 on 2024-04-06
# Commit 1 on 2024-04-07
# Commit 2 on 2024-04-07
# Commit 1 on 2024-04-08
# Commit 2 on 2024-04-08
# Commit 1 on 2024-04-09
# Commit 2 on 2024-04-09
# Commit 1 on 2024-04-10
# Commit 2 on 2024-04-10
# Commit 1 on 2024-04-11
# Commit 2 on 2024-04-11
# Commit 1 on 2024-04-12
# Commit 2 on 2024-04-12
# Commit 1 on 2024-04-13
# Commit 2 on 2024-04-13
# Commit 1 on 2024-04-14
# Commit 2 on 2024-04-14
# Commit 1 on 2024-04-15
# Commit 2 on 2024-04-15
# Commit 1 on 2024-04-16
# Commit 2 on 2024-04-16
# Commit 1 on 2024-04-17
# Commit 2 on 2024-04-17
# Commit 1 on 2024-04-18
# Commit 2 on 2024-04-18
# Commit 1 on 2024-04-19
# Commit 2 on 2024-04-19
# Commit 1 on 2024-04-20
# Commit 2 on 2024-04-20
# Commit 1 on 2024-04-21
# Commit 2 on 2024-04-21
# Commit 1 on 2024-04-22
# Commit 2 on 2024-04-22
# Commit 1 on 2024-04-23
# Commit 2 on 2024-04-23
# Commit 1 on 2024-04-24
# Commit 2 on 2024-04-24
# Commit 1 on 2024-04-25
# Commit 2 on 2024-04-25
# Commit 1 on 2024-04-26
# Commit 2 on 2024-04-26
# Commit 1 on 2024-04-27
# Commit 2 on 2024-04-27
# Commit 1 on 2024-04-28
# Commit 2 on 2024-04-28
# Commit 1 on 2024-04-29
# Commit 2 on 2024-04-29
# Commit 1 on 2024-04-30
# Commit 2 on 2024-04-30
# Commit 1 on 2024-05-01
# Commit 2 on 2024-05-01
# Commit 1 on 2024-05-02
# Commit 2 on 2024-05-02
# Commit 1 on 2024-05-03
# Commit 2 on 2024-05-03
# Commit 1 on 2024-05-04
# Commit 2 on 2024-05-04
# Commit 1 on 2024-05-05
# Commit 2 on 2024-05-05
# Commit 1 on 2024-05-06
# Commit 2 on 2024-05-06
# Commit 1 on 2024-05-07
# Commit 2 on 2024-05-07
# Commit 1 on 2024-05-08
# Commit 2 on 2024-05-08
# Commit 1 on 2024-05-09
# Commit 2 on 2024-05-09
# Commit 1 on 2024-05-10
# Commit 2 on 2024-05-10
# Commit 1 on 2024-05-11
# Commit 2 on 2024-05-11
# Commit 1 on 2024-05-12
# Commit 2 on 2024-05-12
# Commit 1 on 2024-05-13
# Commit 2 on 2024-05-13
# Commit 1 on 2024-05-14
# Commit 2 on 2024-05-14
# Commit 1 on 2024-05-15
# Commit 2 on 2024-05-15
# Commit 1 on 2024-05-16
# Commit 2 on 2024-05-16
# Commit 1 on 2024-05-17
# Commit 2 on 2024-05-17
# Commit 1 on 2024-05-18
# Commit 2 on 2024-05-18
# Commit 1 on 2024-05-19
# Commit 2 on 2024-05-19
# Commit 1 on 2024-05-20
# Commit 2 on 2024-05-20
# Commit 1 on 2024-05-21
# Commit 2 on 2024-05-21
# Commit 1 on 2024-05-22
# Commit 2 on 2024-05-22
# Commit 1 on 2024-05-23
# Commit 2 on 2024-05-23
# Commit 1 on 2024-05-24
# Commit 2 on 2024-05-24
# Commit 1 on 2024-05-25
# Commit 2 on 2024-05-25
# Commit 1 on 2024-05-26
# Commit 2 on 2024-05-26
# Commit 1 on 2024-05-27
# Commit 2 on 2024-05-27
# Commit 1 on 2024-05-28
# Commit 2 on 2024-05-28
# Commit 1 on 2024-05-29
# Commit 2 on 2024-05-29
# Commit 1 on 2024-05-30
# Commit 2 on 2024-05-30
# Commit 1 on 2024-05-31
# Commit 2 on 2024-05-31
# Commit 1 on 2024-06-01
# Commit 2 on 2024-06-01
# Commit 1 on 2024-06-02
# Commit 2 on 2024-06-02
# Commit 1 on 2024-06-03
# Commit 2 on 2024-06-03
# Commit 1 on 2024-06-04
# Commit 2 on 2024-06-04
# Commit 1 on 2024-06-05
# Commit 2 on 2024-06-05
# Commit 1 on 2024-06-06
# Commit 2 on 2024-06-06
# Commit 1 on 2024-06-07
# Commit 2 on 2024-06-07
# Commit 1 on 2024-06-08
# Commit 2 on 2024-06-08
# Commit 1 on 2024-06-09
# Commit 2 on 2024-06-09
# Commit 1 on 2024-06-10
# Commit 2 on 2024-06-10
# Commit 1 on 2024-06-11
# Commit 2 on 2024-06-11
# Commit 1 on 2024-06-12
# Commit 2 on 2024-06-12
# Commit 1 on 2024-06-13
# Commit 2 on 2024-06-13
# Commit 1 on 2024-06-14
# Commit 2 on 2024-06-14
# Commit 1 on 2024-06-15
# Commit 2 on 2024-06-15
# Commit 1 on 2024-06-16
# Commit 2 on 2024-06-16
# Commit 1 on 2024-06-17
# Commit 2 on 2024-06-17
# Commit 1 on 2024-06-18
# Commit 2 on 2024-06-18
# Commit 1 on 2024-06-19
# Commit 2 on 2024-06-19
# Commit 1 on 2024-06-20
# Commit 2 on 2024-06-20
# Commit 1 on 2024-06-21
# Commit 2 on 2024-06-21
# Commit 1 on 2024-06-22
# Commit 2 on 2024-06-22
# Commit 1 on 2024-06-23
# Commit 2 on 2024-06-23
# Commit 1 on 2024-06-24
# Commit 2 on 2024-06-24
# Commit 1 on 2024-06-25
# Commit 2 on 2024-06-25
# Commit 1 on 2024-06-26
# Commit 2 on 2024-06-26
# Commit 1 on 2024-06-27
# Commit 2 on 2024-06-27
# Commit 1 on 2024-06-28
# Commit 2 on 2024-06-28
# Commit 1 on 2024-06-29
# Commit 2 on 2024-06-29
# Commit 1 on 2024-06-30
# Commit 2 on 2024-06-30
# Commit 1 on 2024-07-01
# Commit 2 on 2024-07-01
# Commit 1 on 2024-07-02
# Commit 2 on 2024-07-02
# Commit 1 on 2024-07-03
# Commit 2 on 2024-07-03
# Commit 1 on 2024-07-04
# Commit 2 on 2024-07-04
# Commit 1 on 2024-07-05
# Commit 2 on 2024-07-05
# Commit 1 on 2024-07-06
# Commit 2 on 2024-07-06
# Commit 1 on 2024-07-07
# Commit 2 on 2024-07-07
# Commit 1 on 2024-07-08
# Commit 2 on 2024-07-08
# Commit 1 on 2024-07-09
# Commit 2 on 2024-07-09
# Commit 1 on 2024-07-10
# Commit 2 on 2024-07-10
# Commit 1 on 2024-07-11
# Commit 2 on 2024-07-11
# Commit 1 on 2024-07-12
# Commit 2 on 2024-07-12
# Commit 1 on 2024-07-13
# Commit 2 on 2024-07-13
# Commit 1 on 2024-07-14
# Commit 2 on 2024-07-14
# Commit 1 on 2024-07-15
# Commit 2 on 2024-07-15
# Commit 1 on 2024-07-16
# Commit 2 on 2024-07-16
# Commit 1 on 2024-07-17
# Commit 2 on 2024-07-17
# Commit 1 on 2024-07-18
# Commit 2 on 2024-07-18
# Commit 1 on 2024-07-19
# Commit 2 on 2024-07-19
# Commit 1 on 2024-07-20
# Commit 2 on 2024-07-20
# Commit 1 on 2024-07-21
# Commit 2 on 2024-07-21
# Commit 1 on 2024-07-22
# Commit 2 on 2024-07-22
# Commit 1 on 2024-07-23
# Commit 2 on 2024-07-23
# Commit 1 on 2024-07-24
# Commit 2 on 2024-07-24
# Commit 1 on 2024-07-25
# Commit 2 on 2024-07-25
# Commit 1 on 2024-07-26
# Commit 2 on 2024-07-26
# Commit 1 on 2024-07-27
# Commit 2 on 2024-07-27
# Commit 1 on 2024-07-28
# Commit 2 on 2024-07-28
# Commit 1 on 2024-07-29
# Commit 2 on 2024-07-29
# Commit 1 on 2024-07-30
# Commit 2 on 2024-07-30
# Commit 1 on 2024-07-31
# Commit 2 on 2024-07-31
# Commit 1 on 2024-08-01
# Commit 2 on 2024-08-01
# Commit 1 on 2024-08-02
# Commit 2 on 2024-08-02
# Commit 1 on 2024-08-03
# Commit 2 on 2024-08-03
# Commit 1 on 2024-08-04
# Commit 2 on 2024-08-04
# Commit 1 on 2024-08-05
# Commit 2 on 2024-08-05
# Commit 1 on 2024-08-06
# Commit 2 on 2024-08-06
# Commit 1 on 2024-08-07
# Commit 2 on 2024-08-07
# Commit 1 on 2024-08-08
# Commit 2 on 2024-08-08
# Commit 1 on 2024-08-09
# Commit 2 on 2024-08-09
# Commit 1 on 2024-08-10
# Commit 2 on 2024-08-10
# Commit 1 on 2024-08-11
# Commit 2 on 2024-08-11
# Commit 1 on 2024-08-12
# Commit 2 on 2024-08-12
# Commit 1 on 2024-08-13
