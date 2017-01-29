import requests

from mocket.plugins.pook import MocketEngine


def test_pook_engine():
    import pook

    pook.activate()

    pook.set_mock_engine(MocketEngine)

    url = 'http://twitter.com/api/1/foobar'
    status = 404
    response_json = {'error': 'foo'}

    mock = pook.get(
        url,
        headers={'content-type': 'application/json'},
        reply=status,
        response_json=response_json,
    )
    mock.persist()

    requests.get(url)
    assert mock.calls == 1

    resp = requests.get(url)
    assert resp.status_code == status
    assert resp.json() == response_json
    assert mock.calls == 2

    pook.disable()
