Title: Les fixtures
Category: 3615 ma vie mon oeuvre
Tags: 3615, meta
Date: 2018/07/09 20:00
Modified: 2018/07/10 9:00
Summary: Hein, pour quoi ?
Image:
Lang: fr

___




```
class TestAccess:
    def _test_access(self, http_method, resource):
        http_method('/resources')
        assert resource.authorization_ctx.access == CollectionAccess.ALL

        http_method('/resources/1')
        assert resource.authorization_ctx.access == ItemAccess.SINGLE

        http_method('/self/resources')
        assert resource.authorization_ctx.access == CollectionAccess.SELF

        http_method('/others/2/resources')
        assert resource.authorization_ctx.access == CollectionAccess.RELATED

    def test_get(self, client, resource):
        self._test_access(client.simulate_get, resource)

    def test_post(self, client, resource):
        self._test_access(client.simulate_post, resource)

    def test_put(self, client, resource):
        self._test_access(client.simulate_put, resource)

    def test_patch(self, client, resource):
        self._test_access(client.simulate_patch, resource)

    def test_delete(self, client, resource):
        self._test_access(client.simulate_delete, resource)
```

```
@pytest.fixture(params=[
    {
        'endpoint': '/resources',
        'access': CollectionAccess.ALL,
    },
    {
        'endpoint': '/resources/1',
        'access': ItemAccess.SINGLE,
    },
    {
        'endpoint': '/self/resources',
        'access': CollectionAccess.SELF,
    },
    {
        'endpoint': '/others/2/resources',
        'access': CollectionAccess.RELATED,
    },
])
def scenario(request):
    return request.param

@pytest.fixture
def endpoint(scenario):
    return scenario['endpoint']

@pytest.fixture
def access(scenario):
    return scenario['access']

@pytest.fixture(params=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def http_method(client, request):
    method = getattr(client, 'simulate_{}'.format(request.param.lower()))
    return method

def test_access(resource, endpoint, access, http_method):
    http_method(endpoint)
    assert resource.authorization_ctx.access == access
```
