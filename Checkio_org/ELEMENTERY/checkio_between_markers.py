import re


def between_markers(text: str, begin: str, end: str) -> str:
    match_begin = re.search(r"\%s" % begin, text)
    match_end = re.search(r"\%s" % end, text)
    if match_begin and match_end:
        return text[match_begin.end():match_end.start()]
    elif match_begin:
        return text[match_begin.end():]
    elif match_end:
        return text[:match_end.start()]
    else:
        return text
    # if begin in text and end in text:
    #     return text[text.index(begin) + len(begin):text.index(end)]
    # elif begin in text:
    #     return text[text.index(begin) + len(begin):]
    # elif end in text:
    #     return text[:text.index(end)]
    # else:
    #     return text


if __name__ == '__main__':
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    print('Wow, you are doing pretty good. Time to check it!')
