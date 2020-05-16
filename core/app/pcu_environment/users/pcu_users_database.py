import logging
import os
import uuid

from .pcu_user import PCUuser

logger = logging.getLogger(__name__)


class PCUusersDatabase(object):
    PCU_USER_DATABASE_PATH = ''

    @property
    def registered_userdatas(self):
        # TODO: remove this tmp database and create a real one
        return [{PCUuser.USERDATA_KEY_IDS: '0000',
                 PCUuser.USERDATA_KEY_NAME_ID: 'cmassin',
                 PCUuser.USERDATA_KEY_NAME_FIRST: 'clementin',
                 PCUuser.USERDATA_KEY_NAME_LAST: 'massin'
                 },
                {PCUuser.USERDATA_KEY_IDS: '0001',
                 PCUuser.USERDATA_KEY_NAME_ID: 'tstory',
                 PCUuser.USERDATA_KEY_NAME_FIRST: 'toto',
                 PCUuser.USERDATA_KEY_NAME_LAST: 'story'
                 }
                ]

    @property
    def registered_users(self):
        pcu_users = []
        for usersata in self.registered_userdatas:
            pcu_users.append(PCUuser(usersata))
        return pcu_users

    def get_user_from_id(self, user_id):
        for pcu_user in self.registered_users:
            if user_id in pcu_user.ids:
                return pcu_user

    def is_user_registered(self, user):
        return True if self.get_user_from_id(user.local_id) else False

    def register_new_user(self, name_id, name_first, name_last):
        local_id = str(uuid.uuid4())
        if self.get_user_from_id(local_id):
            return
        new_userdata = {PCUuser.USERDATA_KEY_IDS: local_id,
                        PCUuser.USERDATA_KEY_NAME_ID: name_id,
                        PCUuser.USERDATA_KEY_NAME_FIRST: name_first,
                        PCUuser.USERDATA_KEY_NAME_LAST: name_last
                        }
        new_pcu_user = PCUuser(new_userdata)
        self.save_user(new_pcu_user)
        return new_pcu_user

    @staticmethod
    def save_user(pcu_user):
        # TODO: saving user
        userdata = pcu_user.userdata
        logger.info('------ userdata saved: {}'.format(userdata))
