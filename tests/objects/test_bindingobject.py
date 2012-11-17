class TestBindingObject(object):
    def test_simple(self, space):
        w_res = space.execute("return binding.eval('4')")
        assert space.int_w(w_res) == 4

    def test_local(self, space):
        w_res = space.execute("""
        a = 4
        return binding.eval('a + 2')
        """)
        assert space.int_w(w_res) == 6

    def test_in_block(self, space):
        w_res = space.execute("""
        def f(a, b)
            return proc { binding }
        end

        return f(3, 4).call.eval("a + b")
        """)
        assert space.int_w(w_res) == 7
