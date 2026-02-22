from lumi.domain.entities.recipe import Recipe

class RecipeRepository:
    def __init__(self):
        self._recipes = {
    "receita panqueca": Recipe(
        name="Panquecas",
        ingredients=[
            "1 xícara de farinha",
            "2 colheres de sopa de açúcar",
            "1 colher de sopa de fermento em pó",
            "1 xícara de leite",
            "1 ovo",
            "2 colheres de sopa de manteiga derretida"
        ],
        description="Panqueca é um bolo achatado e redondo à base de massa, preparado em uma chapa ou frigideira quente, geralmente feito com farinha, leite, ovos e um agente de fermentação como fermento em pó.",
        steps=[
            "Em uma tigela, misture a farinha, o açúcar e o fermento em pó.",
            "Em outra tigela, bata o leite, o ovo e a manteiga derretida.",
            "Combine os ingredientes líquidos e secos até misturar levemente.",
            "Aqueça uma frigideira antiaderente em fogo médio.",
            "Despeje 1/4 de xícara de massa para cada panqueca.",
            "Cozinhe até formar bolhas, depois vire e cozinhe até dourar."
        ]
    ),

    "receita arroz branco": Recipe(
        name="Arroz Branco",
        ingredients=[
            "1 xícara de arroz branco",
            "2 xícaras de água",
            "1/2 colher de chá de sal",
            "1 colher de sopa de manteiga (opcional)"
        ],
        description="O arroz branco é um grão básico, refinado e altamente versátil, processado pela remoção da casca, farelo e gérmen, restando apenas o endosperma branco rico em amido.",
        steps=[
            "Lave o arroz em água corrente fria até a água ficar transparente.",
            "Em uma panela, leve a água para ferver.",
            "Adicione o sal e a manteiga à água fervente.",
            "Acrescente o arroz, reduza o fogo para baixo e tampe a panela.",
            "Cozinhe por 18-20 minutos, ou até que a água seja absorvida e o arroz esteja macio.",
            "Retire do fogo e deixe descansar, tampado, por 5 minutos. Solte com um garfo antes de servir."
        ]
    )
}
    def get_recipe_by_name(self, name: str) -> Recipe | None:
        print(name)
        recipe = self._recipes.get(name.lower())
        if not recipe:
            print("receita não encontrada")
        return recipe
    
    def list_all_recipes(self) -> list[Recipe]:
        return list(self._recipes.values())