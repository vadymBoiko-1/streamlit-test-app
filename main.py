import data_manager
import streamlit as st

def main() -> None:
    st.title("Reservations View")
    data = data_manager.pull_data()
    st.json(data)   # renders as collapsible tree
    return None


if __name__ == '__main__':
    main()