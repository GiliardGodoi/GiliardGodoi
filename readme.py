'''
Tanks to @fishnets88
https://github.com/koaning/koaning/tree/main
'''
from rich.console import Console
from rich.tree import Tree
from rich.markdown import Markdown

console = Console(record=True, width=100)

# Estrutura de diretórios formatada com Rich
tree = Tree("[bold blue]# Giliard_Godoi[/bold blue]")

formacao = tree.add("[bold]📂 Formação_Acadêmica/[/bold]")
formacao.add("🎓 [bold]Doutorado_ICMC_USP.txt[/bold]")
formacao.add("🎓 [bold]Mestrado__UTFPR.txt[/bold]")
formacao.add("🎓 [bold]Tecnólogo_ADS_UTFPR.txt[/bold]")
formacao.add("🎓 [bold]Licenciatura_Matemática_UENP.txt[/bold]")

areas = tree.add("[bold]📂 Áreas_de_Interesse/[/bold]")
areas.add("🧠 [bold]Aprendizado_de_Maquina.ipynb[/bold]")
areas.add("🤖 [bold]Redes_Neurais.ipynb[/bold]")
areas.add("🔠 [bold]Processamento_de_Linguagem_Natural.ipynb[/bold]")
areas.add("📜 [bold]Sumarização_Automática.ipynb[/bold]")
areas.add("🔍 [bold]Constrastive_Learning.ipynb[/bold]")
areas.add("🔄 [bold]Alinhamento_Modelos_Linguagem.ipynb[/bold]")
areas.add("📊 [bold]Análise_Visualização_Dados.ipynb[/bold]")
areas.add("🏆 [bold]Algoritmos_Evolutivos.py[/bold]")

projetos = tree.add("[bold]📂 Projetos_e_Pesquisas/[/bold]")
projetos.add("🔹 [bold]Redes_Neurais_Contrastivas.txt[/bold]")
projetos.add("🔹 [bold]Fine_tuning_Modelos_Linguagem.txt[/bold]")
projetos.add("🔹 [bold]Sumarizacao_Textos_Longos.txt[/bold]")

repos = tree.add("[bold]📂 Repositórios_Destaque[/bold]")
repos.add("🔗 [bold][link=https://github.com/GiliardGodoi/xsteiner]xsteiner/[/link][/bold]")

contato = tree.add("[bold]📂 Contato[/bold]")
contato.add("🔗 [bold][link=https://www.linkedin.com/in/giliardgodoi]LinkedIn.txt[/link][/bold]")

# Exibir no terminal
console.print(tree)
# console.print("")
# console.print("[green]Follow me on twitter [bold link=https://twitter.com/fishnets88]@fishnets88[/]")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)