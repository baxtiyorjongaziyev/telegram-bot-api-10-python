import pytest
from telegram_bot_api_10 import TelegramBotAPI10Client, build_input_checklist, rich_section_heading


def test_builders():
    h = rich_section_heading("Summary")
    assert h["type"] == "heading"
    chk = build_input_checklist("Tasks", [(1, "Step 1")])
    assert chk["title"] == "Tasks"


@pytest.mark.asyncio
async def test_client_transport():
    calls = []

    async def transport(method, payload):
        calls.append((method, payload))
        return {"ok": True, "result": True}

    client = TelegramBotAPI10Client("test-token", transport=transport)
    res = await client.call("getMe", {})
    assert res["ok"] is True
    assert calls[0][0] == "getMe"
