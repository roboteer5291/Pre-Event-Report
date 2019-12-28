from jinja2 import Environment, FileSystemLoader
from os import path, makedirs

directory_name = "outputs/"
file_name = "report.html"
file_path = directory_name + file_name

# Content to be published
content = "Hello, world!"

# Configure Jinja and ready the template
env = Environment(
    loader=FileSystemLoader(searchpath="templates")
)
template = env.get_template("report.html")


def main(report):
    """
    Entry point for the script.
    Render a templates and write it to file.
    :return:
    """
    if not path.exists(directory_name):
        makedirs(directory_name)
    with open(file_path, "w+") as f:
        f.write(template.render(event_name=report.event_name, event_year=report.event_code[:4], team_infos=report.team_infos, report=report))


# if __name__ == "__main__":
#     main()
