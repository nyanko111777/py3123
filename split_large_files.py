import os
import json
from pathlib import Path

def split_file(file_path, chunk_size_mb=49):
    """大きなファイルを分割"""
    chunk_size = chunk_size_mb * 1024 * 1024
    file_path = Path(file_path)
    output_dir = file_path.parent / f"{file_path.name}_split"
    output_dir.mkdir(exist_ok=True)
    
    # 分割情報を記録するJSON
    split_info = {
        "original_path": str(file_path),
        "original_size": file_path.stat().st_size,
        "chunk_size_mb": chunk_size_mb,
        "chunks": []
    }
    
    with open(file_path, 'rb') as f:
        chunk_num = 0
        while True:
            chunk_data = f.read(chunk_size)
            if not chunk_data:
                break
            
            chunk_name = f"{file_path.name}.part{chunk_num:03d}"
            chunk_path = output_dir / chunk_name
            with open(chunk_path, 'wb') as chunk_file:
                chunk_file.write(chunk_data)
            
            split_info["chunks"].append({
                "name": chunk_name,
                "size": len(chunk_data)
            })
            chunk_num += 1
    
    # 分割情報をJSONに保存
    info_file = output_dir / "split_info.json"
    with open(info_file, 'w') as f:
        json.dump(split_info, f, indent=2)
    
    return output_dir

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("使用方法: python split_large_files.py [ファイルパス]")
        sys.exit(1)
    
    file_to_split = sys.argv[1]
    if not Path(file_to_split).exists():
        print(f"エラー: ファイルが見つかりません - {file_to_split}")
        sys.exit(1)
    
    print(f"{file_to_split} を分割中...")
    output_dir = split_file(file_to_split)
    print(f"分割完了: {output_dir}")