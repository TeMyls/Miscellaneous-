local tree = require "n_ary_tree"


tree.edges = {
    [0] = {1, 2},
    [1] = {3, 4},
    [2] = {5},
    [3] = {},
    [4] = {},
    [5] = {}
}

local v = tree:traverse(0, true)
tree:display()
for i = 1, #v do
    print(v[i])
end
print("hiias")
tree:delete_array_index(1)
tree:display()
v = tree:traverse(0, true)
for i = 1, #v do
    print(v[i])
end