import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_pref_file(host):
    f = host.file('/etc/apt/preferences.d/docker-ce.pref')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('pkg', [
  'docker-ce',
  'docker-ce-cli'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


def test_docker_service(host):
    service = host.service('docker.service')

    assert service.is_running
    assert service.is_enabled
