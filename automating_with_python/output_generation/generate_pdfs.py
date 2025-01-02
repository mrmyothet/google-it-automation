# pip install reportlab

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

fruit = {
    "elderberry": 1,
    "figs": 2,
    "apples": 3,
    "durian": 4,
    "bananas": 5,
    "cherries": 6,
    "grapes": 7,
}

report = SimpleDocTemplate("./temp/fruit_report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])
table_style = [("GRID", (0, 0), (-1, -1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report.build([report_title, report_table])
