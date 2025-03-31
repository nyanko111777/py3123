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

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("使用方法: python join_split_files.py [分割ディレクトリパス]")
        print("例: python join_split_files.py large_file_split")
        sys.exit(1)
    
    split_dir = sys.argv[1]
    if not Path(split_dir).exists():
        print(f"エラー: ディレクトリが見つかりません - {split_dir}")
        sys.exit(1)
    
    success = join_files(split_dir)
    sys.exit(0 if success else 1)