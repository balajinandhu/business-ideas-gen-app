from streamlit.testing.v1 import AppTest

def test_click_button():
    at = AppTest.from_file("src/streamlit_app.py").run()
    at.button[0].click().run()
    assert at.write[0] == "Button clicked.. Generating ideas..."