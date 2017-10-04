import os
import json
import sys
import yaml
import shutil


def make_frontend(*args, **kwargs):
    json_file = {}
    project_name = raw_input(
        'Front-end project name (default: Frontend): '
    ) or 'Frontend'

    with open(os.path.join('.', 'frontend', 'package.json'), 'r') as file:
        json_file = json.load(file)

    json_file['name'] = project_name

    with open(os.path.join('.', 'frontend', 'package.json'), 'w') as file:
        file.write(json.dumps(json_file, indent=2))


def make_backend(*args, **kwargs):
    project_name = raw_input(
        'Backend-end project name (default: src): '
    ) or 'src'
    old_project_name = 'src'

    with open(os.path.join('.', 'backend', 'manage.py'), 'r+') as file:
        file_lines = file.readlines()
        old_project_name = file_lines[5].split(',')[1].strip().strip('"').split('.')[0]
        file_lines[5] = file_lines[5].replace(old_project_name, project_name)
        file.seek(0)
        file.write(''.join(file_lines))

    with open(os.path.join(
        '.', 'backend', old_project_name, 'settings', 'common.py'
    ), 'r+') as file:
        file_lines = file.readlines()
        file_lines[59] = file_lines[59].replace(old_project_name, project_name)
        file_lines[79] = file_lines[79].replace(old_project_name, project_name)
        file_lines[142] = file_lines[142].replace(old_project_name, project_name)
        file.seek(0)
        file.write(''.join(file_lines))

    with open(os.path.join(
        '.', 'backend', old_project_name, 'settings', 'development.py'
    ), 'r+') as file:
        file_lines = file.readlines()
        file_lines[0] = file_lines[0].replace(old_project_name, project_name)
        file.seek(0)
        file.write(''.join(file_lines))

    with open(os.path.join(
        '.', 'backend', old_project_name, 'settings', 'production.py'
    ), 'r+') as file:
        file_lines = file.readlines()
        file_lines[0] = file_lines[0].replace(old_project_name, project_name)
        file.seek(0)
        file.write(''.join(file_lines))

    with open(os.path.join(
        '.', 'backend', old_project_name, 'wsgi.py'
    ), 'r+') as file:
        file_lines = file.readlines()
        file_lines[13] = file_lines[13].replace(old_project_name, project_name)
        file.seek(0)
        file.write(''.join(file_lines))

    shutil.move(
        os.path.join('.', 'backend', old_project_name),
        os.path.join('.', 'backend', project_name)
    )


def make_docker(*args, **kwargs):
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

    if len(set(names.values())) != len(names.values()):
        sys.exit('All docker container names must be unique')

    with open(os.path.join('.', 'docker-compose.yml'), 'r') as file:
        yaml_file = yaml.load(file)

    yaml_file['services']['backend']['container_name'] = names['backend']
    yaml_file['services']['database']['container_name'] = names['database']
    yaml_file['services']['frontend']['container_name'] = names['frontend']

    with open(os.path.join('.', 'docker-compose.yml'), 'w') as file:
        file.write(yaml.dump(yaml_file))


def main(*args, **kwargs):
    make_frontend(*args, **kwargs)
    make_docker(*args, **kwargs)
    make_backend(*args, **kwargs)


if __name__ == '__main__':
    main()
