#!/bin/bash

echo "🔍 Running ruff check..."
ruff check .

echo ""
read -p "❓ Do you want to run ruff format? (y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🎨 Running ruff format..."
    ruff format .
else
    echo "🚫 Skipping ruff format."
fi


read -p "❓ Do you want to commit and push all changes? (y/n): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "🚫 Push cancelled."
    exit 0
fi

# Добавляем все изменения (включая новые файлы)
git add .

git commit -m "test"


git push origin main