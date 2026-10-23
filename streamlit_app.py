import streamlit as st
from openai import OpenAI

st.title("🎈 My new Business Ideas app")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

c = st.container()
input = c.text_input("Enter a topic:")
c.button("Generate ideas!", on_click=click_button)

api_key = st.secrets["xAI_key"]
#st.write(api_key)

if api_key:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.x.ai/v1"
    )

if input:
    with st.spinner("Generating ideas with Grok..."):
        try:
            response = client.chat.completions.create(
                model="grok-3",          # or "grok-beta"
                messages=[
                    {"role": "system", "content": "You are a helpful business idea generator."},
                    {"role": "user", "content": f"Give me 8 realistic business ideas based on this topic: {input}. For each idea, give a short title and one-sentence description."}
                ],
                temperature=0.7,
                max_tokens=800
            )

            ideas = response.choices[0].message.content
            st.subheader("Generated Business Ideas")
            st.write(ideas)

        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.warning("Please enter a topic")



if st.session_state.clicked:
    st.write("Button clicked.. Generating ideas...")

else:
    st.write("")
