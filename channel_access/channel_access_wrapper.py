class CaChannelWrapper(object):

    def __init__(self, test_mode=True):
        self.test_mode = test_mode
        self.pvs = dict()

    def set_pv_value(self, name, value, wait=False, timeout=TIMEOUT):
        if self.test_mode:
            self.pvs[name] = value

    def get_pv_value(self, name, to_string=False, timeout=TIMEOUT):
        if self.test_mode:
            return self.pvs.get(name)

    def pv_exists(self, name):
        if self.test_mode:
            if self.pvs.get(name) is None:
                return False
            else:
                return True