from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from typing import Optional

from rosu_pp_py import PerformanceAttributes

from app.generation.canvas import Canvas
from app.generation.canvas import CanvasSettings
from app.generation.canvas import CanvasStyle
from app.generation.canvas import Vector2
from app.objects.beatmap import Beatmap
from app.objects.replay import ReplayInfo

#
OUTPUT_FOLDER: Path = Path.cwd() / "outputs"
OUTPUT_FOLDER.mkdir(exist_ok=True)

# Common
DEFAULT_FILENAME_FORMAT: str = "[{name}] - ({artist} - {title} [{diff}])"
FILENAME_INVALID_REGEX: re.Pattern = re.compile(r'[<>:"/\\|?*]')


class Replay2Picture:
    def __init__(self) -> None:
        self.replay: ReplayInfo
        self.beatmap: Beatmap
        self.info: PerformanceAttributes

    # rosu-pp doesn't yet support csr so this will be vastly different from live pp values
    def calculate(self) -> None:
        print("[Replay2Picture] Calculating PP,", end="")
        self.info = self.beatmap.calculate_pp(
            mods=self.replay.mods,  # type: ignore
            acc=self.replay.accuracy.value,  # type: ignore
            combo=self.replay.max_combo,  # type: ignore
            misses=self.replay.accuracy.hitmiss,  # type: ignore
        )

        print(" done!")

    def generate(self, style: int = 1, **kwargs: dict[Any, Any]) -> Path:
        custom_filename: str = kwargs.pop("custom_filename", "")  # type: ignore

        settings: CanvasSettings = CanvasSettings(
            style=CanvasStyle(style),
            context=self,
            **kwargs,
        )

        canvas: Canvas = Canvas.from_settings(settings=settings)

        image = canvas.generate()

        # Filename
        filename: str = DEFAULT_FILENAME_FORMAT

        if custom_filename:
            filename = custom_filename.removesuffix(
                ".png",
            )  # Remove any trailing .png just incase

        # Format the shit
        filename: str = filename.format(
            name=canvas.context.replay.player_name,
            artist=canvas.context.beatmap.artist,
            title=canvas.context.beatmap.title,
            diff=canvas.context.beatmap.difficulty,
        )

        filename = filename

        result_image_path = OUTPUT_FOLDER / (
            FILENAME_INVALID_REGEX.sub("", filename) + ".png"
        )
        image.save(fp=result_image_path, format="png")

        return result_image_path

    @classmethod
    def from_replay_file(
        cls,
        replay_path: Path,
        beatmap_file: Path | None = None,
    ) -> Replay2Picture:
        print(f"[Replay2Picture] File: `{replay_path.name}`")

        self: Replay2Picture = cls()
        self.replay = ReplayInfo.from_file(replay_path)

        if not beatmap_file and self.replay.beatmap_md5:
            print("[Replay2Picture] No Beatmap file passed, getting from osu!")
            self.beatmap = Beatmap.from_md5(self.replay.beatmap_md5)
        elif beatmap_file:
            print("[Replay2Picture] Beatmap file passed, using that instead.")
            self.beatmap = Beatmap.from_osu_file(beatmap_file)

        return self

    @classmethod
    def from_beatmap_file(cls, beatmap_file: Path) -> Replay2Picture:
        ...
