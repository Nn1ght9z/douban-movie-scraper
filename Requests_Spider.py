# -*- coding:utf-8 -*-
# @Time : 2025/4/2 19:35
# @Author : Nn1ght9z
# @File : Requests_Spider.py
# @Software : PyCharm

import time
import random  # randomモジュールをインポートしてランダム遅延を生成
import requests
import re
import xlwt
from bs4 import BeautifulSoup

# 正規表現オブジェクトを作成（文字列パターンのルール）
# 映画詳細リンクのルール
findLink = re.compile(r'a href="(.*?)">')
# 映画画像
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.Sで改行文字を包含
# 映画タイトル
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 映画評価
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 評価者数
findJudge = re.compile(r'<span>(\d*)人評価</span>')
# 概要検索
findInq = re.compile(r'<p\s+class="quote"[^>]*>[\s\S]*?<span[^>]*>(.*?)<\/span>[\s\S]*?<\/p>', re.S)  # inqのspanを直接マッチング
# 関連情報検索
findBd = re.compile(r'<p>(.*?)</p>', re.S)

# クローラー第一段階: ウェブコンテンツの取得
# クローラーを通常のブラウザとして偽装
user_cookie = 'bid=BySP1GHf6dc; ll="118243"; push_noty_num=0; push_doumail_num=0; dbcl2="288069729:770X3UMAIhA"; ck=zU8G; ap_v=0,6.0'
# 完全なリクエストヘッダーの構築
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Cookie": user_cookie,
    "Referer": "https://movie.douban.com/"  # 参照元ページをシミュレート
}

# Sessionオブジェクトを使用してセッションを維持
session = requests.Session()
session.headers.update(head)

datalist = []
for start_num in range(0, 250, 25):
    # ランダム遅延を追加
    time.sleep(random.uniform(1, 3))
    try:
        url = f"https://movie.douban.com/top250?start={start_num}"
        response = session.get(url)  # Responseクラスのインスタンス
        if response.ok:  # ok属性でリクエスト成功を判断
            html = response.text  # レスポンス内容を文字列で取得
            soup = BeautifulSoup(html, "html.parser")  # HTMLパーサーで解析
            for item in soup.find_all('div', class_='item'):
                data = []  # 1作品の全情報を保存
                item = str(item)

                # リンク抽出
                link = re.findall(findLink, item)[0]
                data.append(link)  # リンク追加

                # 画像抽出
                imgSrc = re.findall(findImgSrc, item)[0]
                data.append(imgSrc)  # 画像追加

                # タイトル抽出
                titles = re.findall(findTitle, item)
                if len(titles) == 2:
                    Chinesetitle = titles[0]
                    data.append(Chinesetitle)  # 中国語タイトル
                    othertitle = titles[1].replace("/", "")  # 不要記号を削除
                    data.append(othertitle)  # 外国語タイトル
                else:
                    data.append(titles[0])
                    data.append(' ')  # 外国語タイトル空白

                # 評価抽出
                rating = re.findall(findRating, item)[0]
                data.append(rating)  # 評価追加

                # 評価者数抽出
                judgeNum = re.findall(findJudge, item)[0]
                data.append(judgeNum)  # 評価者数追加

                # 概要抽出
                inq = re.findall(findInq, item)
                if len(inq) != 0:
                    inq = inq[0].replace("。", "")  # 句点を削除
                    data.append(inq)  # 概要追加
                else:
                    data.append(" ")  # 空白

                # 関連情報抽出
                bd = re.findall(findBd, item)[0]
                bd = re.sub(r'<br(\s+)?/>(\s+)?', ' ', bd)  # <br/>削除
                bd = re.sub('/', " ", bd)  # /を削除
                data.append(bd.strip())  # 前後空白削除

                datalist.append(data)  # 処理済みデータをリストに追加

    except Exception as e:
        print(f"ページ{start_num}の取得エラー: {e}")

moviebook = xlwt.Workbook(encoding='utf-8', style_compression=0)  # Workbookオブジェクト作成
moviesheet = moviebook.add_sheet('Douban_Movie_TOP250', cell_overwrite_ok=True)  # ワークシート追加
cols = ("映画詳細リンク", "画像リンク", "中国語タイトル", "外国語タイトル", "評価", "評価者数", "概要", "関連情報")
for i, col in enumerate(cols):
    moviesheet.write(0, i, col)

for i, data in enumerate(datalist, 1):
    for j, value in enumerate(data):
        moviesheet.write(i, j, value)

moviebook.save('Douban_Movie_TOP250.xls')
print(f"データ{len(datalist)}件を成功裏に保存")
