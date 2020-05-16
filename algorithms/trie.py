
def contacts_old(queries):
    output = []
    saved = []
    for query in queries:
        if query[0] == 'add':
            saved.append(query[1])
        elif query[0] == 'find':
            occurences = [i for i in saved if query[1] in i]
            output.append(len(occurences))

    return output


def contacts(queries):
    trie = Trie()
    output = []
    for query in queries:
        if query[0] == 'add':
            trie.insert(query[1])
        elif query[0] == 'find':
            occurences = trie.get_all_with_prefix(query[1])
            output.append(occurences)

    return output


class Node:
    """Node for Python Trie Implementation"""
    def __init__(self):
        self.word = None
        self.nodes = {}  # dict of nodes

    def get_all(self):
        occurrence = []
        for key, node in self.nodes.items():
            if node.word is not None:
                occurrence.append(node.word)
            occurrence += node.get_all()
        return occurrence

    def __str__(self):
        return self.word

    def insert(self, word, string_pos=0):
        """Add a word to the node in a Trie"""
        current_letter = word[string_pos]

        # Create the Node if it does not already exist
        if not self.nodes.get(current_letter):
            self.nodes[current_letter] = Node()

        next_pos = string_pos + 1
        if next_pos == len(word):
            self.nodes[current_letter].word = word
        else:
            self.nodes[current_letter].insert(word, next_pos)

        return True

    def get_all_with_prefix(self, prefix, string_pos):
        occurrence = 0

        for key, node in self.nodes.items():
            if node.word and node.word.startswith(prefix):
                occurrence += 1

            if node.nodes:
                string_pos += 1

            occurrence += node.get_all_with_prefix(prefix, string_pos)
        return occurrence


class Trie:
    """Trie Python Implementation"""

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        self.root.insert(word)

    def get_all(self):
        return self.root.get_all()

    def get_all_with_prefix(self, prefix, string_pos=0):
        return self.root.get_all_with_prefix(prefix, string_pos)


if __name__ == "__main__":
    s = [['add', 'alini'], ['add', 'ali'], ['add', 'ribeiro'], ['find', 'ali'], ['find', 'rib']]
    # s = [['add', 's'],
    #      ['add', 'ss'],
    #      ['add', 'sss'],
    #      ['add', 'ssss'],
    #      ['add', 'sssss'],
    #      ['find', 's'],
    #      ['find', 'ss'],
    #      ['find', 'sss'],
    #      ['find', 'ssss'],
    #      ['find', 'sssss'],
    #      ['find', 'ssssss']
    #      ]

    # s = [['add', 'eouecvksgllpvfxfvndu'],
    #      ['find', 'zivh'],
    #      ['add', 'uugxgcrtujxzyjysqrhu'],
    #      ['find', 'of'],
    #      ['add', 'ryhlozedmgzcmjdfjhte'],
    #      ['find', 'uqaqv'],
    #      ['add', 'ibfzenldsdltkjbbsccq'],
    #      ['find', 'bmcop'],
    #      ['add', 'vvxwlttswneoosvgfezt'],
    #      ['find', 've'],
    #      ['add', 'qimoqjtjypqupwwrueew'],
    #      ['find', 'ccyc'],
    #      ['add', 'nkaetboylnjbxxvhzupk'],
    #      ['find', 'lre'],
    #      ['add', 'rdzddgjryupsyhhbjtmx'],
    #      ['find', 'hhn'],
    #      ['add', 'kudnlccqbvkizsfdbwxy'],
    #      ['find', 'yyr']]


    pr = contacts(s)
    print(f">>>>>{pr}")