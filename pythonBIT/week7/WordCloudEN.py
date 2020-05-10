# WordCloudENV1.py
import wordcloud
# read input from txt file
with open(r'pythonBIT\week7\Trump_union_speech.txt',
          'r', encoding='utf-8') as f:
    txt = f.read()
# generate wordcloud
w = wordcloud.WordCloud(width=1000, font_path='msyh.ttc',
                        height=618, background_color='black',
                        max_words=15)
w.generate(txt)
w.to_file('pyencloud_hamlet.png')
