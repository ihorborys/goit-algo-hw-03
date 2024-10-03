import os
import shutil


def copy_files_recursively(src_dir, dest_dir):
    """
    Рекурсивно копіює файли з вихідної директорії до нової директорії та сортує їх за розширенням.
    """
    try:
        # Перебір всіх елементів у вихідній директорії
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            # Якщо це директорія, викликати функцію рекурсивно
            if os.path.isdir(item_path):
                copy_files_recursively(item_path, dest_dir)
            else:
                # Якщо це файл, копіювати його
                ext = os.path.splitext(item)[1].lower()  # Отримати розширення файлу
                if not ext:
                    ext = 'no_extension'  # Якщо файл без розширення

                # Створити відповідну піддиректорію у директорії призначення
                ext_dir = os.path.join(dest_dir, ext[1:])  # Видалити крапку з розширення
                os.makedirs(ext_dir, exist_ok=True)

                # Копіювати файл у нову директорію
                shutil.copy2(item_path, ext_dir)
                print(f"Копіюю {item_path} до {ext_dir}")

    except Exception as e:
        print(f"Помилка при обробці: {e}")

src_dir = 'Temp'
copy_files_recursively(input('Введіть вихідну директорію: '), dest_dir  = 'dist')