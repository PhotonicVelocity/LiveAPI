import re


def get_version_number(module) -> str:
    app = module.Application.get_application()  # get a handle to the App
    try:
        return (
            f"{app.get_major_version()}.{app.get_minor_version()}.{app.get_bugfix_version()}"
        )
    except Exception:
        # Fallback for older Live versions
        try:
            version = app.get_version_string()
        except Exception:
            return "unknown"

        match = re.search(r"(\\d+)\\.(\\d+)\\.(\\d+)", version)
        if match:
            return ".".join(match.groups())
        return version
