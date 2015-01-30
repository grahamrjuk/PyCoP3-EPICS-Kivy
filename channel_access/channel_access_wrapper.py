TIMEOUT = 15

class ChannelAccessWrapper(object):

    def __init__(self, test_mode=True):
        self.test_mode = test_mode
        self.pvs = dict()
        if not test_mode:
            from ca_channel_imp import CaChannelWrapper
            self.ca_imp = CaChannelWrapper()

    def set_pv_value(self, name, value, wait=False, timeout=TIMEOUT):
        if self.test_mode:
            self.pvs[name] = value
        else:
            self.ca_imp.set_pv_value(name, value, wait, timeout)


    def get_pv_value(self, name, to_string=False, timeout=TIMEOUT):
        if self.test_mode:
            return self.pvs.get(name)
        else:
            return self.ca_imp.get_pv_value(name, to_string, timeout)

    def pv_exists(self, name):
        if self.test_mode:
            if self.pvs.get(name) is None:
                return False
            else:
                return True
        else:
            return self.ca_imp.pv_exists(name)