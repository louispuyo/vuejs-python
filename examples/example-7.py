
from vuejspython import model, start


@model
class Comp:
    # define properties to forward to vue (or not)
    i_name = 'l'
    o_name = 's'
    slice_expr = '5:15'
    is_error = False
    input_expr = str(list(range(40,60)))

    def __init__(self):
        pass

    def computed_input(self):
        try:
            res = eval(self.input_expr)
            if type(res) is list: return res
            return []
        except:
            return []

    def computed_taginput(self):
        return ['%s#%03d'%(str(v), i) for i,v in enumerate(self.input)]

    def computed_tagoutput(self):
        try:
            locals()[self.i_name] = self.input
            locals()['___'+self.i_name] = self.taginput
            res = eval('___%s[%s]'%(self.i_name, self.slice_expr))
            self.is_error = False
            return res
        except Exception as e:
            self.is_error = True
            self.error_message = str(e)
            return []


start(Comp())
