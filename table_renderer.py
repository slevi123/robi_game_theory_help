from jinja2 import Environment, FileSystemLoader

import parameters
from table import Table


class TableRenderer:
    RENDER_DIR = parameters.RENDER_PATH / "tables"

    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("table_template.html")

    def __init__(self, table: Table):
        self.table = table

    def render(self):
        rendered_str = TableRenderer.template.render(table=self.table)
        with open(TableRenderer.RENDER_DIR/f"table{self.table.name()}.html", mode="w", encoding="utf-8") as file:
            file.write(rendered_str)