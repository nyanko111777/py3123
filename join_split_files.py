import os
import json
from pathlib import Path

def join_files(split_dir):
    """分割ファイルを結合して元のファイルに復元"""
    split_dir = Path(split_dir)
    info_file = split_dir / "split_info.json"
    
    if not info_file.exists():
        print(f"エラー: split_info.jsonが見つかりません - {split_dir}")
        return False
    
    with open(info_file) as f:
        split_info = json.load(f)
    
    original_path = Path(split_info["original_path"])
    original_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(original_path, 'wb') as output_file:
        for chunk_info in split_info["chunks"]:
            chunk_path = split_dir / chunk_info["name"]
            with open(chunk_path, 'rb') as chunk_file:
                output_file.write(chunk_file.read())
    
    # ファイルサイズを検証
    if original_path.stat().st_size == split_info["original_size"]:
        print(f"復元成功: {original_path}")
        return True
    else:
        print(f"警告: 復元後のファイルサイズが一致しません - {original_path}")
        return False

def find_split_dirs(directory='.'):
    """_splitで終わるディレクトリを再帰的に検索"""
    split_dirs = []
    for root, dirs, _ in os.walk(directory):
        for dir_name in dirs:
            if dir_name.endswith('_split'):
                split_dirs.append(Path(root) / dir_name)
    return split_dirs

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) == 1:
        # 引数なし: 自動検索モード
        split_dirs = find_split_dirs()
        if not split_dirs:
            print("結合可能な分割ディレクトリが見つかりませんでした")
            sys.exit(0)
            
        print("以下の分割ディレクトリが見つかりました:")
        for i, dir_path in enumerate(split_dirs, 1):
            print(f"{i}: {dir_path}")
            
        total_success = True
        for dir_path in split_dirs:
            print(f"\n{dir_path} を結合中...")
            success = join_files(dir_path)
            total_success = total_success and success
            
        sys.exit(0 if total_success else 1)
        
    elif len(sys.argv) == 2:
        # 従来の単一ディレクトリ指定モード
        split_dir = sys.argv[1]
        if not Path(split_dir).exists():
            print(f"エラー: ディレクトリが見つかりません - {split_dir}")
            sys.exit(1)
            
        success = join_files(split_dir)
        sys.exit(0 if success else 1)
        
    else:
        print("使用方法: python join_split_files.py [分割ディレクトリパス]")
        print("例1: python join_split_files.py (自動検索モード)")
        print("例2: python join_split_files.py large_file_split")
        sys.exit(1)