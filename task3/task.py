import sys
from pathlib import Path
from colorama import Fore, Style

def print_directory_structure(directory, prefix=""):
    try:
        entries = list(Path(directory).iterdir())
    except FileNotFoundError:
        print(Fore.RED + "Директорію не знайдено. Перевірте шлях.")
        return
    except NotADirectoryError:
        print(Fore.RED + "Вказаний шлях не є директорією.")
        return

    for entry in entries:
        if entry.is_dir():
            print(f"{prefix}{Fore.BLUE}{entry.name}{Style.RESET_ALL}/")
            print_directory_structure(entry, prefix + "  ")
        elif entry.is_file():
            print(f"{prefix}{Fore.GREEN}{entry.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
        sys.exit(1)

    directory_path = sys.argv[1]

    print_directory_structure(directory_path)

#  python task3/task.py task3