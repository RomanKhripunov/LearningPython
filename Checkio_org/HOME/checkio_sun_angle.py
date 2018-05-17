def sun_angle(time):
    splited_time = [int(i) for i in time.split(":")]
    angle = ((splited_time[0] - 6) * 15) + (splited_time[1] * 0.25)
    return angle if 0 <= angle <= 180 else "I don't see the sun!"


if __name__ == '__main__':
    assert sun_angle("07:00") == 15
    assert sun_angle("18:00") == 180
    assert sun_angle("18:01") == "I don't see the sun!"
    assert sun_angle("06:00") == 0
    assert sun_angle("06:15") == 3.75
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
