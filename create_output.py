from jinja2 import Environment, FileSystemLoader

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
    with open("outputs/report.html", "w") as f:
        f.write(template.render(event_name=report.event_name, event_year=report.event_code[:4], team_infos=report.team_infos, report=report))


# if __name__ == "__main__":
#     main()
