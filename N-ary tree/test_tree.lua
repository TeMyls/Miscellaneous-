--local tree = require "n_ary_tree"
local tree = require "adjacency_matrix"

--[[
tree.edges = {
    [0] = {1, 2},
    [1] = {3, 4},
    [2] = {5},
    [3] = {},
    [4] = {},
    [5] = {}
}
]]
tree:input_indexes( 
    {
        
        [1] = {2, 4},
        [2] = {3},
        [3] = {4, 5},
        [4] = {},
        [5] = {}
    }
)

tree:display()
local v = tree:traverse(1, true)

for i = 1, #v do
    print(v[i])
end
tree:add_node()
tree:display()
tree:add_node()
tree:display()
tree:remove_node(2)
tree:display()
print("hiias")
