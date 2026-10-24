import streamlit as st
import sys
from openai import OpenAI
class IdeaGenApp:
    api_key: str
    input: str

    def update_progress(self):
        if st.session_state.clicked:
            st.write("Button clicked.. Generating ideas...")
        else:
            st.write("")

    def click_button(self):
        self.update_progress()
        st.session_state.clicked = True
        self.fetch_ideas()
        
    def __init__(self):
        st.title("🎈 My new Business Ideas app")
        if 'clicked' not in st.session_state:
            st.session_state.clicked = False
        c = st.container()
        self.input = c.text_input("Enter a topic:", key = "name1")
        c.button("Generate ideas!", on_click=self.click_button)

    def init_secret(self):
        self.api_key = st.secrets["xAI_key"] 
        #print(self.api_key)

    def fetch_ideas(self):
        self.init_secret()
        if self.api_key:
            client = OpenAI(
                api_key=self.api_key,
                base_url="https://api.x.ai/v1")
        if self.input and st.session_state.clicked == True:
            with st.spinner("Generating ideas with Grok..."):
                try:
                    response = client.chat.completions.create(
                        model="grok-3",          # or "grok-beta"
                        messages=[
                            {"role": "system", "content": "You are a helpful business idea generator."},
                            {"role": "user", "content": f"Give me 8 realistic business ideas based on this topic: {self.input}. For each idea, give a short title and one-sentence description."}
                        ],
                        temperature=0.7,
                        max_tokens=800
                    )
    
                    ideas = response.choices[0].message.content
                    st.subheader("Generated Business Ideas")
                    st.write(ideas)
                except Exception as e:
                    st.error(f"Error: {e}")

if __name__ == '__main__':
    app = IdeaGenApp()
    sys.exit(0)





    



