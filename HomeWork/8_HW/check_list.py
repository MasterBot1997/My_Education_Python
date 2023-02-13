from logg import logging

def check_last_id(num):
    if num.isdigit():
        logging.info(f"Последний id - {num}")
        return int(num)
    else:
        logging.info("Это первая запись данных о пользователе id - 1")
        num = 0
        return int(num)