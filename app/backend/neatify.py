'''This module formats the brainfuck code properly

@author: tdhiraj

'''


def tabs(indent):
    return indent * ' ' * 4


class Neatify(object):
    def format(self, code):
        formatted_code = []
        indent = 0
        prev_ch = ''

        for ch in code:
            if ch == '[':
                formatted_code.append('\n')
                formatted_code.append(tabs(indent) + ch)
                formatted_code.append('\n')
                indent += 1
            elif ch == ']':
                indent -= 1
                formatted_code.append('\n')
                formatted_code.append(tabs(indent) + ch)
                formatted_code.append('\n')
            else:
                if prev_ch in ('[', ']'):
                    formatted_code.append(tabs(indent) + ch)
                else:
                    formatted_code.append(ch)
            prev_ch = ch

        return ''.join(formatted_code)
