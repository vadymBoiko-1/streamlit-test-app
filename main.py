import json

import streamlit as st

_path = 'reservations_view.json'

def load_data() -> dict:
    # todo get from REDIS
    with open(_path) as f:
        return json.load(f)

def main() -> None:
    st.title("Reservations View")
    data = load_data()
    st.json(data)   # renders as collapsible tree
    return None


if __name__ == '__main__':
    main()