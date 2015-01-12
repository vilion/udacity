# -*- coding:utf-8 -*-

#
# Finish the delta debug function ddmin
#


import re
def remove_html_markup(s):
    tag   = False
    quote = False
    out   = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
    
    assert out.find("<") == -1

    return out


def test(s):
    print s, len(s)
    try:
        remove_html_markup(s)
        return "PASS"
    except:
        return "FAIL"
    # print s, len(s)
    # if re.search("<SELECT[^>]*>", s) >= 0:
    #     return "FAIL"
    # else:
    #     return "PASS"


def ddmin(s):
    assert test(s) == "FAIL"

    n = 2
    while len(s) >= 2:
        subset_len = len(s) / n
        start = 0
        is_any_complement_fail = False

        while start < len(s):
            complement = s[:start] + s[start + subset_len:]
            result = test(complement)
            is_any_complement_fail = result == "FAIL"

            if is_any_complement_fail:
                s = complement
                n = max(n - 1, 2)
                break

            start += subset_len

        if not is_any_complement_fail:
            if n == len(s):
                break
            n = min(n * 2, len(s))

    return s



# UNCOMMENT TO TEST
# html_input = '<SELECT>foo</SELECT>'
html_input = '"<b>foo</b>"'
print ddmin(html_input) # expected "<
# print remove_html_markup(html_input)
