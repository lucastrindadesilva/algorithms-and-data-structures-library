from binary_tree import BinaryTree

string_tree = BinaryTree(('A', ['alberto','amelia','augusto','andrea']))
string_tree.insert(('B', ['bob','bianca','bruna','barbara']))
string_tree.insert(('C', ['claudio','cintia']))
string_tree.insert(('D', ['dandara','dalton','diego','deleteria']))
string_tree.insert(('F', ['flavia','flavio','fernanda']))
string_tree.insert(('E', ['edgar','eliana','eudes','elvira']))

print(string_tree.search("E"))
print(string_tree.search('Z'))
print(string_tree)

string_tree2 = BinaryTree(('B', ['bob','bianca','bruna','barbara']))
string_tree2.insert(('A', ['alberto','amelia','augusto','andrea']))
string_tree2.insert(('C', ['claudio','cintia']))
string_tree2.insert(('E', ['edgar','eliana','eudes','elvira']))
string_tree2.insert(('D', ['dandara','dalton','diego','deleteria']))
string_tree2.insert(('F', ['flavia','flavio','fernanda']))
print(string_tree2)

integer_tree = BinaryTree((3,[300,31,369,3501]))
integer_tree.insert((2,[200,2,25]))
integer_tree.insert((5,[54,532,500]))
print(integer_tree.search(10))
integer_tree.insert((1,[1]))
integer_tree.insert((3,[320,357,369845]))
integer_tree.insert((3,[30]))
integer_tree.insert((4,[42,46]))
integer_tree.insert((5,[50,5,500]))
integer_tree.insert((10,[103,105]))
integer_tree.insert((6,[63,654]))
print(integer_tree.search(10))
print(integer_tree)