import streamlit as st


def creds_entered():
    if st.session_state["user"].strip() == "admin" and st.session_state["passwd"].strip() == "admin":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please enter password")
        elif not st.session_state["user"]:
            st.warning["Please enter username"]
        else:
            st.error("Invalid Username/Pass :face_with_raised_eyebrow: :man-shrugging: :yawning_face:")


def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
        st.text_input(
            label="Password:",
            value="",
            key="passwd",
            type="password",
            on_change=creds_entered,
        )
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
            st.text_input(
                label="Password:",
                value="",
                key="passwd",
                type="password",
                on_change=creds_entered,
            )
            return False
