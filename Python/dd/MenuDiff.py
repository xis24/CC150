class Node:
    def __init__(self, key, value, active) -> None:
        self.key = key
        self.value = value
        self.active = active
        self.children = []

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Node):
            return self.key == __o.key and self.value == __o.value and self.active == __o.active


class MenuDiff:
    '''
    At DoorDash, menus are updated daily even hourly to keep them up-to-date. Each menu can be regarded as a tree. A menu can have many categories; each category can have many menu_items; each menu_item can have many item_extras; An item_extra can have many item_extra_options…
    class Node {
        String key;
        int value;
        boolean active;
        List<Node> children;
    }

    We will compare the new menu sent from the merchant with our existing menu. Each item can be considered as a node in the tree. The definition of a node is defined above. Either value change or the active status change means the node has been changed. There are times when the new menu tree structure is different from existing trees, which means some nodes are set to null. In this case, we only do soft delete for any nodes in the menu. If that node or its sub-children are null, we will treat them ALL as inactive. There are no duplicate nodes with the same key.
    Return the number of changed nodes in the tree.

        Existing tree                                        
         a(1, T)                                                
        /       \                                                          
     b(2, T)   c(3, T)                                               
    /     \           \                                                        
d(4, T) e(5, T)   f(6, T)                                               

        New tree 
        a(1, T)
            \
           c(3, F)
               \
               f(66, T)

    5 changed nodes
    '''

    def getModifiedItems(self, oldMenu, newMenu):
        if not oldMenu and not newMenu:
            return 0
        count = 0
        if not oldMenu or not newMenu or oldMenu != newMenu:
            count += 1

        oldChildren = self.getChildNodes(oldMenu)
        newChildren = self.getChildNodes(newMenu)

        for key in oldChildren.keys():
            count += self.getModifiedItems(oldChildren.get(key),
                                           newChildren.get(key, None))

        for key in newChildren.keys():
            if key not in oldChildren:
                count += self.getModifiedItems(None, newChildren.get(key))
        return count

    def getChildNodes(self, menu):
        map = {}
        if not menu:
            return map
        for node in menu.children:
            map[node.key] = node
        return map


if __name__ == '__main__':
    '''
    /*
         Existing tree
            a(1, T)
          /         \
        b(2, T)   c(3, T)
      /       \
  d(4, T) e(5, T)

                New tree
                a(1, T)
             /          \
       b(2, T)         c(3, T)
      /                   \
 d(4, T)                   e(5, T)

 */
    '''
    a = Node("a", 1, True)
    b = Node("b", 2, True)
    c = Node("c", 3, True)
    d = Node("d", 4, True)
    e = Node("e", 5, True)

    a.children.append(b)
    a.children.append(c)
    b.children.append(d)
    b.children.append(e)

    a1 = Node("a", 1, True)
    b1 = Node("b", 2, True)
    c1 = Node("c", 3, True)
    d1 = Node("d", 4, True)
    e1 = Node("e", 5, True)

    a1.children.append(b1)
    a1.children.append(c1)
    b1.children.append(d1)
    c1.children.append(e1)

    obj = MenuDiff()
    print(obj.getModifiedItems(a, a1))
