import codecs

def line_healing(line):
    content = line.rstrip()[8:].split('//')
    to_add = []
    for inflex in content:
        if inflex[-3:] == 'аго':
            to_add.append(inflex[:-3] + 'ово')
            to_add.append(inflex[:-3] + 'ого')
    content += to_add
    content = set(content)
    return ' -flex: ' + '//'.join(content) + '\r\n'


f = codecs.open('C:\\Users\\Tatiana\Documents\GitHub\paradigm_tagging\прилфлексии.txt', 'r', 'utf-8')

a = codecs.open('C:\\Users\Tatiana\Documents\GitHub\paradigm_tagging\прилфлексии011117.txt', 'w', 'utf-8')

for line in f:
    if 'flex' in line:
        line = line_healing(line)
    a.write(line)

a.close()
