from channel_access_wrapper import ChannelAccessWrapper

if __name__ == '__main__':
        ca = ChannelAccessWrapper(False)
        ca.set_pv_value("ANALOG:SP", 3.3)
        ca.set_pv_value("ON_OFF:SP", True)
        ca.set_pv_value("STRING", "HELLO")
        ca.set_pv_value("PICTURE", bytearray("HELLO"))

        assert ca.get_pv_value("ANALOG") == 3.3
        assert ca.get_pv_value("ON_OFF") == "1"
        assert ca.get_pv_value("STRING") == "HELLO"
        assert ca.get_pv_value("PICTURE") == bytearray("HELLO")