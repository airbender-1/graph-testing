from pprint import pprint
from grape import Graph, GraphBuilder  # , GraphVisualizer
import timeit
from pathlib import Path


def fix_numpy_2():
    import numpy as np
    np.float_ = np.float64
    np.string_ = np.bytes_


def build_graph() -> Graph:
    builder = GraphBuilder()

    builder.set_name("English")
    builder.set_directed(True)

    builder.add_node("Jane", ["NOUN"])
    builder.add_node("dragon", ["NOUN"])

    builder.add_edge("Jane", "dragon", "mother of")

    graph = builder.build()

    graph.dump_nodes("English_nodes.tsv")
    graph.dump_edges("English_edges.tsv")

    return graph

    # # pprint(dir(graph))
    # x = GraphVisualizer(graph)
    # # x.plot_dot()
    # x.plot_nodes()


def loadCsvGraph(file_path: str) -> Graph:
    graph = Graph.from_csv(
        directed=True,  # directed graph
        edge_path=file_path,
        edge_list_comment_symbol='#',
        sources_column_number=0,
        destinations_column_number=1,
        edge_list_separator='	',
        edge_list_header=False,
        verbose=True  # Optional: to show loading progress
    )
    return graph


def save_to_html_file(content, filename):
    if (not filename):
        raise ValueError("Missing required argument: filename")

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{filename}</title>
</head>
<body>
{content}
</body>
</html>
"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_template)

    pprint(f"Saved to {filename}")


def run():
    pprint("Ready !")
    # fix_numpy_2()

    # graph = build_graph()

    data_folder = "./graph-testing-data"
    # file_path = f"{data_folder}/google.txt"
    # file_path = f"{data_folder}/amazon.txt"
    file_path = f"{data_folder}/English_edges.tsv"

    # time = timeit.timeit(lambda: loadCsvGraph(file_path), number=1)
    # pprint(f'Loading {file_path} takes {time} sec')

    graph = loadCsvGraph(file_path)

    file_name = Path(file_path).stem  # file name without extension
    save_to_html_file(graph.__str__(), f'./output/{file_name}.html')

    # pprint(graph)

    # from grape.datasets.string import HomoSapiens
    # homo_sapiens = HomoSapiens()

    # from grape.datasets.kgobo import HP
    # hpo = HP(version="2022-10-05")

    # # with open("hbo.html", "+w") as f:
    # #     print(hpo, file=f)
    # from grape.datasets.kgobo import MP
    # mpo = MP(version="2021-11-04")

    # # # hp_or_mp = hpo | mpo
    # hp2 = hpo & mpo

    # print(hp2)
    # # print(hp_or_mp)

    # from grape.datasets.kghub import KGCOVID19
    # kgcovid19 = KGCOVID19()

    # kgcovid19_and_hp_or_mp = kgcovid19 & hp_or_mp
    # s = kgcovid19_and_hp_or_mp.size()

    # print(s)
