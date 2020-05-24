import json
import logging
import os
import uuid

from .pcu_user import PCUuser
import config

logger = logging.getLogger(__name__)


class PCUusersDatabase(object):
    USERS_DATABASE_PATH = config.PCU_CONFIG_PATH_USERS
    USERS_DATABASE_USER_FILEEXT = '.json'
    USERS_DATABASE_USER_FILENAME = '{local_id}_{name_id}'

    @property
    def registered_userdata_files(self):
        # TODO: add regex to check and get userdata files
        userdata_files = [os.path.join(self.USERS_DATABASE_PATH, f)
                          for f in os.listdir(self.USERS_DATABASE_PATH)
                          if os.path.splitext(f)[-1] == self.USERS_DATABASE_USER_FILEEXT]
        return userdata_files

    @property
    def registered_userdatas(self):
        userdatas = []
        for userdata_file in self.registered_userdata_files:
            with open(userdata_file) as udf:
                userdatas.append(json.load(udf))
        return userdatas

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

    def register_new_user(self, name_id, name_first, name_last, email):
        local_id = str(uuid.uuid4())
        if self.get_user_from_id(local_id):
            return
        new_userdata = {PCUuser.USERDATA_KEY_IDS: local_id,
                        PCUuser.USERDATA_KEY_NAME_ID: name_id,
                        PCUuser.USERDATA_KEY_NAME_FIRST: name_first,
                        PCUuser.USERDATA_KEY_NAME_LAST: name_last,
                        PCUuser.USERDATA_KEY_EMAIL: email
                        }
        new_pcu_user = PCUuser(new_userdata)
        self.save_user(new_pcu_user)
        return new_pcu_user

    def save_user(self, pcu_user):
        userdata_file_name = '{}{}'.format(self.USERS_DATABASE_USER_FILENAME.format(local_id=pcu_user.local_id,
                                                                                    name_id=pcu_user.name_id),
                                           self.USERS_DATABASE_USER_FILEEXT)
        userdata_file_path = os.path.join(self.USERS_DATABASE_PATH, userdata_file_name)
        with open(userdata_file_path, 'w') as userdata_file:
            # TODO: json formatting
            json.dump(pcu_user.userdata, userdata_file)
