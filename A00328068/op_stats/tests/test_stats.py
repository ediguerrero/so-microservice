import pytest
from op_stats.app import app

@pytest.fixture
def client():
 

def test_get_cpu_percent(client):
  respose = client.get('/v1/stats/cpu')
  assert '{"cpu_percent":100}' in response.data.decode('utf-8')
  assert response.status_code == 200

