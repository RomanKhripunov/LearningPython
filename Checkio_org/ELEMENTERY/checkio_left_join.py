def left_join(phrases):
    return ",".join(phrases).replace("right", "left")


def left_join_2(phrases):
    return ",".join([p.replace("right", "left") if 'right' in p else p for p in phrases])


def left_join_3(phrases):
    return ','.join(map(lambda x: x.replace("right", "left"), phrases))


if __name__ == '__main__':
    import time

    start = time.time()
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    end = time.time()
    print("{:0.7f}".format(end - start))

    start = time.time()
    assert left_join_2(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join_2(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join_2(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join_2(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    end = time.time()
    print("{:0.7f}".format(end - start))

    start = time.time()
    assert left_join_3(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join_3(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join_3(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join_3(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    end = time.time()
    print("{:0.7f}".format(end - start))
