import re
from collections import defaultdict

regex = re.compile(r'\b([A-Z])\b')


def gen_puzzle_input(filename):
    with open(filename, 'rt') as f:
        for line in f:
            yield line.strip()


def iter_pairs(puzzle_input):
    for line in puzzle_input:
        yield regex.findall(line)


def build_structure(pairs):
    deps = defaultdict(set)
    for dep, step in pairs:
        deps[step].add(dep)
        deps[dep]
    return deps


def next_step(deps, remaining, done):
    ready = set()
    for step in remaining:
        if deps[step] <= done:
            ready.add(step)
    if ready:
        return min(ready)


def part1_traverse(deps):
    remaining = set(deps)
    done = set()
    while remaining:
        step = next_step(deps, remaining, done)
        yield step
        done.add(step)
        remaining.remove(step)


if __name__ == '__main__':
    # puzzle_input = gen_puzzle_input('d07_test.txt')
    puzzle_input = gen_puzzle_input('d07.txt')
    pairs = iter_pairs(puzzle_input)
    deps = build_structure(pairs)
    print("".join(part1_traverse(deps)))
