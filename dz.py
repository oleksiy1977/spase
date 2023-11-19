def main():
    pass
import os
import shutil
import mimetypes
def normalize(filename):
    filename = ''.join(c if c.isalnum() or c in ['.', '_'] else '_' for c in filename)
    return filename
def sort_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Папка '{folder_path}' не існує.")
        return
    categories = ['images', 'video', 'documents', 'audio', 'archives']
    for category in categories:
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)

    # Проходимо по всіх елементах у папці
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Якщо це папка, викликаємо рекурсивно sort_folder
        if os.path.isdir(item_path) and item not in categories:
            sort_folder(item_path)

        # Якщо це файл
        elif os.path.isfile(item_path):
            # Нормалізуємо ім'я файлу
            normalized_name = normalize(item)

            # Отримуємо розширення файлу
            _, file_extension = os.path.splitext(normalized_name)

            # Визначаємо тип файлу за MIME-типом
            mime_type, _ = mimetypes.guess_type(item_path)

            # Переносимо файл до відповідної категорії
            if mime_type:
                if 'image' in mime_type:
                    shutil.move(item_path, os.path.join(folder_path, 'images', normalized_name))
                elif 'video' in mime_type:
                    shutil.move(item_path, os.path.join(folder_path, 'video', normalized_name))
                elif 'audio' in mime_type:
                    shutil.move(item_path, os.path.join(folder_path, 'audio', normalized_name))
                elif 'document' in mime_type:
                    shutil.move(item_path, os.path.join(folder_path, 'documents', normalized_name))
            elif file_extension.lower() in ['zip', 'gz', 'tar']:
                # Розпаковуємо архів та переносимо його вміст
                archive_path = os.path.join(folder_path, 'archives', normalized_name)
                os.makedirs(archive_path, exist_ok=True)
                shutil.unpack_archive(item_path, archive_path)
                os.remove(item_path)
            else:
                # Якщо розширення невідоме, залишаємо файл без змін
                shutil.move(item_path, os.path.join(folder_path, normalized_name))
sort_folder('/user/Desktop/Мотлох')
if __name__ =="_main_":
    print (main)
