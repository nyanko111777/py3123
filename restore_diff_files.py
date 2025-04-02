#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import shutil
from pathlib import Path

def restore_files(diff_folder):
    """
    u5deeu5206u30d5u30a9u30ebu30c0u304bu3089u30d5u30a1u30a4u30ebu3092u5143u306eu5834u6240u306bu5fa9u5143u3059u308b
    """
    # u30deu30c3u30d4u30f3u30b0u30d5u30a1u30a4u30ebu306eu30d1u30b9
    mapping_file = os.path.join(diff_folder, "file_mapping.json")
    
    if not os.path.exists(mapping_file):
        print(f"u30a8u30e9u30fc: u30deu30c3u30d4u30f3u30b0u30d5u30a1u30a4u30eb {mapping_file} u304cu898bu3064u304bu308au307eu305bu3093u3002")
        return
    
    # u30deu30c3u30d4u30f3u30b0u60c5u5831u3092u8aadu307fu8fbcu3080
    with open(mapping_file, 'r', encoding='utf-8') as f:
        file_mapping = json.load(f)
    
    restored_count = 0
    errors = []
    
    for diff_filename, original_path in file_mapping.items():
        # u5deeu5206u30d5u30a9u30ebu30c0u5185u306eu30d5u30a1u30a4u30ebu30d1u30b9
        source_path = os.path.join(diff_folder, diff_filename)
        
        if not os.path.exists(source_path):
            errors.append(f"u30a8u30e9u30fc: u30bdu30fcu30b9u30d5u30a1u30a4u30eb {source_path} u304cu898bu3064u304bu308au307eu305bu3093u3002")
            continue
        
        # u5fa9u5143u5148u306eu30c7u30a3u30ecu30afu30c8u30eau3092u4f5cu6210
        os.makedirs(os.path.dirname(original_path), exist_ok=True)
        
        try:
            # u30d5u30a1u30a4u30ebu3092u5143u306eu5834u6240u306bu30b3u30d4u30fc
            shutil.copy2(source_path, original_path)
            print(f"u5fa9u5143: {source_path} -> {original_path}")
            restored_count += 1
        except Exception as e:
            errors.append(f"u30a8u30e9u30fc: {original_path} u306eu5fa9u5143u4e2du306bu554fu984cu304cu767au751fu3057u307eu3057u305f: {e}")
    
    print(f"\nu51e6u7406u304cu5b8cu4e86u3057u307eu3057u305fu3002")
    print(f"u5fa9u5143u3055u308cu305fu30d5u30a1u30a4u30ebu6570: {restored_count} / {len(file_mapping)}")
    
    if errors:
        print("\nu767au751fu3057u305fu30a8u30e9u30fc:")
        for error in errors:
            print(f"- {error}")

def main():
    # u5deeu5206u30d5u30a9u30ebu30c0u306eu30d1u30b9
    diff_folder = "diff_py3123"
    
    if not os.path.exists(diff_folder):
        print(f"u30a8u30e9u30fc: u5deeu5206u30d5u30a9u30ebu30c0 {diff_folder} u304cu898bu3064u304bu308au307eu305bu3093u3002")
        return
    
    # u78bau8a8du30e1u30c3u30bbu30fcu30b8
    print(f"u5deeu5206u30d5u30a1u30a4u30ebu3092 {diff_folder} u304bu3089u5143u306eu5834u6240u306bu5fa9u5143u3057u307eu3059u3002")
    confirm = input("u7d9au884cu3057u307eu3059u304buff1f (y/n): ")
    
    if confirm.lower() != 'y':
        print("u51e6u7406u3092u4e2du6b62u3057u307eu3057u305fu3002")
        return
    
    # u30d5u30a1u30a4u30ebu3092u5fa9u5143
    restore_files(diff_folder)

if __name__ == "__main__":
    main()