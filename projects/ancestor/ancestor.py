
def earliest_ancestor(ancestors, starting_node):
    nodes={}
    copy = ancestors.copy()
    while len(copy)>0:
        current = copy.pop()
        if not nodes.get(current[1]):
            nodes[current[1]]={
                'key':current[1],
                'distance':None,
                'parent':set()
            }
        nodes.get(current[1]).get('parent').add(current[0])

    if not nodes.get(starting_node):
        return -1

    check=[starting_node]
    while len(check)>0:
        current = nodes.get(check.pop())

        if not current.get('distance'):
            current['distance']=0

        for parent in current.get('parent'):
            if not nodes.get(parent):
                nodes[parent]={
                    'key':parent,
                    'distance':None,
                    'parent':set()
                }
            nodes.get(parent)['distance']=current.get('distance')+1
            check.append(parent)

    largest = (None,0)
    
    for node in nodes.values():
        if node.get('distance') and node.get('distance')>largest[1]:
            largest=(node['key'],node['distance'])
        elif node.get('distance') and node.get('distance')==largest[1] and node.get('key') < largest[0]:
            largest=(node['key'],node['distance'])
    
    return largest[0]
