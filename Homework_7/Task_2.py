import os
import sys
import pickle

# Cериализация путей, которые уже были обработаны
def save_paths(paths):
    with open('processed_paths.pkl', 'wb') as f:
        pickle.dump(paths, f)

# Десериализации сохраненных путей
def load_paths():
    try:
        with open('processed_paths.pkl', 'rb') as f:
            processed_paths = pickle.load(f)
            return processed_paths
    except FileNotFoundError:
        return set()

# Поиск файлов и папок
def count_files_and_folders(path, max_count=None):
    processed_paths = load_paths()
    files = []
    folders = []
    sizes = []
    names = []

    try:
        for root, _, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(root, filename)
                if filepath not in processed_paths:
                    processed_paths.add(filepath)
                    try:
                        size = os.path.getsize(filepath)
                        sizes.append(size)
                        names.append(filename)
                        files.append(filepath)
                    except OSError:
                        pass
                    if max_count and len(files) >= max_count:
                        break

            for folder in os.listdir(root):
                folderpath = os.path.join(root, folder)
                if folderpath not in processed_paths:
                    processed_paths.add(folderpath)
                    try:
                        folders.append(folderpath)
                    except OSError:
                        pass
                    if max_count and len(folders) >= max_count:
                        break

            if max_count and (len(files) + len(folders)) >= max_count:
                break

    except KeyboardInterrupt:
        save_paths(processed_paths)
        sys.exit()

    save_paths(processed_paths)

    print(f'Quantity of files: {len(files)}')
    if files:
        print(f'The biggest file: {max(files, key=os.path.getsize)}')
        print(f'The smallest file: {min(files, key=os.path.getsize)}')
        print(f'The longest file name: {max(names, key=len)}')
        print(f'The shortest file name: {min(names, key=len)}')

    print(f'Quantity of folders: {len(folders)}')
    if folders:
        print(f'The longest folder path: {max(folders, key=len)}')
        print(f'The shortest folder path: {min(folders, key=len)}')

if __name__ == '__main__':
    count_files_and_folders('/Users/vladostapenko/PycharmProjects/hillel_homeworks', max_count=100)



