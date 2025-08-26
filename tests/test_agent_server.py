import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.agent_server import app

client = TestClient(app)

# ユーザ入力を受け取り、各演算サーバを呼ぶ関数をモックする例
@pytest.mark.parametrize(
    "expr,expected_result",
    [
        ("4+4", 8.0),
        ("5-2", 3.0),
        ("6*3", 18.0),
        ("8/2", 4.0),
    ]
)
def test_agent_operations(expr, expected_result):
    # 四則演算サーバへのHTTP呼び出しをモック
    with patch("src.agent_server.requests.post") as mock_post:
        # モックの返り値を設定
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"result": expected_result}

        # エージェントサーバにアクセス
        res = client.post("/calculate", json={"expr": expr})

        # 結果を検証
        assert res.status_code == 200
        assert res.json() == {"result": expected_result}

        # 適切なサーバに POST されているかを確認
        if "+" in expr:
            mock_post.assert_called_with("http://localhost:8001/add", json={"a":4.0, "b":4.0})
        elif "-" in expr:
            mock_post.assert_called_with("http://localhost:8002/sub", json={"a":5.0, "b":2.0})
        elif "*" in expr:
            mock_post.assert_called_with("http://localhost:8003/mul", json={"a":6.0, "b":3.0})
        elif "/" in expr:
            mock_post.assert_called_with("http://localhost:8004/div", json={"a":8.0, "b":2.0})
