#!/bin/bash

# version as argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <version_number>"
    exit 1
fi

# temporary dir
temp_dir="delete-line-addon"
mkdir -p "$temp_dir"

# cpy necessary files
cp __init__.py README.md LICENSE text_ot_delete_line.py blender_manifest.toml "$temp_dir"

version="$1"
zip_name="delete-line-addon-v${version}.zip"
zip -r "$zip_name" "$temp_dir"

mkdir -p releases
mv "$zip_name" releases/

# clean up
rm -rf "$temp_dir"

echo "Release created: releases/$zip_name"
