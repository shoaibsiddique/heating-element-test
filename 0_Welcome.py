# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello to Warm Kussens",
        page_icon="👋",
    )
    st.write("# Welcome to Temperature Data Analysis for Warm Kussens!")

    #st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        This web application is designed for the analysis of temperature data of 4 different patterns for the heating element that we have.
        In this web app, you can find the data for different heating elements patterns. Go to the tab **analyze data** in 
        the side bar 👈 to analyze the data for the pattern you are interested in.
    """
    )


if __name__ == "__main__":
    run()