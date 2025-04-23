import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path

import app.utils
from app.gazo import Replay2Picture
from app.generation.common import vector
from app.version import Version

# Constants
CURRENT_VERSION = Version.from_str("0.8.3")
PRESET_FILE = 'preset.txt'
STYLE_TYPES = ['style 1', 'style 2']
DEFAULTS = {
    'message': '',
    'style': STYLE_TYPES[0],
    'width': '1920',
    'height': '1080',
    'dim': '0.6',
    'blur': '5',
    'border': '25',
}


def load_preset():
    if not os.path.exists(PRESET_FILE):
        return DEFAULTS.copy()
    presets = {}
    with open(PRESET_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if ':' not in line:
                continue
            key, val = line.strip().split(':', 1)
            presets[key.strip()] = val.strip()
    for k, v in DEFAULTS.items():
        presets.setdefault(k, v)
    return presets


def save_presets(values):
    with open(PRESET_FILE, 'w', encoding='utf-8') as f:
        for key in DEFAULTS:
            f.write(f"{key}: {values[key]}\n")


class Display(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('osu Thumbnail Generator')
        self.resizable(True, False)

        # Load presets
        presets = load_preset()
        self.vars = {k: tk.StringVar(value=presets[k]) for k in DEFAULTS}
        self.replay_path = tk.StringVar()
        self.beatmap_path = tk.StringVar()

        # Widgets setup
        self.create_widgets()
        self.grid_columnconfigure(1, weight=1)

    def browse_replay(self):
        path = filedialog.askopenfilename(
            title='Select replay file',
            filetypes=[('OSR files', '*.osr')]
        )
        if path:
            self.replay_path.set(path)
            # Update window title
            stem = Path(path).stem
            self.title(f'osu Thumbnail Generator - {stem}')

    def browse_beatmap(self):
        path = filedialog.askopenfilename(
            title='Select beatmap file',
            filetypes=[('OSU files', '*.osu')]
        )
        if path:
            self.beatmap_path.set(path)

    def create_widgets(self):
        # Replay selector
        tk.Label(self, text='Replay (.osr):').grid(row=0, column=0, sticky='e', padx=5, pady=2)
        tk.Entry(self, textvariable=self.replay_path, state='readonly').grid(row=0, column=1, sticky='ew', padx=5)
        tk.Button(self, text='Browse', command=self.browse_replay).grid(row=0, column=2, padx=5)

        # Beatmap selector
        tk.Label(self, text='Beatmap (.osu):').grid(row=1, column=0, sticky='e', padx=5, pady=2)
        tk.Entry(self, textvariable=self.beatmap_path, state='readonly').grid(row=1, column=1, sticky='ew', padx=5)
        tk.Button(self, text='Browse', command=self.browse_beatmap).grid(row=1, column=2, padx=5)

        # Parameter fields
        labels = ['message', 'style', 'width', 'height', 'dim', 'blur', 'border']
        for i, field in enumerate(labels, start=2):
            tk.Label(self, text=f'{field}:').grid(row=i, column=0, sticky='e', padx=5, pady=2)
            if field == 'style':
                ttk.Combobox(
                    self,
                    textvariable=self.vars[field],
                    values=STYLE_TYPES,
                    state='readonly'
                ).grid(row=i, column=1, sticky='ew', padx=5)
            else:
                tk.Entry(
                    self,
                    textvariable=self.vars[field]
                ).grid(row=i, column=1, sticky='ew', padx=5)

        # Buttons
        btn_row = len(labels) + 2
        frame = tk.Frame(self)
        frame.grid(row=btn_row, column=0, columnspan=3, pady=10)
        tk.Button(frame, text='Save Preset', command=self.on_save).pack(side='left', padx=5)
        tk.Button(frame, text='Run', command=self.on_run).pack(side='left', padx=5)

    def on_save(self):
        values = {k: self.vars[k].get() for k in DEFAULTS}
        save_presets(values)
        messagebox.showinfo('Saved', f'{PRESET_FILE} updated.')

    def on_run(self):
        # Validate replay
        if not self.replay_path.get():
            messagebox.showerror('Error', 'Replay file is required.')
            return
        # Init tasks
        for task in (app.utils.ensure_directories, app.utils.ensure_default_assets):
            if code := task():
                messagebox.showerror('Init Error', f'Init failed: {code}')
                return
        # Version check
        try:
            app.utils.ensure_up_to_date(CURRENT_VERSION)
        except Exception:
            pass
        # Paths
        replay_file = Path(self.replay_path.get())
        beatmap_file = Path(self.beatmap_path.get()) if self.beatmap_path.get() else None
        # Construct output in Downloads with same stem
        stem = replay_file.stem
        output_file = f'{stem}.png'
        # Debug
        print(f"Replay: {replay_file}\nBeatmap: {beatmap_file}\nOutput: {output_file}")
        try:
            # Generate
            replay = Replay2Picture.from_replay_file(
                replay_path=replay_file,
                beatmap_file=beatmap_file
            )
            replay.calculate()
            result = replay.generate(
                style=int(self.vars['style'].get().split(' ')[1]),
                resolution=vector.Vector2(
                    x=int(self.vars['width'].get()),
                    y=int(self.vars['height'].get())
                ),
                background_dim=float(self.vars['dim'].get()),
                background_blur=float(self.vars['blur'].get()),
                background_border=float(self.vars['border'].get()),
                message=self.vars['message'].get(),
                custom_filename=str(output_file)
            )
            saved = Path(result) if result else output_file
            if not saved.exists():
                messagebox.showerror('Error', f'File not found after generation:\n{saved}')
                return
            messagebox.showinfo('Done', f'Image saved to:\n{saved}')
            if sys.platform.startswith('win'):
                os.startfile(str(saved))
        except Exception as e:
            messagebox.showerror('Error', f'Generation failed:\n{e}')


if __name__ == '__main__':
    Display().mainloop()
