import pandas as pd

# remplacer par les candidats choisis
main_candidates = ["Emmanuel Macron","Marine Le Pen","Jean-Luc Mélenchon","Eric Zemmour","Valérie Pécresse","Yannick Jadot"]
other_candidates = ["Nicolas Dupont-Aignan","Jean Lassalle","Philippe Poutou","Anne Hidalgo","Nathalie Arthaud","Fabien Roussel"]

# remplacé par les couleurs choisies
colors = {
    "Emmanuel Macron":"#FFAB00",
    "Marine Le Pen":"#000008",
    "Jean-Luc Mélenchon": "#D50000",
    "Eric Zemmour": "#951DFF",
    "Valérie Pécresse": "#0051A7",
    "Yannick Jadot": "#239E5E",
    "Nicolas Dupont-Aignan":"#000008",
    "Jean Lassalle":"#F8CC00",
    "Philippe Poutou":"#BC1A1B",
    "Anne Hidalgo":"",
    "Nathalie Arthaud":"",
    "Fabien Roussel":""
}

# import polls-2022-aggregated
df_main = pd.read_csv("polls-2022-agregated.csv", usecols=["date"] + main_candidates)
df_other = pd.read_csv("polls-2022-agregated.csv", usecols=["date"] + other_candidates)

df_main = df_main.melt(id_vars=["date"], var_name="candidat", value_name="score agrégé")
df_other = df_other.melt(id_vars=["date"], var_name="candidat", value_name="score agrégé")

df_main["couleur"] = df_main.apply(
    lambda row: colors[row["candidat"]],
    axis=1
)

df_other["couleur"] = df_other.apply(
    lambda row: colors[row["candidat"]],
    axis=1
)

df_main.to_csv("main_candidates.csv")
df_other.to_csv("other_candidates.csv")