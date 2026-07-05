# 🧬 CODENAME: STRAIN ISOLATION

`CODENAME: STRAIN ISOLATION` on dynaaminen ja kevyt dataohjelmisto, joka on suunniteltu analysoimaan ja erottelemaan GitHub-käyttäjien julkisten repositorioiden koodikantoja (kieliä).

---

## 🚀 Ominaisuudet
* **Live-diagnostiikka:** Hakee reaaliaikaista dataa GitHub API:sta valitun käyttäjätunnuksen perusteella.
* **Kantojen erottelu (Strain Isolation):** Laskee ja visualisoi tarkan tavukohtaisen jakauman eri ohjelmointikielten välillä.
* **Plotly-graafi:** Responsiivinen horisontaalinen pylväsdiagrammi.
* **Tietoturvallinen arkkitehtuuri:** API-tokenit on eristetty kokonaan lähdekoodista ja ne hallitaan salatusti ympäristömuuttujien (`st.secrets`) kautta.

---

## 🛠️ Teknologiat
* **Python** (Taustalogiikka ja datan käsittely)
* **Streamlit** (Käyttöliittymä ja globaali teemanhallinta via `config.toml`)
* **Plotly Go** (Dynaaminen ja responsiivinen datan visualisointi)

---

## 🌐 Live-versio
Sovellus on julkaistu ja sitä voi ajaa livenä täällä:  
👉 [CODENAME: STRAIN ISOLATION - Live App](https://strain-isolation.streamlit.app/)