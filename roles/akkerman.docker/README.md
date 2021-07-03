Ansible Role for Docker
=========

Installs docker on Ubuntu with version pinning support.

Requirements
------------

None.

Role Variables
--------------

Role variables with their defaults:

```yaml
docker_version: "18.06"
docker_apt_key_id: 9DC858229FC7DD38854AE2D88D81803C0EBFCD88
docker_apt_key_url: https://download.docker.com/linux/ubuntu/gpg
docker_users: []
```

The `docker_version` should be the version you want pinned, so a newer version does not automatically get installed when adding a server later or when performing a apt upgrade. The packes `docker-ce` and `docker-ce-cli` will be pinned to the same version.

A more current example: 

```yaml
docker_version: "5:19.03"
```

The variable `docker_users` should be a list with one or more users that should be added to the docker group.

```yaml
docker_users:
  - ubuntu
  - vagrant
```


Dependencies
------------

None

Example Playbook
----------------


```yaml
- hosts: all
    become: true
    roles:
        - akkerman.docker
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
