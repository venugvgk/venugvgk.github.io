"""Script to sync selected articles from Obsidian to Quarto website.
"""
import argparse
import logging
from pathlib import Path
import yaml
import io
import subprocess
import shutil

p = argparse.ArgumentParser()
p.add_argument("-d", "--obsidian-directory", help="Path to the obsidian directory", required=True)
p.add_argument("--no-git", dest="git", action="store_false", default=True,
               help="Only copy files, don't commit and push to git")

logger = logging.getLogger()

def setup_logging():
    level = logging.INFO
    format = '[%(asctime)s] %(message)s'
    datefmt = '%Y-%d-%m %H:%M:%S'

    logging.basicConfig(
        level=level,
        format=format,
        datefmt=datefmt)

class MarkdownFile:
    """Markfown file to be synced.
    """
    def __init__(self, path):
        self.path = path
        self.contents = path.read_text()
        if "quarto-sync" in self.contents:
            self.metadata = self.read_metadata()
        else:
            self.metadata = {}

    def is_sync_enabled(self):
        return self.metadata.get("quarto-sync") in [True, "true"]

    def read_metadata(self):
        text = self._read_metadata_text()
        return yaml.safe_load(io.StringIO(text))

    def _read_metadata_text(self):
        lines = self.contents.splitlines()
        if not lines or lines[0] != "---":
            return ""

        meta_lines = []
        for line in lines[1:]:
            if line.strip() == "---":
                break
            meta_lines.append(line)

        return "\n".join(meta_lines)

    def sync(self, state):
        filename = self.metadata.get("quarto-filename")
        if filename is None:
            logger.error("%s: quarto-filename is missing", self.path)
            return

        logger.info("cp %s %s", self.path, filename)
        shutil.copy(self.path, filename)
        state['modified_files'].append(filename)

        parent = Path(filename).parent
        assets = self.find_assets()
        for asset_filename in assets:
            src_path = Path(self.path).parent / asset_filename
            dest_path = Path(filename).parent / asset_filename
            logger.info("cp %s %s", src_path, dest_path)
            shutil.copy(src_path, dest_path)
            state['modified_files'].append(dest_path)

    def find_assets(self):
        image = self.metadata.get("image")
        if image:
            yield image

    @staticmethod
    def find_files_to_sync(obsidian_directory):
        """Find all files that need to be synced.
        """
        root = Path(obsidian_directory)
        files = (MarkdownFile(path) for path in root.rglob("*.md"))
        return [f for f in files if f.is_sync_enabled()]

def sync_files(obsidian_directory):
    """Syncs files from obsidian directory and returns paths to the modified files.
    """
    state = {"modified_files": []}
    files = MarkdownFile.find_files_to_sync(obsidian_directory)
    logger.info("found %d files", len(files))
    for f in files:
        f.sync(state)
    return state['modified_files']

def run_command(cmd):
    logger.info("RUN %s", cmd)
    subprocess.run(cmd, shell=True, check=True)

def main():
    setup_logging()
    logger.info("BEGIN OBSIDIAN SYNC")
    args = p.parse_args()

    if args.git:
        run_command("git pull")

    modified_files = sync_files(args.obsidian_directory)

    if args.git:
        for f in modified_files:
            run_command(f"git add {f}")
        run_command("git commit -m 'obsidian sync'")
        run_command("git push")

    logger.info("END OBSIDIAN SYNC")

if __name__ == "__main__":
    main()