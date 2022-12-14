import pytest


@pytest.fixture(scope="session")
def alice(accounts):
    return accounts[0]

@pytest.fixture(scope="session")
def bob(accounts):
    return accounts[1]

@pytest.fixture(scope="session")
def my_contract(project, alice):
    return alice.deploy(project.TokenVendor)