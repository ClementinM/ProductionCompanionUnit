import logging

logger = logging.getLogger(__name__)


class PCUuser(object):
    USERDATA_KEY_IDS = 'ids'
    USERDATA_KEY_IDS_SEP = ','
    USERDATA_KEY_NAME_ID = 'name_id'
    USERDATA_KEY_NAME_FIRST = 'name_first'
    USERDATA_KEY_NAME_LAST = 'name_last'
    USERDATA_KEY_EMAIL = 'email'
    USERDATA_KEY_PREFERENCES = 'preferences'

    def __init__(self, userdata):
        self.userdata = userdata
        self.ids = self.userdata[self.USERDATA_KEY_IDS].split(self.USERDATA_KEY_IDS_SEP)
        self.local_id = self.ids[0]
        self.name_id = self.userdata[self.USERDATA_KEY_NAME_ID]
        self.name_first = self.userdata[self.USERDATA_KEY_NAME_FIRST]
        self.name_last = self.userdata[self.USERDATA_KEY_NAME_LAST]
        self.preferences = self.userdata[self.USERDATA_KEY_PREFERENCES]

    @property
    def name_full(self):
        if not (self.name_first and self.name_last):
            return
        return '{} {}'.format(self.name_first, self.name_last)
