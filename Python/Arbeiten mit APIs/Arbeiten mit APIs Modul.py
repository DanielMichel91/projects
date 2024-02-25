from Arbeiten_mit_APIs import get_projects_from_github, create_barplot_projects

# Retrieve GitHub projects related to the Scala programming language.
get_projects_from_github("Scala")

# Create a bar plot for GitHub projects related to the Ruby programming language.
create_barplot_projects(projects=[0], language="Ruby")