from typing import Optional
from grape import Graph
from profiling.benchmark import benchmark
from profiling.task import Task


class GrapeProfile:
    def profile(self, filename: str, n: int, task: Optional[Task] = None):
        print('Library: Grape')
        print(f'Dataset: {filename}')

        if (task is not None):
            # do specific task
            if (task == Task.LOAD):
                benchmark(lambda: self.load(filename), task, n, globals=globals())
                return

            graph = self.load(filename)

            if (task == Task.CONNECTED_COMPONENT):
                benchmark(lambda: self.connected_components(graph), task, n, globals=globals())
                return

            if (task == Task.HARMONIC_CENTRALITY):
                benchmark(lambda: self.harmonic_centrality(graph), task, n, globals=globals())
                return

            print(f'Unknown Task: {task}')
            return

        # do all tasks
        benchmark(lambda: self.load(filename), Task.LOAD, n, globals=globals())
        benchmark(lambda: self.connected_components(graph), Task.CONNECTED_COMPONENT, n, globals=globals())
        benchmark(lambda: self.harmonic_centrality(graph), Task.HARMONIC_CENTRALITY, n, globals=globals())

        graph = self.load(filename)

    def load(self, filename: str):
        graph = Graph.from_csv(
            directed=False,  # directed graph
            edge_path=filename,
            edge_list_comment_symbol='#',
            sources_column_number=0,
            destinations_column_number=1,
            edge_list_separator='	',
            edge_list_header=False,
            verbose=False  # Optional: to show loading progress
        )
        return graph

    def connected_components(self, graph: Graph):
        (
            connected_component_ids_per_node,
            number_of_connected_components,
            smallest_component_size,
            largest_component_size
        ) = graph.get_connected_components()

    def harmonic_centrality(self, graph: Graph):
        graph.get_harmonic_centrality()
