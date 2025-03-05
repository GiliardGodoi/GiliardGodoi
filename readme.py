'''
Tanks to @fishnets88
https://github.com/koaning/koaning/tree/main
'''
from rich.console import Console
from rich.tree import Tree
from rich.markdown import Markdown

console = Console(record=True, width=100)

# Estrutura de diretórios formatada com Rich
# tree = Tree("Giliard_Godoi", guide_style="bold bright_black")
tree = Tree("[link=https://giliardgodoi.github.io/]Giliard_Godoi[/link]", style='bold', guide_style='bright_black')

formacao = tree.add("📂 Formação_Acadêmica/")
formacao.add("🎓 Estudante_Doutorado_ICMC_USP.txt")
formacao.add("🎓 Mestrado_Informatica_UTFPR.txt")
formacao.add("🎓 Tecnólogo_ADS_UTFPR.txt")
formacao.add("🎓 Licenciatura_Matemática_UENP.txt")

areas = tree.add("📂 Áreas_de_Interesse/")
areas.add("🧠 Aprendizado_de_Maquina.ipynb")
areas.add("🤖 Redes_Neurais.ipynb")
areas.add("🔠 Processamento_de_Linguagem_Natural.ipynb")
areas.add("📜 Sumarização_Automática.ipynb")
areas.add("🔍 Constrastive_Learning.ipynb")
areas.add("🔄 Alinhamento_Modelos_Linguagem.ipynb")
areas.add("📊 Análise_Visualização_Dados.ipynb")
areas.add("🏆 Algoritmos_Evolutivos.py")

projetos = tree.add("📂 Projetos_e_Pesquisas/")
projetos.add("🔹 Redes_Neurais_Contrastivas.txt")
projetos.add("🔹 Fine_tuning_Modelos_Linguagem.txt")
projetos.add("🔹 Sumarizacao_Textos_Longos.txt")

repos = tree.add("📂 Repositórios_Destaque/")
repos.add("🔗 [link=https://github.com/GiliardGodoi/tj-datasets]tjdatasets/[/link]")
repos.add("🔗 [link=https://github.com/GiliardGodoi/xsteiner]xsteiner/[/link]")

contato = tree.add("📂 Contato")
contato.add("🔗 [link=https://www.linkedin.com/in/giliardgodoi]LinkedIn.txt[/link]")

# Exibir no terminal
console.print(tree)
# console.print("")
# console.print("[green]Follow me on twitter [bold link=https://twitter.com/fishnets88]@fishnets88[/]")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)