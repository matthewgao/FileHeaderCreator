import sublime, sublime_plugin
import datetime

class FileHeaderCreatorCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        # print(self.view.settings().get("author"))
        if self.view.size() == 0:
            self.check_file_type(edit)

    def check_file_type(self, edit):
        file_path = self.view.file_name()
        pos = file_path.rfind('.')
        if pos == -1:
            return
        suffix = file_path[pos+1:]

        token = '/'
        if sublime.platform() == 'windows':
            token = '\\'
        file_name_pos = file_path.rfind(token)
        if file_name_pos == -1:
            return
        file_name = file_path[file_name_pos+1:]

        header = ''
        if suffix == 'py':
            header = self._python(file_name)
        elif suffix == 'cpp':
            header = self._cpp(file_name)
        elif suffix == 'h':
            header = self._h(file_name)
        elif suffix == 'hs':
            header = self._haskell(file_name)

        self.view.insert(edit, 0, header)

    def _h(self, name):
        string = "/*\n"
        string += " * " + name + "\n"
        string += " * Created By: " + self.view.settings().get("author") + "\n"
        string += " * " + self.view.settings().get("company") + "\n"
        string += " * Created Time: " + datetime.date.today().isoformat() + "\n"
        string += " */\n"
        string += "#ifndef _" + name.replace('.', '_').upper() + "\n"
        string += "#define _" + name.replace('.', '_').upper() + "\n\n\n"
        string += "#endif"
        return string
    
    def _python(self, name):
        string = "#!/usr/bin/env python3\n"
        string += "# coding=utf-8\n"
        string += "# Created Time: " + datetime.date.today().isoformat() + "\n\n"
        string += "__author__ = " + "\'" + self.view.settings().get("author") + "\'"
        
        return string

    def _cpp(self, name):
        string = "/*\n"
        string += " * " + name + "\n"
        string += " * Created By: " + self.view.settings().get("author") + "\n"
        string += " * " + self.view.settings().get("company") + "\n"
        string += " * Created Time: " + datetime.date.today().isoformat() + "\n"
        string += " */\n"
        return string

    def _haskell(self, name):
        pass


class FileHeaderCreator(sublime_plugin.EventListener):
    def on_load(self, view):
        print("FileHeaderCreator on_load invoked")
        view.run_command("file_header_creator")

    def on_post_save(self, view):
        print("FileHeaderCreator on_post_save invoked")
        view.run_command("file_header_creator")

