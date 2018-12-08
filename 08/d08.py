
def gen_puzzle_input(filename):
    with open(filename, 'rt') as f:
        for n in f.read().split():
            yield int(n)


class Node:
    _registry = set()

    def __init__(self, input_numbers):
        self.num_children = next(input_numbers)
        self.num_metadata = next(input_numbers)

        self.children = [Node(input_numbers) for _ in range(self.num_children)]
        self.metadata = [next(input_numbers) for _ in range(self.num_metadata)]

        Node._registry.add(self)

    @property
    def node_value(self):
        if self.num_children == 0:
            return sum(self.metadata)
        else:
            value = 0
            for i in self.metadata:
                try:
                    v = self.children[i-1].node_value
                except IndexError:
                    v = 0
                value += v
            return value


def add_all_metadata_entries():
    total = 0
    for n in Node._registry:
        total += sum(n.metadata)
    return total


if __name__ == '__main__':
    # puzzle_input = gen_puzzle_input('d08_test.txt')
    puzzle_input = gen_puzzle_input('d08.txt')
    root = Node(puzzle_input)
    print(add_all_metadata_entries())
    print(root.node_value)