#! /usr/bin/env python3

import base64
import json
import math
import os
import time

import requests

import git


def make_request(url, creds, pagelen=1, page=1):
    headers = {
        'authorization': 'Basic {}'.format(creds),
    }
    querystring = {
        "pagelen": pagelen,
        "page": page,
    }
    return requests.get(url, headers=headers, params=querystring)


def get_repos_quantity(url, creds):
    return make_request(url, creds).json()['size']


def get_repos_data(url, creds):
    pagesize = 1
    pages = math.ceil(get_repos_quantity(url, creds) / pagesize)

    def get_type(name):
        if 'exercise' in name:
            return 'exercise'
        if 'challenge' in name:
            return 'challenge'
        if 'course' in name:
            return 'course'
        return ''

    repos = []

    for i in range(1, pages + 1):
        repo = make_request(url, creds, pagesize, i).json()['values']
        dir_name = repo[0]['project']['name']  # parent dir
        repo_name = repo[0]['name']
        repo_type = get_type(repo_name)
        clone_links = repo[0]['links']['clone']
        ssh_link = list(filter(
            lambda link: link['name'] == 'ssh', clone_links))[0]['href']

        repos.append({
            'dir': dir_name,
            'name': repo_name,
            'type': repo_type,
            'link': ssh_link,
        })

        time.sleep(2)

    return repos


def clone(repo, paths):
    if repo['type']:
        parent_dir = paths[repo['type']]
        path = '{}/{}/{}'.format(parent_dir, repo['dir'], repo['name'])
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            print('Cloning {}'.format(repo['name']))
            git.Repo.clone_from(repo['link'], path)
            print('Done')
            return time.sleep(2)
        print('Already exists')


def main(config):
    url = '{}{}'.format(config['apiurl'], config['teamname'])
    cred_bytes = ('{}:{}'.format(
        config['username'],
        config['password']).encode('utf-8'))
    credentials = str(base64.b64encode(cred_bytes), 'utf-8')
    paths = config['dirs']

    for repo in get_repos_data(url, credentials):
        clone(repo, paths)


if __name__ == '__main__':
    with open('config.json') as config:
        main(json.load(config))
