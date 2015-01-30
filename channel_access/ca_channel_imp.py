from CaChannel import ca, CaChannel

TIMEOUT = 1
CACHE = dict()

MYPVPREFIX = "NDLT702:ffv81422:TEST_01"

class CaChannelWrapper(object):

    def _waveform2string(self, data):
        output = ""
        for i in data:
            if i == 0:
                break
            output += str(unichr(i))
        return output

    def set_pv_value(self, name, value, wait=False, timeout=TIMEOUT):
        """Set the PV to a value.
           When getting a PV value this call should be used, unless there is a special requirement.

        Parameters:
            name - the PV name
            value - the value to set
            wait - wait for the value to be set before returning
        """
        name = MYPVPREFIX + ':' + name
        if name not in CACHE.keys():
            chan = CaChannel(name)
            chan.setTimeout(TIMEOUT)
            #Try to connect - throws if cannot
            chan.searchw()
            CACHE[name] = chan
        else:
            chan = CACHE[name]
        if wait:
            chan.putw(value)
        else:
            def putCB(epics_args, user_args):
                #Do nothing in the callback
                pass
            ftype = chan.field_type()
            ecount = chan.element_count()
            chan.array_put_callback(value, ftype, ecount, putCB)
            chan.flush_io()


    def get_pv_value(self, name, to_string=False, timeout=TIMEOUT):
        """Get the current value of the PV"""
        name = MYPVPREFIX + ':' + name

        if name not in CACHE.keys():
            chan = CaChannel(name)
            chan.setTimeout(TIMEOUT)
            #Try to connect - throws if cannot
            chan.searchw()
            CACHE[name] = chan
        else:
            chan = CACHE[name]
        ftype = chan.field_type()
        if ca.dbr_type_is_ENUM(ftype) or ca.dbr_type_is_CHAR(ftype) or ca.dbr_type_is_STRING(ftype):
            to_string = True
        if to_string:
            if ca.dbr_type_is_ENUM(ftype):
                value = chan.getw(ca.DBR_STRING)
            else:
                value = chan.getw(ca.DBR_CHAR)
            #Could see if the element count is > 1 instead
            if isinstance(value, list):
                return self._waveform2string(value)
            else:
                return str(value)
        else:
            return chan.getw()

    def pv_exists(self, name):
        """See if the PV exists"""
        name = MYPVPREFIX + ':' + name
        try:
            chan = CaChannel(name)
            #Try to connect - throws if cannot
            chan.searchw()
            return True
        except:
            return False