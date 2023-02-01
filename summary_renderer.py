from jinja2 import FileSystemLoader, Environment

import parameters


class SummaryRenderer:
    RENDER_DIR = parameters.RENDER_PATH

    def __init__(self, mesh_counts, min_counts, max_counts, table_names):
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("summary_template.html")

        rendered_str = template.render(table_names = table_names, mesh_counts=mesh_counts,
                                       min_counts=min_counts, max_counts=max_counts)
        with open(SummaryRenderer.RENDER_DIR / "summary.html", mode="w", encoding="utf-8") as file:
            file.write(rendered_str)

