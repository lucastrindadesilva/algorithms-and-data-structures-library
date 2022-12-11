from binary_tree import BinaryTree

item = ('A', ['alberto','amelia','augusto','andrea'])
string_tree = BinaryTree(item)

item = ('B', ['bob','bianca','bruna','barbara'])
string_tree.insert(item)

item = ('C', ['claudio','cintia'])
string_tree.insert(item)

item = ('D', ['dandara','dalton','diego','deleteria'])
string_tree.insert(item)

item = ('F', ['flavia','flavio','fernanda'])
string_tree.insert(item)

item = ('E', ['edgar','eliana','eudes','elvira'])
string_tree.insert(item)

print(string_tree.search("E"))
print(string_tree.search('Z'))
print(string_tree)

string_tree2 = BinaryTree('B')
string_tree2.insert('A')
string_tree2.insert('C')
string_tree2.insert('E')
string_tree2.insert('D')
string_tree2.insert('F')
print(string_tree2)

integer_tree = BinaryTree(3)
integer_tree.insert(2)
integer_tree.insert(5)
print(integer_tree.search(10))
integer_tree.insert(1)
integer_tree.insert(3)
integer_tree.insert(3)
integer_tree.insert(4)
integer_tree.insert(5)
integer_tree.insert(10)
integer_tree.insert(6)
print(integer_tree.search(10))
print(integer_tree)