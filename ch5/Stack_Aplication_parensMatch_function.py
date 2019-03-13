def check_parens(text):
    parens = '()[]{}'
    open_parens = '([{'
    opposite = {')': '(', ']': '[', '}': '{'}

    # 开括号入栈
    def parentheses(text):
        i, text_len = 0, len(text)
        while (True):
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = sstack()  # 保存括号的栈 这里使用的顺序表形式的栈
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print('Unmatching is found at ', i, ' for ', pr)
            return False
        # else: 这次匹配成功什么也不做
    print('All parentheses are correctly matched!')
    return True
'''
# 测试
text = 'afa(aklfa{afjha[Lalk;fka;f]alkfaf[afalla]})'
check_parens(text)
'''
