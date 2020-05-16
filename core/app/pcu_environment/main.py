import logging
import os

from .users import PCUusersDatabase

logger = logging.getLogger(__name__)

# --- ENVIRON VARIABLES ---
# context
ENV_KEY_CONTEXT_PROJECT = 'PCU_CONTEXT_PROJECT'
ENV_KEY_CONTEXT_PROJECT_ID = 'PCU_CONTEXT_PROJECT_ID'
ENV_KEY_CONTEXT_ASSET_BUILD = 'PCU_CONTEXT_ASSET_BUILD'
ENV_KEY_CONTEXT_ASSET_BUILD_ID = 'PCU_CONTEXT_ASSET_BUILD_ID'
ENV_KEY_CONTEXT_ASSET_GROUP = 'PCU_CONTEXT_ASSET_GROUP'
ENV_KEY_CONTEXT_ASSET_GROUP_ID = 'PCU_CONTEXT_ASSET_GROUP_ID'
ENV_KEY_CONTEXT_EPISODE = 'PCU_CONTEXT_EPISODE'
ENV_KEY_CONTEXT_EPISODE_ID = 'PCU_CONTEXT_EPISODE_ID'
ENV_KEY_CONTEXT_SEQUENCE = 'PCU_CONTEXT_SEQUENCE'
ENV_KEY_CONTEXT_SEQUENCE_ID = 'PCU_CONTEXT_SEQUENCE_ID'
ENV_KEY_CONTEXT_SHOT = 'PCU_CONTEXT_SHOT'
ENV_KEY_CONTEXT_SHOT_ID = 'PCU_CONTEXT_SHOT_ID'
ENV_KEY_CONTEXT_TASK = 'PCU_CONTEXT_TASK'
ENV_KEY_CONTEXT_TASK_ID = 'PCU_CONTEXT_TASK_ID'
# user
ENV_KEY_USER_NAME_ID = 'PCU_USER_NAME_ID'
ENV_KEY_USER_ID = 'PCU_USER_ID'


# --- CORE ---


def update_environ(user_id=None, task_id=None):
    if user_id:
        update_user(user_id)
    if task_id:
        # TODO: context update
        pass


# --- CONTEXT ---


# TODO: context env management


# --- USER ---


def user(user_id=None):
    pcu_users_database = PCUusersDatabase()
    id_to_use = user_id or os.environ.get(ENV_KEY_USER_ID, None)
    return pcu_users_database.get_user_from_id(id_to_use)


def update_user(user_id):
    pcu_users_database = PCUusersDatabase()
    pcu_user = pcu_users_database.get_user_from_id(user_id)
    if not pcu_user:
        return
    os.environ[ENV_KEY_USER_ID] = pcu_user.local_id
    os.environ[ENV_KEY_USER_NAME_ID] = pcu_user.name_id
    logger.info('New current user: {}'.format(pcu_user.name_full))
    return pcu_user
