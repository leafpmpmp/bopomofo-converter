import streamlit as st
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    st.title("精靈文產生器")
    st.write("這是一個精靈文產生器。請切換到英文模式後開始打字，按下Enter後即可看到對應的注音符號。")
    st.text_input("Enter text to convert to BOPOMOFO", key="input", on_change=update)
    f = st.radio("Select font", ["fern", "rock"], key="font")
    if f == "fern":
        st.markdown(
            """
            <style>
            @font-face {
            font-family: 'fern';
            src: url('https://github.com/justfont/Elffont/releases/download/v1.0/elffont-fern.otf');
            }
            html, body, [class*="fern"]  {
            font-family: 'fern';
            font-size: 16px;
            }
            </style>

            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            @font-face {
            font-family: 'rock';
            src: url('https://github.com/justfont/Elffont/releases/download/v1.0/elffont-rock.otf');
            }
            html, body, [class*="rock"]  {
            font-family: 'rock';
            font-size: 16px;
            }
            </style>

            """,
            unsafe_allow_html=True,
        )
    bopomofo_text =st.session_state.input
    if st.session_state.font == "fern":
        st.markdown(f'<p class="fern" style="font-family: fern">{bopomofo_text}</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p class="rock">{bopomofo_text}</p>', unsafe_allow_html=True)

def update():
    bopomofo = {'1': 'ㄅ', 'q': 'ㄆ', 'a': 'ㄇ', 'z': 'ㄈ', '2': 'ㄉ', 'w': 'ㄊ', 's': 'ㄋ', 'x': 'ㄌ', 
                'e': 'ㄍ', 'd': 'ㄎ', 'c': 'ㄏ', 'r': 'ㄐ', 'f': 'ㄑ', 'v': 'ㄒ', '5': 'ㄓ', 't': 'ㄔ', 
                'g': 'ㄕ', 'b': 'ㄖ', 'y': 'ㄗ', 'h': 'ㄘ', 'n': 'ㄙ', 'u': 'ㄧ', 'j': 'ㄨ', 'm': 'ㄩ',
                '8': 'ㄚ', 'i': 'ㄛ', 'k': 'ㄜ', ',': 'ㄝ', '9': 'ㄞ', 'o': 'ㄟ', 'l': 'ㄠ', '.': 'ㄡ',
                '0': 'ㄢ', 'p': 'ㄣ', ';': 'ㄤ', '/': 'ㄥ', '-': 'ㄦ', '4': 'ˋ', '6': 'ˊ', '3': 'ˇ', '7': '˙'}
    text = st.session_state.input
    bopomofo_text = ""
    for char in text:
        bopomofo_text += bopomofo.get(char, char)
    st.session_state.input = bopomofo_text

if __name__ == "__main__":
    main()
    