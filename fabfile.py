from fabric.api import run, put, sudo, env, cd, local, hosts
import os

env.hosts = ['staging.code-on.be']
env.user = 'django'
env.base_dir = '/srv/cloudywatch'
env.project_name = 'cloudywatch'
env.database = 'cloudywatch'
env.project_dir = '{0}/{1}'.format(env.base_dir, env.project_name)


def stage():
    local('git push origin master')
    with cd(env.base_dir):
        run('git pull')
        run('find . -name "*.pyc" -exec rm {} \;')

    with cd(env.project_dir):
        run('./manage.py collectstatic --noinput')

    with cd(env.base_dir):
        run('touch conf/run.wsgi')


def reset():
    with cd(env.project_dir):
        run('./manage.py reset_staging')


@hosts('vitaliy@code-on.be')
def deploy(*args, **kwargs):
    from codeon.utils import fab

    fab.deploy(env, args)
    
    with cd(env.project_dir):
        run('sudo -u www-data ./manage.py collectstatic --noinput')