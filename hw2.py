import data
from data import Point, Duration
from data import Rectangle

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1:Point, p2:Point) -> Rectangle:
    if p1.y<p2.y:
        p1.y, p2.y = p2.y, p1.y
    return Rectangle(p1, p2)

# Part 2
def shorter_duration_than(dur1:Duration, dur2:Duration) -> bool:
    if dur1.minutes>dur2.minutes:
        return False
    elif dur1.minutes<dur2.minutes:
        return True
    else:
        if dur1.seconds > dur2.seconds:
            return False
        elif dur1.seconds < dur2.seconds:
            return True

# Part 3
def songs_shorter_than(lst, dur:Duration):
    return [x for x in lst if shorter_duration_than(x.duration, dur)]

# Part 4
def running_time(songs, ints):
    dur = Duration(0,0)
    for x in ints:
        dur.minutes += songs[x].duration.minutes
        dur.seconds += songs[x].duration.seconds
    dur.minutes += dur.seconds//60
    dur.seconds = dur.seconds%60
    return dur

# Part 5
def validate_route(clist, route):
    count = 0
    for x in clist:
        if route[count] in x:
            if route[count+1] in x:
                count+=1
                if (count)==len(route)-1: return True
    return False

# Part 6
def longest_repetition(numbers):
    if not numbers:
        return None
    max_len = current_len = 1
    max_index = current_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_index = current_index
            current_len = 1
            current_index = i
    if current_len > max_len:
        max_len = current_len
        max_index = current_index
    return max_index