from src.utils.preprocess import clean_text

def test_clean_text():
    text = "Hello @user visit http://example.com #AI"
    cleaned = clean_text(text)
    assert "http" not in cleaned
    assert "@user" not in cleaned
