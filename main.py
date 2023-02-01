import itertools as it
import parameters
from summary_renderer import SummaryRenderer
from table import Table
from table_renderer import TableRenderer


def main():
    count = 0
    tables = []
    mesh_counts = {}
    min_counts = {}
    max_counts = {}

    for table in map(lambda x: Table(set(x)), reversed(list(it.combinations(Table.ALL_CARDS, parameters.HAND_SIZE)))):
        # TODO: filter symmetric hands, if needed
        print(table)
        TableRenderer(table).render()

        tables.append(table.name())
        min_counts[table.name()] = table.min_count
        max_counts[table.name()] = table.max_count
        mesh_counts[table.name()] = table.mesh_count

        count += 1
        # break

    print("--------------------------------------------------")
    print(f"{count} tables generated")

    SummaryRenderer(mesh_counts, min_counts, max_counts, tables)


if __name__ == "__main__":
    main()
