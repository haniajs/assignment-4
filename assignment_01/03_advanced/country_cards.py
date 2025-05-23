import streamlit as st
import requests

st.set_page_config(page_title="Country Info Cards", layout="wide")
st.title("🌍 Country Information Cards")

# Search box
search_query = st.text_input("Search for a country", "")

# Fetch country data
@st.cache_data
def get_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

countries = get_countries()

# Filter based on search
if search_query:
    countries = [c for c in countries if search_query.lower() in c["name"]["common"].lower()]

# Display country cards
num_cols = 3
cols = st.columns(num_cols)

for idx, country in enumerate(countries):
    with cols[idx % num_cols]:
        st.image(country["flags"]["png"], width=200)
        st.subheader(country["name"]["common"])
        st.write(f"**Capital:** {country.get('capital', ['N/A'])[0]}")
        st.write(f"**Region:** {country['region']}")
        st.write(f"**Population:** {country['population']:,}")
        currencies = country.get("currencies", {})
        if currencies:
            currency_names = ', '.join([f"{v['name']} ({k})" for k, v in currencies.items()])
            st.write(f"**Currencies:** {currency_names}")
        else:
            st.write("**Currencies:** N/A")
        st.markdown("---")
