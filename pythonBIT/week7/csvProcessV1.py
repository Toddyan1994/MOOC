# csvProcessV1.py
with open(r'pythonBIT\week7\test.csv', 'r',
          encoding='utf-8') as fo:
          lines = fo.readlines()
          lines.reverse()
          for line in lines:
              line=line.replace(' ', '')
              line = line.replace('\n', '')
              t = line.split(',')
              t.reverse()
              print(';'.join(t))


