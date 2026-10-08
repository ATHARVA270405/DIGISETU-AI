from digisetu.orchestration.graph import build_graph


graph = build_graph()

initial_state = {}

result = graph.invoke(initial_state)

print("\nFinal State:")
print(result)