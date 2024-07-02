from typing import Optional
from networkx import DiGraph, Graph, read_edgelist, strongly_connected_components, harmonic_centrality as nx_harmonic_centrality
from profiling.benchmark import benchmark
from profiling.task import Task


class NetworkxProfile:
    def profile(self, filename, n, task: Optional[Task] = None):
        print('Library: Networkx')
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
        graph = self.load(filename)

        benchmark(lambda: self.load(filename), Task.LOAD, n, globals=globals())
        benchmark(lambda: self.connected_components(graph), Task.CONNECTED_COMPONENT, n, globals=globals())
        benchmark(lambda: self.harmonic_centrality(graph), Task.HARMONIC_CENTRALITY, n, globals=globals())

    def load(self, filename: str):
        graph = read_edgelist(filename, delimiter="\t", nodetype=int, create_using=Graph())
        return graph

    def load_directed(self, filename: str):
        graph = read_edgelist(filename, delimiter="\t", nodetype=int, create_using=DiGraph())
        return graph

    def connected_components(self, graph: Graph):
        [i for i in strongly_connected_components(graph)]

    def harmonic_centrality(self, graph: Graph):
        nx_harmonic_centrality(graph)
