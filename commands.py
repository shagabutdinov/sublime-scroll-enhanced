import sublime
import sublime_plugin

class ScrollLinesEnhanced(sublime_plugin.TextCommand):
  def run(self, edit, amount = 0, horizontal_amount = 0, overheight = True):
    col, row = self.view.viewport_position()
    line_height = self.view.line_height()
    column_width = self.view.em_width()

    row += amount * line_height
    lines_count, _ = self.view.rowcol(self.view.size())

    max_height = lines_count * line_height
    if not overheight:
      _, height = self.view.viewport_extent()
      max_height -= height

    if row > max_height:
      row = max_height

    if row < 0:
      row = 0

    col += horizontal_amount * column_width
    viewport_width, _ =self.view.viewport_extent()
    layout_width, _ =self.view.layout_extent()
    max_width = layout_width - viewport_width

    if col > max_width:
      col = max_width

    if col < 0:
      col = 0

    self.view.set_viewport_position([col, row])
