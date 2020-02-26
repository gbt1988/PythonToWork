import re, pyperclip

def re_strip(s, t='\\s'):
    tb_format = '^' + t + '+'
    tt_format = t + '+' + '$'
    sb_re = re.compile(tb_format)
    st_re = re.compile(tt_format)
    s = sb_re.sub('', s)
    s = st_re.sub('', s)
    return s

print(re_strip('aaaafaaaa', 'a'))
print(re_strip('    f    '))
###########################################################

# 根据建议优化的版本：
import re

def re_strip(s, t=r'\s'):
    t_format = r'^%s*|%s*$' % (t, t)
    s_re = re.compile(t_format)
    s = s_re.sub('', s)
    return s

print(re_strip('aaaafaaaa', 'a'))
print(re_strip('    f    '))
