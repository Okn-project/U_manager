# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\app\\application.py'],
    pathex=['C:\\Users\\Mission\\Desktop\\main\\proj\\U_manager'],
    binaries=[],
    datas=[],
    hiddenimports=['src.app.application'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt6',
        'PySide6',
        'qt6',
        'Qt6'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='U_Manager',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
