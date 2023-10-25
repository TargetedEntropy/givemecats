
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Cats",
        page_icon="👋",
    )

    st.write("# Give me cats")

    st.sidebar.success("Select a feed above.")

    st.markdown(
        """This is cats."""
    )


if __name__ == "__main__":
    run()
