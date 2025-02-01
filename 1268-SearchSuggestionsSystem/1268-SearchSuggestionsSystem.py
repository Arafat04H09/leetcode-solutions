class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.products = []
        self.isEnd = False

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        root = TrieNode()
        
        for product in products:
            node = root
            for letter in product:
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                if len(node.products) < 3:
                    node.products.append(product)
                node = node.children[letter]
            if len(node.products) < 3:
                node.products.append(product)
            node.isEnd = True
        
        result = []
        node = root
        for letter in searchWord:
            if node and letter in node.children:
                node = node.children[letter]
                result.append(node.products)
            else:
                node = None
                result.append([])
        return result
