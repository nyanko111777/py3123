#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import shutil
import subprocess
import hashlib
from pathlib import Path

def get_git_diff_files():
    """
    Gitの差分ファイルリストを取得する
    """
    try:
        # 最新のコミットとの差分ファイルを取得
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD'],
            capture_output=True, text=True, check=True
        )
        modified_files = result.stdout.strip().split('\n')
        
        # ステージングされていないファイルも取得
        result = subprocess.run(
            ['git', 'ls-files', '--others', '--exclude-standard'],
            capture_output=True, text=True, check=True
        )
        untracked_files = result.stdout.strip().split('\n')
        
        # 空の要素を削除して結合
        all_files = [f for f in modified_files + untracked_files if f]
        return all_files
    except subprocess.CalledProcessError as e:
        print(f"Gitコマンドの実行中にエラーが発生しました: {e}")
        return []

def copy_files_to_diff_folder(files, diff_folder):
    """
    差分ファイルを指定フォルダにコピーし、ファイルマッピング情報を返す
    """
    # 差分フォルダが存在しない場合は作成
    os.makedirs(diff_folder, exist_ok=True)
    
    file_mapping = {}
    
    for file_path in files:
        if not file_path or not os.path.exists(file_path):
            continue
            
        # ファイル名の衝突を避けるためにハッシュを使用
        file_hash = hashlib.md5(file_path.encode()).hexdigest()[:8]
        original_filename = os.path.basename(file_path)
        new_filename = f"{file_hash}_{original_filename}"
        
        # 差分フォルダにコピー
        dest_path = os.path.join(diff_folder, new_filename)
        shutil.copy2(file_path, dest_path)
        
        # マッピング情報を記録
        file_mapping[new_filename] = file_path
        
        print(f"コピー: {file_path} -> {dest_path}")
    
    return file_mapping

def main():
    # 差分フォルダのパス
    diff_folder = "diff_py3123"
    
    # Gitの差分ファイルを取得
    diff_files = get_git_diff_files()
    
    if not diff_files:
        print("差分ファイルが見つかりませんでした。")
        return
    
    print(f"検出された差分ファイル数: {len(diff_files)}")
    
    # 差分ファイルをコピーしてマッピング情報を取得
    file_mapping = copy_files_to_diff_folder(diff_files, diff_folder)
    
    # マッピング情報をJSONファイルに保存
    mapping_file = os.path.join(diff_folder, "file_mapping.json")
    with open(mapping_file, 'w', encoding='utf-8') as f:
        json.dump(file_mapping, f, ensure_ascii=False, indent=2)
    
    print(f"\n処理が完了しました。")
    print(f"コピーされたファイル数: {len(file_mapping)}")
    print(f"マッピング情報: {mapping_file}")

if __name__ == "__main__":
    main()