
#Funkcje z zajec nr3 potrzebne dalej
def ConnectedComponents(graph):
  """
  Znajduje spójne składowe w grafie nieskierowanym
  Jako wynik zwraca listę zbiorów wierzchołków
  Uwaga: pierwszym elementem zwracanej listy jest zbiór wszystkich wierzchołków grafu
  """
  def DFS(v):
    """
    Przeszukiwanie grafu w głąb
    """
    for u in graph[v]:
      if not u in VT[0]:    # u - jeszcze nie odwiedzony
        VT[0].add(u)        # u - już odwiedzony
        VT[-1].add(u)       # u - w ostatniej spójnej składowej
        DFS(u)

  """
  VT - lista zbiorów VT[i] dla i > 0 zbiór elementów i-tej spójnej składowej
  VT[0] = union_{i > 0} VT[i] - docelowo - zbiór wszystkich wierzchołków grafu
  """
  VT = [set([])]
  for v in graph:
    if not v in VT[0]:
      VT[0].add(v)
      VT.append(set([v])) # zaczątek nowej, spójnej składowej
      DFS(v)
  return VT
def ConnectedComponentsGraphs(graph):
  """
  Zwraca spójne składowe grafu w formie listy grafów
  """
  VT = ConnectedComponents(graph)
  print("Liczba spójnych składowych: ", len(VT) - 1)

  # Każdą spójną składową przepisujemy jako graf
  components = []
  for vt in VT[1:]:
    comp = {}
    for v in vt:
      comp[v] = graph[v].copy()
    components.append(comp)
  return components




def graph_to_edges(graph, filename):
    edges_list = ''
    used = []
    for v in graph:
        if not graph[v]:
            edges_list += f'{v}\n'
        for u in graph[v]:
            if u not in used:
                edges_list += f'{v} {u}\n'
        used.append(v)
    f = open(filename, 'w')
    f.write(edges_list)
    f.close()

#dla grafu skierowanego odwracamy strzałki
def transpose_graph(graph):
    graph_transposed = {key: [] for key in graph}
    for v in graph:
        for u in graph[v]:
            graph_transposed[u].append(v)
    return graph_transposed



#Przeszukujemy graf wglab i kolorujemy odwiedzone wierzcholki
def DFSsort(graph, v, S, colours):
    if colours[v] == 'red':
        print('graf ma cykl')
        return False
    if colours[v] == 'green':
        return True
    colours[v] = 'red'
    for u in graph[v]:
        if not DFSsort(graph, u, S, colours):
            return False
    colours[v] = 'green'
    S.append(v)
    return True


def strongly_connected_components(graph, order):
    order.reverse() #reverse() odwraca kolejnosc posortowanych elementow
    graph_transposed = transpose_graph(graph)
    graph_ordered = {key: graph_transposed[key] for key in order}
    return connected_componentsBFS(graph_ordered)


def connected_componentsBFS(graph):
    def BFS(v):
        queue.append(v)
        while len(queue) > 0:
            v = queue.pop(0)
            VT[-1].add(v)
            for u in graph[v]:
                if u in VT[0]:
                    continue
                queue.append(u)
                VT[0].add(u)

    VT = [set([])]
    queue = []
    for v in graph:
        if v not in VT[0]:
            VT[0].add(v)
            VT.append({v})
            BFS(v)
    return VT

#Zadanie 3
#Uwaga - zwraca liste elementow topologicznie od najwiekszego do najmniejszego
def TopologicalSort(graph):
    colours = {key: 'white' for key in graph}
    S = []
    for v in graph:
        if not colours[v] == 'white':
            continue
        if not DFSsort(graph, v, S, colours):
            return S
    components = strongly_connected_components(graph, S.copy())[1:]
    if len(components) == len(graph):
        print('Kolejność jest porządkiem topologicznym')
    else:
        print('Brak porządku topologicznego')
    return S





#funckje do tworzenia grafow
def add_vertex(graph, vertex):
    """Nowy wierzchołek do istniejącego grafu"""
    if vertex not in graph:
      graph[vertex] = []


def add_arc(graph, arc):
  """Dodaje nowy łuk (parę wierzchołków) do istniejącego grafu
     rozważamy grafy proste, skierowane
  """
  u, v = arc
  add_vertex(graph, u)
  add_vertex(graph, v)
  if v not in graph[u]:
    graph[u].append(v)
# testy dla TopologicalSort

#Tutaj wymyslony graf bez cyklu
tree = {}
add_arc(tree, (1, 2))
add_arc(tree, (4, 5))
add_arc(tree, (1, 3))
add_arc(tree, (3, 4))
add_arc(tree, (3, 5))
# print(tree)
print(TopologicalSort(tree))


#tutaj dorobilem petle z 5 do 1
tree2 = {}
add_arc(tree2, (1, 2))
add_arc(tree2, (4, 5))
add_arc(tree2, (1, 3))
add_arc(tree2, (3, 4))
add_arc(tree2, (3, 5))
add_arc(tree2, (5, 1))
# print(tree)
print(TopologicalSort(tree2))
