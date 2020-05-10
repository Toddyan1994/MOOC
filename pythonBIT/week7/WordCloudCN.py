# WordCloudCNV1.py
import wordcloud
import jieba
# import from txt
with open(r'pythonBIT\week7\President_Xi_Speech_Taiwan.txt',
          'r', encoding='utf-8') as f:
    t = f.read()
ls = jieba.lcut(t)
txt = ' '.join(ls)
# generate word cloud
w = wordcloud.WordCloud(width=1000, font_path='msyh.ttc',
                        height=618, background_color='red',
                        max_words=15)
w.generate(txt)
w.to_file('pycncloud_speech.png')
