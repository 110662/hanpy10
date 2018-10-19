可視化ツールDashについて


---    

目次    

1 Dashの解説      
2．Dashのギャラリーで実際に見てみる     
3．ちょっとコードを見てみる     
3.1　ちょっと難しかったところ-callback      
3.2  データの形     
3.3　リアルタイムで使う     

---
自己紹介
* 小川英幸(@mazarimono)    
* はんなりPython主催者     
* Blockchainkyotoも主催    
* プログラマーではありません。     
* 最近ハッカソン行ってみたいなと思っている。    
      
---    
     
Dash User Guideを見ながら。     
<br>
資料を見てもわからない場合はここへ     
<br>
https://dash.plot.ly/     
     
---
     
Dash / Flask, Plotly.js, React.jsを使って作られたデータビジュアライゼーションアプリ。      
       webブラウザーに出力できる。     
<br>
flask: Pythonのウェブサーバーライブラリ     
<br>
React: フロントエンドのレンダーコンポーネント　悪名高きFacebookがメンテしてるらしい     

--- 

可視化　/ データ分析において重要。データ眺める時間が多い。     
<br>
可視化ツール　/ たくさんある。大体pandasとの親和性も高いし、どれも良い。     
代表的なもの　matplotlib/ seaborn/ bokeh /plotly     
<br>
きれいに見える＆簡単にかけるのが良いと思う。グラフ書くのって意外に難しかったりする。     
で、最近機能的にDash凄いなと思ったので紹介。     

---     

すごみ     
<br>
サイトを見るとわかる。（ギャラリー）    
<br>
https://dash.plot.ly/gallery     

---

## Plotlyは凄いグラフ書くの簡単    
しかし・・・idとかpassword、さらにAPIの制限とかあった。   
<br> 
まぁ有料ツールだしね　＝＝＞　Dashは制限が何もない。     

ブラウザーで見られる    
みんなで共有するとか良いような。     
アプリ化して技術を現金化！     

---    

## import 
<br>
dash /     
入れものつくり         
dash_core_component /     
https://dash.plot.ly/dash-core-components          
色々なツールとグラフを書くツールが入っている。     
dash_html_component /      
htmlを書くのに使う。     
     
---    

## わかりにくかったもの
callback      
<br>
まずユーザーがアプリをスタートした時点でデータがメモリに読み込まれる。      
可能であればグローバルスコープでデータの読み込みは行われるべきだ。      
コールバックはスコープの外側のデータを変化させるべきではない。      
もしコールバックでデータを変化させると、ほかのユーザーのセッションに影響を及ぼす。     

---

component_property Is 何？　＝＞　調べているとjavascriptがどうのこうのと出てきた。      
https://qiita.com/jkr_2255/items/66a16bd969454ee8b114      
たぶんそういうことなのだろう。      
ちなみに作る時には、適当に入れてみて、エラーを見て変えてみたいな感じで作っている。      
      
---    

* Stateというのもあってやな。      
      
* グラフを作る際のデータの形。      
      
* Liveupdate / dccのIntervalを使う。      
      
---         

使われてたデータで気になったもの      
<br>
newsapi     
https://newsapi.org/     
fivrthirtyeight      
https://fivethirtyeight.com/     
