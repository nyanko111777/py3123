import os
from pathlib import Path

def find_large_files(directory='.', min_size_mb=50):
    """指定したサイズ以上のファイルを検索"""
    min_size = min_size_mb * 1024 * 1024
    large_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            try:
                file_size = file_path.stat().st_size
                if file_size > min_size:
                    large_files.append((str(file_path), file_size))
            except (PermissionError, OSError):
                continue
    
    return large_files

def split_large_files(large_files):
    """見つかった大きなファイルを分割"""
    for file_path, _ in large_files:
        print(f"\n{file_path} を分割中...")
        os.system(f'python split_large_files.py "{file_path}"')
        print(f"{file_path} の分割が完了しました")

def update_gitignore(large_files):
    """見つかった大きなファイルを.gitignoreに追加"""
    gitignore_path = Path('.gitignore')
    if not gitignore_path.exists():
        gitignore_path.touch()
    
    existing_entries = set()
    if gitignore_path.stat().st_size > 0:
        with open(gitignore_path, 'r') as f:
            existing_entries = set(line.strip() for line in f if line.strip())
    
    new_entries = set()
    for file_path, _ in large_files:
        new_entries.add(str(Path(file_path).name))
        new_entries.add(str(file_path))
        # 分割ディレクトリも追加
        new_entries.add(f"{file_path}_split")
    
    to_add = new_entries - existing_entries
    if to_add:
        with open(gitignore_path, 'a') as f:
            f.write('\n# 50MB以上の大きなファイル\n')
            for entry in sorted(to_add):
                f.write(f"{entry}\n")
        print(f"\n.gitignoreに{len(to_add)}件のエントリを追加しました")
    else:
        print("\n追加する.gitignoreエントリはありませんでした")

if __name__ == '__main__':
    print("50MB以上のファイルを検索中...")
    large_files = find_large_files()
    
    if large_files:
        print("\n以下の50MB以上のファイルが見つかりました:")
        for file_path, size in large_files:
            print(f"{size/1024/1024:.2f}MB - {file_path}")
        
        update_gitignore(large_files)
    else:
        print("50MB以上のファイルは見つかりませんでした。")