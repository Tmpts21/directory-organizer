
import json
import logging
from datetime import datetime
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)


def load_config(config_path: str = "config.json") -> dict:
    """Load the file organizer configuration."""
    path = Path(config_path)

    with path.open("r", encoding="utf-8") as config_file:
        return json.load(config_file)


def get_unique_path(destination: Path) -> Path:
    """Generate a unique filename if the destination already exists."""
    if not destination.exists():
        return destination

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    new_name = f"{destination.stem}_{timestamp}{destination.suffix}"
    candidate = destination.with_name(new_name)

    counter = 1
    while candidate.exists():
        new_name = (
            f"{destination.stem}_{timestamp}_{counter}"
            f"{destination.suffix}"
        )
        candidate = destination.with_name(new_name)
        counter += 1

    return candidate


def organize_files(
    directories: list[str],
    file_extensions: str,
    folder_name: str,
) -> int:
    """Move matching files into a specified folder in each directory."""
    extensions = {
        ext.lower() if ext.startswith(".") else f".{ext.lower()}"
        for ext in file_extensions.split()
    }

    moved_count = 0

    for directory in directories:
        source_dir = Path(directory)

        if not source_dir.is_dir():
            logging.warning("Directory does not exist: %s", source_dir)
            continue

        destination_dir = source_dir / folder_name

        for source_file in source_dir.iterdir():
            if not source_file.is_file():
                continue

            if source_file.suffix.lower() not in extensions:
                continue

            try:
                destination_dir.mkdir(parents=True, exist_ok=True)

                destination_file = get_unique_path(
                    destination_dir / source_file.name
                )

                source_file.rename(destination_file)
                moved_count += 1

                logging.info(
                    "Moved: %s -> %s",
                    source_file,
                    destination_file,
                )

            except OSError as error:
                logging.error(
                    "Failed to move %s: %s",
                    source_file,
                    error,
                )

    return moved_count


def run_script(config: dict) -> None:
    """Execute all enabled file organization rules."""
    directories = config["directory"]["path"]

    for rule in config.get("automate", []):
        organize = rule.get("organize", False)

        # Support both JSON booleans and legacy "True"/"False" strings.
        if isinstance(organize, str):
            organize = organize.strip().lower() == "true"

        if not organize:
            continue

        moved_count = organize_files(
            directories=directories,
            file_extensions=rule["file_ext"],
            folder_name=rule["type"],
        )

        logging.info(
            "Rule '%s' completed. Files moved: %d",
            rule["type"],
            moved_count,
        )


def main() -> None:
    """Application entry point."""
    try:
        config = load_config()
        run_script(config)
    except FileNotFoundError as error:
        logging.error("File not found: %s", error)
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        logging.error("Invalid configuration: %s", error)


if __name__ == "__main__":
    main()
