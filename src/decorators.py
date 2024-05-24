from functools import wraps
from typing import Any, Callable


def log(filename: str | None) -> Callable:
    """
    Декоратор логирует вызов функции и ее результат в файл или в консоль
    """
    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                log_info = "my_function ok"
                result = function(*args, **kwargs)
            except Exception:
                log_info = "my_function error"
            if filename:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(log_info)
            else:
                print(log_info)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """
    Функция суммирует числа
    """
    return x + y
