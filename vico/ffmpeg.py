import shutil
import sys
import logging
import subprocess

import vico.context as ctx

logger = logging.getLogger(__name__)


def precheck():
    if not has_binaries():
        print(
            "'ffmpeg' is not installed. Consider installing it with your package manager.",
            file=sys.stderr,
        )
        sys.exit(1)
    progs_versions()


def has_binaries() -> bool:
    return shutil.which("ffprobe") is not None and shutil.which("ffmpeg") is not None


def progs_versions():  # -> list[str]:
    versions = {}
    for prog in ["ffprobe", "ffmpeg"]:
        completed = subprocess.run([prog, "-version"], capture_output=True)
        versions[prog] = completed.stdout.splitlines()
        logger.debug("%s version is %s", prog, versions[prog][0])
    ctx.context["versions"] = versions
