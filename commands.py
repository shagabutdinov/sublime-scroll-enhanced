import sublime
import sublime_plugin

class ScrollLinesEnhanced(sublime_plugin.TextCommand):
  def run(self, edit, amount, overheight = True):
    col, row = self.view.viewport_position()
    line_height = self.view.line_height()

    row += amount * line_height
    lines_count, _ = self.view.rowcol(self.view.size())

    max = lines_count * line_height
    if not overheight:
      _, height = self.view.viewport_extent()
      max -= height

    if row > max:
      row = max

    if row < 0:
      row = 0

    self.view.set_viewport_position([col, row])