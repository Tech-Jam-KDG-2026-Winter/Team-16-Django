# MoveShare 
運動を「孤独な努力」から「共有する楽しみ」へ　

運動が続かない最大の理由は、一人で成果が見えにくいことにあります。本アプリは、日々の運動を記録・共有し、仲間からのリアクションを得ることで、習慣化を強力にサポートするSNSプラットフォームです。

<img src="https://github.com/user-attachments/assets/0d5778b6-6670-4b82-85cd-36141e5632b7" width="100%">


## 開発の背景（課題と解決策）
課題：なぜ運動は続かないのか？
孤独感： 一人だとモチベーションを維持しにくい。

実感の薄さ： 成果が出るまでに時間がかかり、途中で挫折してしまう。

既存アプリの不満： 記録するだけの「自己完結型」が多く、他者との繋がりが薄い。

解決策：共有と反応が習慣を作る
可視化と共有： 自分の頑張りを投稿し、仲間からの「いいね」で承認欲求を満たす。

相互刺激： 他のユーザーの活動がタイムラインに流れることで、自分もやろうという刺激を受ける。

手軽さの追求： 記録の心理的ハードルを下げ、スマホでサッと報告できる環境を提供。

## 実装のこだわり
「スマホファースト」な操作性

外出先や運動直後に手軽に投稿・閲覧ができるよう、モバイルでの利用を想定したUI/UXを設計しました。

情報の引き算（シンプルデザイン）

画面全体のトーンに統一感を持たせ、余計な情報を削ぎ落とすことで「今、何をすべきか（投稿・確認）」が直感的にわかるデザインを意識しました。

モチベーション維持の仕組み

リアクション（いいね）機能を核に据え、自分一人の記録で終わらせない「つながり」を重視した機能構成にしています。

## 機能一覧
機能を整理し、優先度の高いものを中心に構成しています。

### 1. 運動記録・SNS機能
運動投稿： タイトル、時間、内容をサクッと記録。

タイムライン： 自分や他ユーザーの投稿を一覧で表示。

リアクション（いいね）： 仲間の投稿を応援し、モチベーションを循環。

フォロー機能： 特定の仲間と繋がり、活動を追いやすくする。

### 2. ユーザー管理機能
アカウント管理： 新規登録、ログイン、パスワード再設定。

プロフィール： 自己紹介や過去の投稿履歴の閲覧・編集。

### 3. 管理者向け機能
ダッシュボード： 全ユーザー・全投稿の状況把握。

コンテンツ管理： 不適切なユーザーの停止（BAN）や投稿の削除権限。
## 技術スタック

### バックエンド

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4%2F5-darkgreen?logo=django&logoColor=white)

- Python 3.x  
- Django 4.x / 5.x  
---

### フロントエンド

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

- Mobile First UI (390x844)
- Custom CSS Card Design

---

### データベース

![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

- SQLite3
---

### 管理

![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)

- GitHub
## アプリ画面

<table>
<tr>
<td align="center">

### トップ画面

<img width="533" height="725" alt="TOP" src="https://github.com/user-attachments/assets/4d009317-5edd-4eb2-99aa-77230bf07cab" width="250">

</td>

<td align="center">

### ログイン画面

<img width="531" height="729" alt="LOGIN" src="https://github.com/user-attachments/assets/940cba66-d9f8-4c98-9f76-e6ba3328ccca" width="250">

</td>
</tr>
<tr>
<td align="center">

### 新規登録画面

<img width="527" height="719" alt="NEW" src="https://github.com/user-attachments/assets/b473f642-1d53-40a9-b759-ccba2cfb0372" width="250">

</td>

<td align="center">

### パスワード再登録画面

<img width="530" height="728" alt="PASS" src="https://github.com/user-attachments/assets/86dbb6a7-0e0c-403b-8047-576bd872bea6" width="250">

</td>
</tr>
<tr>
<td align="center">

### 投稿一覧画面

<img width="519" height="724" alt="LIST" src="https://github.com/user-attachments/assets/bbd5cb8b-33b1-477c-a47a-094a6592f4d2" width="250">

</td>

<td align="center">

### 投稿詳細画面

<img width="516" height="716" alt="DETAIL" src="https://github.com/user-attachments/assets/1d98bf79-ecfc-4483-b723-570cfd79a465" width="250">

</td>
</tr>
<tr>
<td align="center">

### 投稿作成画面

<img width="527" height="726" alt="POST" src="https://github.com/user-attachments/assets/ccb5bf43-268f-4ad1-8e6d-38895d7ed34f" width="250">

</td>

<td align="center">

### 投稿編集画面

<img width="517" height="720" alt="POSTDIT" src="https://github.com/user-attachments/assets/09a3551b-e61a-44e3-91c2-5c72cd5d8569" width="250">

</td>
</tr>
<tr>
<td align="center">

### プロフィール画面

<img width="530" height="729" alt="PRO" src="https://github.com/user-attachments/assets/9807b12e-6835-4ecc-af28-ab19c8454b7b" width="250">

</td>

<td align="center">

### プロフィール編集画面

<img width="497" height="723" alt="EDIT" src="https://github.com/user-attachments/assets/55105f7d-fbcc-4a06-abbb-48b29eec9d76" width="250">

</td>
</tr>

<tr>
<td align="center">

### フォロー一覧画面

<img width="513" height="718" alt="FOLLOW" src="https://github.com/user-attachments/assets/1a3716f9-4770-4426-82b2-481e294fb75c" width="250">

</td>

<td align="center">

### ナビゲーションメニュー

<img width="521" height="712" alt="NAVI" src="https://github.com/user-attachments/assets/b149db10-d55c-46ff-bf27-f2224b0ee14d" width="250">

</td>
</tr>
</table>



## 画面遷移図
<img width="801" height="511" alt="Move_page" src="https://github.com/user-attachments/assets/a19b155d-6bac-4bee-9b0b-4976dc763a1d" />

## ER図
<img width="1008" height="787" alt="Move_ER" src="https://github.com/user-attachments/assets/a23046eb-11f6-424e-8e85-7f1c391b044b" />



