
import asyncio
import vuejspython


@vuejspython.model
class Comp:
    # define properties to forward to vue (synchronized state)
    suggestions = ['+1', 'ToTo']
    title = 'Test1'
    i = 42
    i2_withwatch = -1
    subtitle = 'very local'
    _v_novue = ['subtitle'] # property names to exclude from the synchronized state

    def __init__(self):
        self.i = 10
        # just for the example, starts a loop that increments every few seconds
        asyncio.ensure_future(self.demo_incr(1, 2))

    def watch_i(self, i):
        print("TEST: UPDATING i2_withwatch")
        self.i2_withwatch = i*i

    def computed_i2(self):
        print("TEST: COMPUTING i2")
        return self.i**2

    async def demo_incr(self, t, v):
        while True:
            await asyncio.sleep(t)
            self.i += v

    def meth1(self, v):
        print("TEST: COMMAND", v)
        self.subtitle = "Changed: "+v # will not trigger change as _novue
        if v == '+1':
            self.i += 1

    async def meth2(self, v):
        await asyncio.sleep(1)
        return str(v[::-1])

    def meth3(self, v):
        return str(v[::-1])

    def clone(self, v):
        print("TEST: CLONE", type(self.suggestions))
        self.suggestions += [v]

vuejspython.start(Comp())
