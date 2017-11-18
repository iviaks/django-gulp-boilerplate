import os
import json
import sys
import yaml
import re
import shutil


def make_frontend(project_name, *args, **kwargs):
    json_file = {}
    project_name += '-frontend'

    with open(os.path.join('.', 'frontend', 'package.json'), 'r+') as file:
        json_file = json.load(file)
        json_file['name'] = project_name
        file.seek(0)
        file.write(json.dumps(json_file, indent=2))


def make_changes_in_file(file, old, new):
    lines = "".join(file.readlines())
    lines = re.sub(old, new, lines)
    file.seek(0)
    file.write(lines)


def make_backend(project_name, *args, **kwargs):
    old_project_name = 'src'

    with open(os.path.join('.', 'backend', 'manage.py'), 'r+') as file:
        make_changes_in_file(file, old_project_name, project_name)

    with open(os.path.join(
        '.', 'backend', old_project_name, 'settings', 'common.py'
    ), 'r+') as file:
        make_changes_in_file(file, old_project_name, project_name)

    with open(os.path.join(
        '.', 'backend', old_project_name, 'settings', 'development.py'
    ), 'r+') as file:
        make_changes_in_file(file, old_project_name, project_name)

    with open(os.path.join(
        '.', 'backend', old_project_name, 'settings', 'production.py'
    ), 'r+') as file:
        make_changes_in_file(file, old_project_name, project_name)

    with open(os.path.join(
        '.', 'backend', old_project_name, 'wsgi.py'
    ), 'r+') as file:
        make_changes_in_file(file, old_project_name, project_name)

    with open(os.path.join('.', '.env.example'), 'r+') as file:
        make_changes_in_file(file, old_project_name, project_name)

    with open(os.path.join('.', 'initial.sql'), 'r+') as file:
        make_changes_in_file(file, old_project_name, project_name)

    shutil.move(
        os.path.join('.', 'backend', old_project_name),
        os.path.join('.', 'backend', project_name)
    )


def make_docker(project_name, *args, **kwargs):
    yaml_file = {}
    names = {}
    sys.stdout.write('All docker container names must be unique\n')
    names['backend'] = raw_input(
        'Docker backend container name (default: docker-backend): '
    ) or 'docker-backend'
    names['database'] = raw_input(
        'Docker database container name (default: docker-database): '
    ) or 'docker-database'
    names['frontend'] = raw_input(
        'Docker frontend container name (default: docker-frontend): '
    ) or 'docker-frontend'
    names['jupyter'] = raw_input(
        'Docker Jupyter container name (default: docker-jupyter): '
    ) or 'docker-jupyter'

    if len(set(names.values())) != len(names.values()):
        sys.exit('All docker container names must be unique')

    with open(os.path.join('.', 'docker-compose.yml'), 'r') as file:
        yaml_file = yaml.load(file)

    backend = yaml_file['services']['backend']
    database = yaml_file['services']['database']
    frontend = yaml_file['services']['frontend']
    jupyter = yaml_file['services']['jupyter']

    backend['container_name'] = names['backend']
    backend['working_dir'] = backend['working_dir'].replace(
        'docker', project_name)
    for index in range(len(backend['volumes'])):
        backend['volumes'][index] = backend['volumes'][index].replace(
            'docker', project_name
        )

    database['container_name'] = names['database']
    for index in range(len(database['environment'])):
        env = database['environment'][index]
        env = env.replace(
            'docker-database', names['database']
        )
        database['environment'][index] = env

    with open(os.path.join('.', '.env.example'), 'r+') as file:
        make_changes_in_file(file, 'docker-database', names['database'])

    frontend['container_name'] = names['frontend']
    frontend['working_dir'] = frontend['working_dir'].replace(
        'docker', project_name)
    frontend['volumes'] = backend['volumes'][::]

    jupyter['container_name'] = names['jupyter']
    jupyter['working_dir'] = jupyter['working_dir'].replace(
        'docker', project_name)
    jupyter['volumes'] = backend['volumes'][::]

    yaml_file['services']['backend'] = backend
    yaml_file['services']['database'] = database
    yaml_file['services']['frontend'] = frontend
    yaml_file['services']['jupyter'] = jupyter

    with open(os.path.join('.', 'docker-compose.yml'), 'w') as file:
        file.write(yaml.dump(yaml_file))


def main(*args, **kwargs):
    project_name = raw_input(
        'Project name (default: src): '
    ) or 'src'
    make_frontend(project_name=project_name, *args, **kwargs)
    make_docker(project_name=project_name, *args, **kwargs)
    make_backend(project_name=project_name, *args, **kwargs)


if __name__ == '__main__':
    main()
