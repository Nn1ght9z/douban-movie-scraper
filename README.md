# Douban Movie Top250 Scraper || 豆瓣映画Top250スクレイパー

A Python web scraper for collecting Douban's Top 250 movies information || 豆瓣映画TOP250の情報を収集するPythonウェブスクレイパー

## Features || 特徴
- Scrapes movie details including title, rating, reviews and descriptions || タイトル、評価、レビュー数、概要を含む映画詳細情報を収集
- Automatically handles pagination and random delays || 自動ページネーション処理とランダム遅延機能
- Exports data to Excel format (.xls) || Excel形式(.xls)へのデータ出力
- Anti-crawler evasion measures implemented || アンチクローラー対策を実装

## Technologies Used || 使用技術
- Python 3 || Python 3
- Requests (HTTP library) || Requests (HTTPライブラリ)
- BeautifulSoup (HTML parsing) || BeautifulSoup (HTML解析)
- xlwt (Excel export) || xlwt (Excel出力)
- Regular Expressions || 正規表現

## Installation || インストール
```bash
pip install requests beautifulsoup4 xlwt || pip install requests beautifulsoup4 xlwt
