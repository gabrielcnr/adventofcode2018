from collections import Counter

def part1():
    lines = open('input_02.txt', 'rt')
    counters = (Counter(line.strip()) for line in lines if line.strip())
    counter_of_counts = (Counter(counter.values()) for counter in counters)

    d = {2: 0, 3: 0}

    for counter in counter_of_counts:
        c2 = counter.get(2, 0)
        c3 = counter.get(3, 0)

        if c2 == 0:
            if c3:
                d[3] += 1

        elif c3 == 0:
            if c2:
                d[2] += 1

        else:
            d[2] += c2
            d[3] += c3


    print('2: ', d[2])
    print('3: ', d[3])
    print('checksum: ', d[2] * d[3])


def part2():
    lines = [l.strip() for l in open('input_02.txt', 'rt')]
    for i, line in enumerate(lines):
        for other_line in lines[i+1:]:
            count = 0
            diff_pos = -1
            for pos, (ch1, ch2) in enumerate(zip(line, other_line)):
                if ch1 != ch2:
                    count += 1
                    diff_pos = pos
                if count > 1:
                    break
            if count == 1:
                for j, ch in enumerate(line):
                    if j == diff_pos:
                        continue
                    yield ch
                return


if __name__ == '__main__':
    print(''.join(part2()))