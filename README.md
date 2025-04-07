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
```

## Important Notes || 注意事項
- Respect website's robots.txt and terms of service || サイトのrobots.txtと利用規約を遵守してください  
- Add proper delays (1-3s) between requests || リクエスト間に適切な遅延(1-3秒)を追加してください  
- Rotate User-Agents if blocked || ブロックされた場合User-Agentを変更してください  
- Website structure changes may require code updates || サイト構造変更時はコード修正が必要です  
- Do NOT use for commercial purposes || 商業目的での使用は禁止です  
- Maintain request frequency under 10 requests/min || リクエスト頻度は10回/分以下に保ってください  
- Store data responsibly and delete if requested || データは責任を持って管理し、要請時は削除してください  
- For educational purposes only || 教育目的のみでの使用  
